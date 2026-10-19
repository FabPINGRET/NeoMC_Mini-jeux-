"""⚽ Terrain de foot souterrain du spawn : python tools/lobby/gen_foot.py .
(depuis la racine du dépôt ; idempotent ; APRÈS gen_lobby.py, gen_pvpcave.py, gen_events.py et gen_ombrelune.py, AVANT gen_themes.py)

Un tapis téléporteur (x -7..-5, z -40..-38, bord de l'avenue nord, côté ouest ; ligne de core/tick -> foot/pad -> foot/go) mène à un vestiaire creusé
dans la roche, puis au terrain (31×19, sol vert, deux buts) en dessous. Une balle (sulfur_cube au corps test_block, dessinée en ballon par le
resource pack, archétype mg:football) au centre ; deux équipes au choix sur les socles du vestiaire. Un but compte pour l'équipe ADVERSE du
but, quel que soit le tireur. Aucune équipe sur le terrain : buts libres, comptés par joueur (dernier toucheur), remis à zéro à la sortie.
Pas de PvP sur le terrain. L'ancien puits (x -2..1, z -18..-15) est rebouché par foot/build avec les blocs du spawn (theme_world.W).
- foot_build.py : géométrie, constantes de sélecteur (FOOT_ZONE, aussi lue par gen_sit.py), foot/build, labels, tapis, build_start / build_go.
- foot_game.py : foot/tick, foot/second, balle, buts, score, archétype.  foot_teams.py : équipes mg_ftr / mg_ftb, socles, cleanup.
- foot_admin.py : mg.opt 84 (on/off) et 85 (compteurs), boutons du menu des événements.
Tout est reconstruit si le bloc témoin (pierre de magnétite en (2, 46, -30)) disparaît ; forceload permanent de la zone (core/forceloads).
Le bloc témoin est posé en dernier par foot/build, et core/tick ne lance la reconstruction que si les 4 coins de la zone sont chargés.
Reconstruction du spawn (lobby/build, ex. changement de version) : elle remplit de nouveau la roche (y 46..58) et le sol carré de la place,
donc efface le tapis et le terrain. Pour le refaire dans la foulée, foot/build est appelé à la fin de lobby/build_end (patch plus bas).
Limite : entre les étapes build_5 et build_8 le bloc témoin peut manquer (roche remplie avant le sol) : la reconstruction de core/tick,
si elle part pendant ces étapes, est alors écrasée par la suite de lobby/build, puis refaite par lobby/build_end. Ne pas lancer foot/build
à la main pendant lobby/build.
Les fonctions de construction sont sous foot/ (PAS sous lobby/theme/) : theme_world.load les classe DYN, les décors saisonniers n'y touchent pas.
foot/ est effacé puis réécrit à chaque passage (comme gen_elyrace.py ; remis en place si un contrôle du site échoue) ; gen_events.py réécrit
lobby_events.json et menu_chat : relancer ensuite gen_foot.py PUIS gen_sit.py (gen_rating régénère rate/d/lobby_events).
Objectifs : mg.ft (scores, et buts libres de chaque joueur), mg.ftn (compteurs) ; équipes mg_ftr, mg_ftb ;
tags mg.ftr, mg.ftb, mg.ftin, mg.ftlt (dernier toucheur), mg.ball, mg.ftd.
Écrit aussi data/mg/sulfur_cube_archetype/football.json (archétype de la balle ; lu au démarrage du serveur seulement).
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
    carpet = (FB.PAD_X[0], FB.PAD_X[1], 63, 66, FB.PAD_Z[0], FB.PAD_Z[1])     # tapis d'entrée et sa colonne dégagée (y 64..66)
    # (nom, boîte) : tout ce qui est en surface (tapis, but blanc, haie ouverte) est contrôlé plus bas, pas comme de la roche
    for name, box in (('terrain', FB.SHELL), ('vestiaire', FB.LOCKER), ('ancien puits', FB.OLD_SHAFT), ('tapis', carpet),
                      ('but blanc', FB.GOAL), ('haie ouverte', FB.GATE)):
        for d in TW.DYN:
            assert not overlap(box, d), f'{name} {box} touche une zone modifiée ailleurs (DYN) : {d}'
        for r in TW.RESERVED + TW.PAD_BOXES:
            assert not overlap(box, r), f'{name} {box} touche une zone réservée : {r}'
        if box in (carpet, FB.GOAL, FB.GATE):
            continue                                             # en surface : contrôlé plus bas
        for x in range(box[0], box[1] + 1):
            for y in range(box[2], min(box[3], 62) + 1):
                for z in range(box[4], box[5] + 1):
                    # la roche de l'île est dans W (pierre de y 46 à 58, terre de 59 à 62) : tout ce qu'on creuse y est déjà plein (rien dans le vide)
                    assert TW.solid(x, y, z) and (x, y, z) in TW.W, f'{name} : pas de roche en {(x, y, z)} ({TW.W.get((x, y, z))})'
    assert all(abs(c) < TW.LIM for c in (FB.SHELL[0], FB.SHELL[1], FB.SHELL[4], FB.SHELL[5]))
    x1, x2, _, _, z1, z2 = FB.OLD_SHAFT
    for x in range(x1, x2 + 1):                                  # sol du spawn sur l'ancien puits (y 63) : foot/build le rebouche avec W
        for z in range(z1, z2 + 1):
            assert (x, 63, z) in TW.W and TW.solid(x, 63, z), f'pas de sol du spawn en {(x, 63, z)}'
    for x in (x1, x2):                                           # piquets (y 64 et 65) : rien d'autre du spawn à leur place
        for z in (z1, z2):
            assert not any((x, y, z) in TW.W for y in (64, 65)), f'décor du spawn à la place d\'un piquet ({x}, {z})'
    # tapis : sol d'herbe ou de terre (le terracotta le remplace), colonne y 64..66 libre (plantes tolérées : foot/build les vide)
    for x in range(FB.PAD_X[0], FB.PAD_X[1] + 1):
        for z in range(FB.PAD_Z[0], FB.PAD_Z[1] + 1):
            assert TW.bid(TW.W.get((x, 63, z))) in TW.GROUND, f'tapis : pas de sol d\'herbe en {(x, 63, z)} ({TW.W.get((x, 63, z))})'
            for y in (64, 65, 66):
                assert TW.opening((x, y, z)), f'tapis : décor du spawn en {(x, y, z)} ({TW.W.get((x, y, z))})'
    # ancien tapis : sol d'herbe ou de terre d'origine (foot/build le restitue depuis W : un trou dans W laisserait de l'air à sa place)
    ox1, ox2, _, _, oz1, oz2 = FB.OLD_PAD
    for x in range(ox1, ox2 + 1):
        for z in range(oz1, oz2 + 1):
            assert TW.bid(TW.W.get((x, 63, z))) in TW.GROUND, f'ancien tapis : pas de sol d\'herbe en {(x, 63, z)} ({TW.W.get((x, 63, z))})'
    # but blanc : que de l'air, des plantes ou du bambou (foot/build vide la boîte puis pose les poteaux et la barre)
    gx1, gx2, gy1, gy2, gz1, gz2 = FB.GOAL
    for x in range(gx1, gx2 + 1):
        for y in range(gy1, gy2 + 1):
            for z in range(gz1, gz2 + 1):
                b = TW.bid(TW.W.get((x, y, z)))
                assert b == 'minecraft:air' or b in TW.PLANTS or b == 'minecraft:bamboo', f'but blanc : décor du spawn en {(x, y, z)} ({TW.W.get((x, y, z))})'
    # haie ouverte : seulement de la haie d'azalée en y 64 (y 65..66 vides) ; sol de y 63 : herbe ou terre (foot/build la remplace par des briques)
    # ou le purpur de l'anneau de la place des plots (laissé en place)
    hx1, hx2, hy1, hy2, hz1, hz2 = FB.GATE
    for x in range(hx1, hx2 + 1):
        for z in range(hz1, hz2 + 1):
            assert TW.bid(TW.W.get((x, hy1, z))) in TW.GROUND | {'minecraft:purpur_block'}, f'haie : sol inattendu en {(x, hy1, z)} ({TW.W.get((x, hy1, z))})'
            assert TW.bid(TW.W.get((x, hy1 + 1, z))).endswith('azalea_leaves'), f'haie : pas de haie d\'azalée en {(x, hy1 + 1, z)} ({TW.W.get((x, hy1 + 1, z))})'
            for y in range(hy1 + 2, hy2 + 1):
                assert (x, y, z) not in TW.W, f'haie : décor du spawn en {(x, y, z)} ({TW.W.get((x, y, z))})'
    # point d'arrivée du socle or (RETURN, sur l'avenue) : sol plein, deux cases libres au-dessus
    rx, ry, rz = int(FB.RETURN[0] // 1), int(FB.RETURN[1]), int(FB.RETURN[2] // 1)
    assert TW.solid(rx, ry - 1, rz) and all(TW.opening((rx, y, rz)) for y in (ry, ry + 1)), f'arrivée du socle or ({rx}, {ry - 1}..{ry + 1}, {rz}) obstruée'


# ---------------------------------------------------------------- foot/ mis de côté pendant les contrôles et l'écriture (restauré en cas d'échec)
foot_dir = os.path.join(C.F, 'foot')
bak = tempfile.mkdtemp(prefix='foot_bak_')
if os.path.isdir(foot_dir):
    shutil.move(foot_dir, os.path.join(bak, 'foot'))
try:
    TW.load(C.F)                         # sans foot/ : le modèle du spawn ne connaît pas encore notre construction
    check_site()
    FB.write(TW.W)
    FG.write()
    FG.write_archetype()
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
# drapeau foot2 (tapis déplacé sur l'avenue nord) : sans lui, un serveur qui a déjà foot1 ne reconstruirait jamais le tapis ; foot1 reste posé, sans effet
C.drop_lines('core/load', ['execute if score $setup mg.st matches 1 unless data storage mg:lobby foot1 run schedule function mg:foot/build_start 24s'])
C.patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby pvpc2 run schedule function mg:pvpc/build_start 22s', [
    'execute if score $setup mg.st matches 1 unless data storage mg:lobby foot2 run schedule function mg:foot/build_start 24s'])
C.forceload([f'forceload add {FB.FORCELOAD}'])
C.patch('desinstaller', 'team remove mg_party', ['team remove mg_ftr', 'team remove mg_ftb'])
C.patch('desinstaller', 'data remove storage mg:pvpc s', [
    'schedule clear mg:foot/build_start', 'schedule clear mg:foot/build_go', f'kill {FB.BALLS}', 'kill @e[type=minecraft:text_display,tag=mg.ftd]',
    'tag @a remove mg.ftr', 'tag @a remove mg.ftb', 'tag @a remove mg.ftin', 'data remove storage mg:lobby foot1'])
C.patch('desinstaller', 'tag @a remove mg.ftin', ['tag @a remove mg.ftlt'])      # patch séparé : une liste ci-dessus recopiée en entier doublerait les lignes
C.patch('desinstaller', 'data remove storage mg:lobby foot1', ['data remove storage mg:lobby foot2'])    # idem : le drapeau du tapis déplacé
# core/tick : tapis d'entrée, boucle du terrain (désactivable), entretien toutes les 2 s (le chunk du centre chargé), reconstruction si le bloc témoin manque
# (les 4 coins de la zone doivent être chargés : le bloc témoin est posé en dernier, mais une zone à moitié chargée ne se construit pas)
corners = ' '.join(f'if loaded {x} 46 {z}' for x, z in ((-17, -41), (21, -41), (-17, -14), (21, -14)))
OLD_ZONE = 'x=-17,y=46,z=-41,dx=38,dy=17,dz=27'      # FOOT_ZONE d'avant le tapis (y 46..63) ; OLD_SENT : l'ancien bloc témoin
OLD_SENT = (2, 46, -31)


def tick_lines(zone, sent):
    """Les trois lignes foot/ de core/tick après le tapis, pour une zone et un bloc témoin donnés (les actuels, ou les anciens à retirer)."""
    sx, sy, sz = sent
    return [f'execute if score $setup mg.st matches 1 unless score $ftoff mg.st matches 1 if entity @a[{zone}] run function mg:foot/tick',
            'execute if score $setup mg.st matches 1 if score $lan mg.t matches 30 if loaded 2 48 -31 run function mg:foot/second',
            f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded {sx} {sy} {sz} {corners} unless block {sx} {sy} {sz} minecraft:lodestone run function mg:foot/build']


# tapis allumé = bloc d'or au centre (FB.PAD_C ; foot/entry_close le remplace par du vert) : foot/pad fait les particules et l'envoi au terrain
TICK = [f'execute if score $setup mg.st matches 1 unless score $ftoff mg.st matches 1 if block {FB.PAD_C[0]} 63 {FB.PAD_C[1]} minecraft:gold_block '
        'run function mg:foot/pad'] + tick_lines(FB.FOOT_ZONE, FB.SENT)
OLD_SX, OLD_SY, OLD_SZ = OLD_SENT
# ligne du tapis d'avant (x -19..-17, appelait foot/go directement), recopiée telle quelle de core/tick
OLD_ENTRY = ('execute if score $setup mg.st matches 1 unless score $ftoff mg.st matches 1 if block -18 63 -18 minecraft:gold_block '
             'as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,'
             'gamemode=adventure,x=-18.7,y=63,z=-18.7,dx=1.4,dy=2.5,dz=1.4] run function mg:foot/go')
# toutes les anciennes formes à retirer : zone d'avant (foot/tick), bloc témoin d'avant (foot/build), test d'avant sans les coins, tapis d'avant
OLD = tick_lines(OLD_ZONE, OLD_SENT) + [
    f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded {OLD_SX} {OLD_SY} {OLD_SZ} unless block {OLD_SX} {OLD_SY} {OLD_SZ} minecraft:lodestone run function mg:foot/build',
    OLD_ENTRY]
C.drop_lines('core/tick', TICK + OLD)      # core/tick n'est que patché (jamais réécrit) : on retire d'abord les lignes du foot (dont les anciennes formes)
C.patch('core/tick', 'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded 13 53 5 unless block 13 53 5 minecraft:lodestone run function mg:pvpc/build', TICK)
C.patch('core/reset_player', 'tag @s remove mg.play', ['function mg:foot/cleanup'], where='before')
C.patch('core/request', 'execute as @a[tag=mg.play,tag=mg.elyf] run function mg:elytra/free_stop', ['execute as @a[tag=mg.play] run function mg:foot/cleanup'],
        where='before')
# reconstruction du spawn : le terrain est refait juste après (avant les forceload remove de lobby/build_end ; la zone est dans -80..80, donc chargée)
C.patch('lobby/build_end', 'function mg:parkour/build', ['function mg:foot/build'])
FA.wire()
print('Terrain de foot OK')
