"""🎣 Pêche à l'étang du spawn : python tools/lobby/gen_fish.py .
(depuis la racine du dépôt ; idempotent ; APRÈS gen_lobby.py, gen_pvpcave.py, gen_events.py et gen_foot.py, AVANT gen_themes.py)

Un socle de bois sur la berge de l'étang (POND de gen_lobby.py) donne une canne marquée au clic droit. Les prises sont virtuelles (le spawn est en
aventure, rien ne reste dans l'inventaire) : poisson commun ou rare, poisson doré rare, déchet drôle, avec une taille en cm ; le record de taille
de chacun passe par la plaque « 🎣 Plus belle prise » du Hall (tools/hall/gen_hall.py : plaque mg.h_fish, objectif mg.lfb). La pêche reste ouverte
toute l'année : gen_themes.py laisse l'eau de l'étang liquide sous le thème Noël.
- fish_rod.py : socle, canne, garde (keep), entretien (second, after, build), advancements mg:lobby_fish_take et mg:lobby_fish.
- fish_game.py : table des prises (CATCHES), tirage, effets, record.  fish_admin.py : mg.opt 86 (on/off) et 87 (compteurs), boutons du menu des événements.
Ce fichier : contrôle du site, puis câblage (core/tick, core/request, core/load, core/opt, desinstaller).
Objectifs : mg.lfb (record en cm), mg.lfn (compteurs), mg.lfu (stat vanilla used:fishing_rod) ; $lfoff dans mg.st (coupé).
Le bloc du socle est reposé par core/tick s'il manque (reconstruction du spawn comprise) ; les fonctions sont sous lobby/fish/ (PAS sous lobby/theme/ :
theme_world.load classe ses setblock en zone modifiée ailleurs, les décors saisonniers n'y touchent pas).
lobby/fish/ est effacé puis réécrit à chaque passage (remis en place si un contrôle du site échoue) ; gen_events.py réécrit lobby_events.json et
menu_chat : relancer ensuite gen_foot.py, gen_fish.py PUIS gen_sit.py. L'objet 🎉 Emotes et la canne partagent la liste BUSY (sit_item.py).
La purge (lobby/fish/purge) relit les conteneurs des constructions du spawn et du Hall (SI.containers) : relancer gen_fish.py après gen_lobby.py
et gen_hall.py, comme gen_sit.py.
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C
import fish_admin as FA
import fish_game as FG
import fish_rod as FR
import sit_bench as SB
import sit_item as SI
import theme_world as TW

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')


def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1] and a[2] <= b[3] and b[2] <= a[3] and a[4] <= b[5] and b[4] <= a[5]


def check_site():
    """Le générateur s'arrête avant d'écrire quoi que ce soit si le site n'est pas celui qu'on croit (sinon : une case voisine de la berge)."""
    x, y, z = FR.SOCLE
    box = (x, x, y - 1, y + 2, z, z)                             # sol (y 63), bloc du socle (y 64) et sa colonne dégagée (y 65..66)
    # TW.RESERVED est vide ici (seul theme_npcs.prepare le remplit, plus tard) : le test ne porte en pratique que sur PAD_BOXES
    for d in TW.DYN:
        assert not overlap(box, d), f'socle {box} touche une zone modifiée ailleurs (DYN) : {d}'
    for r in TW.RESERVED + TW.PAD_BOXES:
        assert not overlap(box, r), f'socle {box} touche une zone réservée : {r}'
    assert TW.solid(x, y - 1, z) and (x, y - 1, z) in TW.W, f'socle : pas de sol plein en {(x, y - 1, z)} ({TW.W.get((x, y - 1, z))})'
    for yy in (y, y + 1, y + 2):
        assert TW.opening((x, yy, z)), f'socle : décor du spawn en {(x, yy, z)} ({TW.W.get((x, yy, z))})'
    px, py, pz = (float(v) for v in FR.POND_C.split())
    assert ((x + 0.5 - px) ** 2 + (z + 0.5 - pz) ** 2) ** 0.5 < FR.FISH_R - 2, 'socle trop loin du centre de l\'étang (rayon de garde)'


# ---------------------------------------------------------------- lobby/fish/ mis de côté pendant les contrôles et l'écriture (restauré en cas d'échec)
fish_dir = os.path.join(C.F, 'lobby', 'fish')
bak = tempfile.mkdtemp(prefix='fish_bak_')
if os.path.isdir(fish_dir):
    shutil.move(fish_dir, os.path.join(bak, 'fish'))
try:
    TW.load(C.F)                         # sans lobby/fish/ : le modèle du spawn ne connaît pas encore notre socle
    check_site()
    orig = TW.W.get(FR.SOCLE, 'minecraft:air')       # bloc d'origine du spawn à cette place (remis par la coupure admin)
    FR.write(SI.containers())
    FG.write()
    FA.write(orig)
except BaseException:
    shutil.rmtree(fish_dir, ignore_errors=True)
    if os.path.isdir(os.path.join(bak, 'fish')):
        shutil.move(os.path.join(bak, 'fish'), fish_dir)
    raise
finally:
    shutil.rmtree(bak, ignore_errors=True)


def foot_build_line():
    """La ligne foot/build de core/tick (posée par gen_foot.py ; sa forme dépend de la zone du foot) : ancre des lignes de la pêche."""
    with open(os.path.join(C.F, 'core', 'tick.mcfunction'), encoding='utf-8') as f:
        found = [l for l in f.read().split('\n') if l.endswith(' run function mg:foot/build')]
    if len(found) != 1:
        raise SystemExit(f'core/tick : ligne foot/build trouvée {len(found)} fois (gen_foot.py doit passer avant gen_fish.py)')
    return found[0]


# ---------------------------------------------------------------- câblage (une ligne par patch)
C.objectives([('mg.lfb', 'dummy'), ('mg.lfn', 'dummy'), ('mg.lfu', 'minecraft.used:minecraft.fishing_rod')])
# core/load : marqueurs d'une prise interrompue par un rechargement
C.patch('core/load', 'scoreboard objectives add mg.st dummy', ['kill @e[type=minecraft:marker,tag=mg.lfm]', 'tag @a remove mg.lfc'])
DESINST = ['kill @e[tag=mg.lfs]', 'kill @e[type=minecraft:marker,tag=mg.lfm]', f'setblock {FR.POS} {orig}', f'clear @a {FR.PRED}', FR.DROPPED,
           'function mg:lobby/fish/purge', 'advancement revoke @a only mg:lobby_fish', 'advancement revoke @a only mg:lobby_fish_take',
           'tag @a remove mg.lfc']
C.drop_lines('desinstaller', DESINST)    # patché (jamais réécrit) : on retire d'abord nos lignes (déplacement d'ancre), puis on les repose
C.patch('desinstaller', SB.HEADER_NOTE, DESINST)
C.patch('core/request', 'execute as @a[tag=mg.play,tag=mg.elyf] run function mg:elytra/free_stop', [f'clear @a[tag=mg.play] {FR.PRED}'], where='before')
# core/tick, juste après la ligne foot/build : après une prise, entretien toutes les 2 s (chunk du socle chargé), reconstruction si le bloc du socle manque
TICK = ['execute if entity @a[tag=mg.lfc] run function mg:lobby/fish/after',
        'execute if score $lan mg.t matches 30 if entity @e[type=minecraft:marker,tag=mg.lfm] run function mg:lobby/fish/after',      # joueur déconnecté entre la prise et ce tick (filet : toutes les 2 s)
        f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 30 if loaded {FR.POS} run function mg:lobby/fish/second',
        f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless score $lfoff mg.st matches 1 if loaded {FR.POS} '
        f'unless block {FR.POS} {FR.LOG} run function mg:lobby/fish/build']
C.drop_lines('core/tick', TICK + ['execute if entity @e[type=minecraft:marker,tag=mg.lfm] run function mg:lobby/fish/after'])   # core/tick n'est que patché : on retire nos lignes (anciennes versions comprises), puis on les repose
C.patch('core/tick', foot_build_line(), TICK)
FA.wire()
print('Pêche à l\'étang OK :', len(FG.CATCHES), 'prises')
