"""⚽ Terrain de foot souterrain du spawn : python tools/lobby/gen_foot.py .
(depuis la racine du dépôt ; idempotent ; APRÈS gen_lobby.py, gen_pvpcave.py et gen_events.py, AVANT gen_themes.py)

Un trou 2×2 dans la place nord (à côté du portail de Terra Nova, x -1..0, z -17..-16) mène à un vestiaire creusé dans la roche, puis au
terrain (31×19, sol vert, deux buts) en dessous. Une balle (sulfur_cube) au centre ; deux équipes au choix sur les socles du vestiaire.
Un but compte pour l'équipe ADVERSE du but, quel que soit le tireur. Aucune équipe sur le terrain : buts libres. Pas de PvP sur le terrain.
- foot_build.py : géométrie, constantes de sélecteur (FOOT_ZONE, aussi lue par gen_sit.py), foot/build, labels, trou, build_start / build_go.
- foot_game.py : foot/tick, foot/second, balle, buts, score.  foot_teams.py : équipes mg_ftr / mg_ftb, socles, cleanup.
- foot_admin.py : mg.opt 84 (on/off) et 85 (compteurs), boutons du menu des événements.
Tout est reconstruit si le bloc témoin (pierre de magnétite en (2, 46, -31)) disparaît ; forceload permanent de la zone (core/forceloads).
Le bloc témoin est posé en dernier par foot/build, et core/tick ne lance la reconstruction que si les 4 coins de la zone sont chargés.
Reconstruction du spawn (lobby/build, ex. changement de version) : elle remplit de nouveau la roche (y 46..58) et le sol carré de la place,
donc rebouche le trou et efface le terrain. Pour le refaire dans la foulée, foot/build est appelé à la fin de lobby/build_end (patch plus bas).
Limite : entre les étapes build_5 et build_8 le bloc témoin peut manquer (roche remplie avant le sol) : la reconstruction de core/tick,
si elle part pendant ces étapes, est alors écrasée par la suite de lobby/build, puis refaite par lobby/build_end. Ne pas lancer foot/build
à la main pendant lobby/build.
Les fonctions de construction sont sous foot/ (PAS sous lobby/theme/) : theme_world.load les classe DYN, les décors saisonniers n'y touchent pas.
foot/ est effacé puis réécrit à chaque passage (comme gen_elyrace.py ; remis en place si un contrôle du site échoue) ; gen_events.py réécrit
lobby_events.json et menu_chat : relancer ensuite gen_foot.py PUIS gen_sit.py (gen_rating régénère rate/d/lobby_events).
Objectifs : mg.ft (scores), mg.ftn (compteurs) ; équipes mg_ftr, mg_ftb ; tags mg.ftr, mg.ftb, mg.ftin, mg.ball, mg.ftd.
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C
import foot_admin as FA
import foot_build as FB
import foot_game as FG
import foot_teams as FT
import theme_world as TW

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')


def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1] and a[2] <= b[3] and b[2] <= a[3] and a[4] <= b[5] and b[4] <= a[5]


def check_site():
    """Le générateur s'arrête avant d'écrire quoi que ce soit si le site n'est pas celui qu'on croit."""
    # TW.RESERVED est vide ici (seul theme_npcs.prepare le remplit, plus tard) : le test ne porte en pratique que sur PAD_BOXES
    for name, box in (('terrain', FB.SHELL), ('vestiaire', FB.LOCKER), ('puits', FB.SHAFT)):
        for d in TW.DYN:
            assert not overlap(box, d), f'{name} {box} touche une zone modifiée ailleurs (DYN) : {d}'
        for r in TW.RESERVED + TW.PAD_BOXES:
            assert not overlap(box, r), f'{name} {box} touche une zone réservée : {r}'
        for x in range(box[0], box[1] + 1):
            for y in range(box[2], min(box[3], 62) + 1):
                for z in range(box[4], box[5] + 1):
                    # la roche de l'île est dans W (pierre de y 46 à 58, terre de 59 à 62) : tout ce qu'on creuse y est déjà plein (rien dans le vide)
                    assert TW.solid(x, y, z) and (x, y, z) in TW.W, f'{name} : pas de roche en {(x, y, z)} ({TW.W.get((x, y, z))})'
    assert all(abs(c) < TW.LIM for c in (FB.SHELL[0], FB.SHELL[1], FB.SHELL[4], FB.SHELL[5]))
    hx, hz = FB.HOLE
    for x in range(hx - 1, hx + 3):
        for z in range(hz - 1, hz + 3):
            assert (x, 63, z) in TW.W, f'pas de sol du spawn en {(x, 63, z)}'
    for dx, dz in ((-1, -1), (2, -1), (-1, 2), (2, 2)):          # piquets (y 64 et 65) : rien d'autre du spawn à leur place
        assert not any((hx + dx, y, hz + dz) in TW.W for y in (64, 65)), f'décor du spawn à la place d\'un piquet ({dx}, {dz})'
    for x in (hx, hx + 1):                                       # colonne du trou (y 64..66, vidée par foot/build) : rien du spawn dedans
        for z in (hz, hz + 1):
            assert not any((x, y, z) in TW.W for y in (64, 65, 66)), f'décor du spawn dans la colonne du trou ({x}, {z})'


# ---------------------------------------------------------------- foot/ mis de côté pendant les contrôles et l'écriture (restauré en cas d'échec)
foot_dir = os.path.join(C.F, 'foot')
bak = tempfile.mkdtemp(prefix='foot_bak_')
if os.path.isdir(foot_dir):
    shutil.move(foot_dir, os.path.join(bak, 'foot'))
try:
    TW.load(C.F)                         # sans foot/ : le modèle du spawn ne connaît pas encore notre construction
    check_site()
    FB.write()
    FG.write()
    FT.write()
    FA.write()
except BaseException:
    shutil.rmtree(foot_dir, ignore_errors=True)
    if os.path.isdir(os.path.join(bak, 'foot')):
        shutil.move(os.path.join(bak, 'foot'), foot_dir)
    raise
finally:
    shutil.rmtree(bak, ignore_errors=True)

# ---------------------------------------------------------------- câblage (une ligne par patch)
C.objectives([('mg.ft', 'dummy'), ('mg.ftn', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.ftn dummy', [f'scoreboard players add {n} mg.ft 0' for n in ('$ftr', '$ftb', '$ftg', '$fte', '$fti')])
C.patch('core/load', 'team modify mg_party collisionRule never', [
    '# Équipes du terrain de foot (pas celles des jeux)',
    'team add mg_ftr', 'team modify mg_ftr color red', 'team modify mg_ftr friendlyFire false',
    'team modify mg_ftr prefix [{"text":"⬤ ","color":"red"}]',
    'team add mg_ftb', 'team modify mg_ftb color blue', 'team modify mg_ftb friendlyFire false',
    'team modify mg_ftb prefix [{"text":"⬤ ","color":"blue"}]'])
C.patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby pvpc2 run schedule function mg:pvpc/build_start 22s', [
    'execute if score $setup mg.st matches 1 unless data storage mg:lobby foot1 run schedule function mg:foot/build_start 24s'])
C.forceload([f'forceload add {FB.FORCELOAD}'])
C.patch('desinstaller', 'team remove mg_party', ['team remove mg_ftr', 'team remove mg_ftb'])
C.patch('desinstaller', 'data remove storage mg:pvpc s', [
    'schedule clear mg:foot/build_start', 'schedule clear mg:foot/build_go', f'kill {FB.BALLS}', 'kill @e[type=minecraft:text_display,tag=mg.ftd]',
    'tag @a remove mg.ftr', 'tag @a remove mg.ftb', 'tag @a remove mg.ftin', 'data remove storage mg:lobby foot1'])
# core/tick : boucle du terrain (désactivable), entretien toutes les 2 s (le chunk du centre chargé), reconstruction si le bloc témoin manque
# (les 4 coins de la zone doivent être chargés : le bloc témoin est posé en dernier, mais une zone à moitié chargée ne se construit pas)
sx, sy, sz = FB.SENT
corners = ' '.join(f'if loaded {x} 46 {z}' for x, z in ((-17, -41), (21, -41), (-17, -14), (21, -14)))
TICK = [f'execute if score $setup mg.st matches 1 unless score $ftoff mg.st matches 1 if entity @a[{FB.FOOT_ZONE}] run function mg:foot/tick',
        'execute if score $setup mg.st matches 1 if score $lan mg.t matches 30 if loaded 2 48 -31 run function mg:foot/second',
        f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded {sx} {sy} {sz} {corners} unless block {sx} {sy} {sz} minecraft:lodestone run function mg:foot/build']
TICK_OLD = f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded {sx} {sy} {sz} unless block {sx} {sy} {sz} minecraft:lodestone run function mg:foot/build'
C.drop_lines('core/tick', TICK + [TICK_OLD])      # core/tick n'est que patché (jamais réécrit) : on retire d'abord les lignes du foot (dont l'ancienne forme du test)
C.patch('core/tick', 'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded 13 53 5 unless block 13 53 5 minecraft:lodestone run function mg:pvpc/build', TICK)
C.patch('core/reset_player', 'tag @s remove mg.play', ['function mg:foot/cleanup'], where='before')
C.patch('core/request', 'execute as @a[tag=mg.play,tag=mg.elyf] run function mg:elytra/free_stop', ['execute as @a[tag=mg.play] run function mg:foot/cleanup'],
        where='before')
# reconstruction du spawn : le terrain est refait juste après (avant les forceload remove de lobby/build_end ; la zone est dans -80..80, donc chargée)
C.patch('lobby/build_end', 'function mg:parkour/build', ['function mg:foot/build'])
FA.wire()
print('Terrain de foot OK')
