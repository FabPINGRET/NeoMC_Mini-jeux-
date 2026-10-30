"""Hub des portails (spawn nord, à la place de l'ancien portail des plots) : python tools/lobby/gen_hub.py .

Huit petits portails, chacun dans un plan x = X (ouverture de deux blocs en z), sur deux rangées :
- rangée nord (z -52) : Neo GTA (-9), Terra Nova (-3), Ombrelune (3), arène PvP (9) ;
- rangée sud (z -45) : Survie (-9), Filon (-3), Scourge of the Floaty Isles (3, verrouillé), terrain de foot (9).
Neo GTA, Terra Nova et Ombrelune gardent leur logique d'entrée (lobby_tick de leur générateur, qui lit PX / PZ) :
leur portail_build n'est plus qu'un appel à mg:hub/build. Les cinq autres entrent par mg:hub/tick.
Le passage nord-sud reste ouvert en z -49 (entre les deux rangées) et au centre (x -2..2).

Ordre : après gen_lobby.py, gen_pvpcave.py, gen_ombrelune.py, gen_foot.py, gen_gta.py et gen_terranova.py.
Le hub reprend les anciens emplacements (GTA, Terra Nova, Ombrelune) une seule fois (mg:hub oldclean).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
sys.path.insert(0, os.path.join(HERE, '..', 'lib'))
sys.path.insert(0, HERE)
import mcfn  # noqa: E402
import theme_world as TW  # noqa: E402

TW.load(F)
_fn = mcfn.Fn(F)
w, patch = _fn.write, _fn.patch

TR = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[%sf,%sf,%sf],scale:[%sf,%sf,%sf]}'
BOX = (-10, 63, -56, 10, 82, -42)                 # zone du hub (x1 y1 z1 x2 y2 z2)
WITNESS = (0, 63, -49)                            # bloc témoin du hub (au centre du passage nord-sud)
WITNESS_BLOCK = 'minecraft:mossy_stone_bricks'
OLD_SITES = [(5, 13, -23, -15), (-16, -5, -23, -15), (-18, -5, -33, -25)]   # anciens portails GTA, Terra Nova, Ombrelune (x1 x2 z1 z2)
CLEAN_FLAG = 'mg:hub oldclean'

# id, texte, couleur, garniture, bloc du sol, x, z, witness (portails gérés par leur générateur) ; entry = None (géré par son générateur) ou nom de l'entrée
SLOTS = [
    dict(id='gta', title='🚓 NEO GTA', sub='Monde GTA libre : armes, voitures, hélicos, police', col='gold', trim='gold_block', pad='yellow_concrete', x=-9, z=-52, witness='minecraft:chiseled_polished_blackstone', entry=None),
    dict(id='terra', title='🦖 TERRA NOVA', sub='Colonie préhistorique : missions, jungle, dinosaures', col='green', trim='moss_block', pad='mossy_stone_bricks', x=-3, z=-52, witness='minecraft:chiseled_tuff_bricks', entry=None),
    dict(id='ombre', title='🌙 OMBRELUNE', sub='RPG médiéval-fantastique : 8 régions, dragons, donjons', col='light_purple', trim='amethyst_block', pad='deepslate_tiles', x=3, z=-52, witness='minecraft:chiseled_polished_blackstone', entry=None),
    dict(id='pvp', title='⚔ ARÈNE PVP', sub='Trou souterrain : classes, points, mini-lobby', col='red', trim='red_nether_bricks', pad='blackstone', x=9, z=-52, witness=None, entry='pvp'),
    dict(id='survie', title='🌲 SURVIE', sub='Monde libre : inventaire gardé, structures', col='dark_green', trim='oak_log', pad='grass_block', x=-9, z=-45, witness=None, entry='survie'),
    dict(id='filon', title='⛏ FILON', sub='Mode long par saisons : mine, comptoir, classement', col='yellow', trim='iron_block', pad='sandstone', x=-3, z=-45, witness=None, entry='filon'),
    dict(id='floaty', title='🏝 SCOURGE OF THE FLOATY ISLES', sub='Carte d aventure partagée', col='aqua', trim='prismarine_bricks', pad='prismarine', x=3, z=-45, witness=None, entry='floaty'),
    dict(id='foot', title='⚽ TERRAIN DE FOOT', sub='Vestiaire souterrain, équipes, buts', col='dark_green', trim='green_terracotta', pad='green_terracotta', x=9, z=-45, witness=None, entry='foot'),
]
ENTER_TAGS = 'tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure'


def snbt_text(d):
    return "'" + json.dumps(d, ensure_ascii=False) + "'"


def box_at(s):
    """Boîte de passage (un joueur dans l'ouverture, z = Z - 1 ou Z) : mêmes bornes que les autres portails."""
    return f'x={s["x"]},y=64,z={s["z"] - 1},dx=0,dy=2,dz=2'


def portal_lines(s):
    x, z, trim = s['x'], s['z'], s['trim']
    L = [f'# portail {s["id"]} : plan x={x}, ouverture z {z - 1}..{z}',
         f'fill {x} 64 {z - 3} {x} 70 {z + 2} minecraft:polished_deepslate',           # cadre
         f'fill {x} 64 {z - 1} {x} 67 {z} minecraft:air',                              # ouverture
         f'fill {x} 64 {z - 3} {x} 70 {z - 3} minecraft:{trim}',                       # montants
         f'fill {x} 64 {z + 2} {x} 70 {z + 2} minecraft:{trim}',
         f'fill {x} 71 {z - 3} {x} 71 {z + 2} minecraft:{trim}',                       # linteau
         f'fill {x - 1} 63 {z - 2} {x + 1} 63 {z + 1} minecraft:{s["pad"]}',           # sol devant le portail
         f'summon minecraft:text_display {x + 0.5} 73.2 {z - 0.5} {{Tags:["mg.hubp"],billboard:"center",background:-1442840576,'
         f'text:{snbt_text({"text": s["title"], "color": s["col"], "bold": True})},{TR % (0, 0, 0, 2.2, 2.2, 2.2)}}}',
         f'summon minecraft:text_display {x + 0.5} 72.5 {z - 0.5} {{Tags:["mg.hubp"],billboard:"center",background:0,'
         f'text:{snbt_text({"text": s["sub"], "color": "gray"})},{TR % (0, 0, 0, 0.8, 0.8, 0.8)}}}']
    L.append(f'summon minecraft:text_display {x + 0.5} 66.2 {z - 0.5} {{Tags:["mg.hubp"],billboard:"center",background:0,'
             f'text:{snbt_text({"text": "▶ entre dans le portail", "color": "yellow"})},{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}')
    if s['witness']:
        L.append(f'setblock {x} 63 {z} {s["witness"]}')
    return L


# ---------------------------------------------------------------- construction (une fois, puis à chaque témoin manquant)
X1, Y1, Z1, X2, Y2, Z2 = BOX
BUILD = ['# Hub des portails : huit petits portails au spawn nord (ex-portail des plots), reconstruit par mg:hub/tick si son témoin disparaît',
         f'kill @e[tag=mg.hubp]', 'kill @e[tag=mg.gtap]', 'kill @e[tag=mg.tvport]', 'kill @e[tag=mg.olport]',
         f'kill @e[type=minecraft:text_display,x={X1},y={Y1},z={Z1},dx={X2 - X1},dy={Y2 - Y1},dz={Z2 - Z1}]',
         f'fill {X1} 64 {Z1} {X2} {Y2} {Z2} minecraft:air',
         f'fill {X1} 63 {Z1} {X2} 63 {Z2} minecraft:smooth_stone',
         f'setblock {WITNESS[0]} {WITNESS[1]} {WITNESS[2]} {WITNESS_BLOCK}',
         'execute unless data storage mg:hub floaty run data modify storage mg:hub floaty set value 0b',
         f'execute unless data storage mg:hub oldclean run function mg:hub/old_clean']
for s in SLOTS:
    BUILD += portal_lines(s)
w('hub/build', BUILD)

OLD = ['# Anciens portails (GTA, Terra Nova, Ombrelune) : vidés une seule fois, sol rendu au décor du spawn (mg:hub oldclean)']
for (x1, x2, z1, z2) in OLD_SITES:
    OLD.append(f'fill {x1} 64 {z1} {x2} 80 {z2} minecraft:air')
    OLD += TW.restore_lines(TW.W, (x1, x2, 63, 63, z1, z2))
# ancien portail d'Ombrelune (avenue est, 40 -9) : nettoyé une seule fois (son drapeau mg:lobby olsite), comme avant
OLD += ['execute unless data storage mg:lobby olsite if block 40 63 -9 minecraft:chiseled_polished_blackstone run function mg:ombre/old_site']
OLD += ['data modify storage mg:hub oldclean set value 1b']
w('hub/old_clean', OLD)

# ---------------------------------------------------------------- entrées (portails sans logique propre)
ENTER = {
    'survie': ['# @s entre au portail de Survie (hub)', 'function mg:survie/enter'],
    'filon': ['# @s entre au portail du Filon (hub) : même menu que le bouton (mg.sv 9)', 'function mg:filon/menu_go'],
    'floaty': ['# @s entre au portail de Scourge of the Floaty Isles (hub) : verrouillé tant que le terrain n\'est pas installé',
               'execute unless data storage mg:hub {floaty:1b} run return run title @s actionbar {"text":"🔒 Scourge of the Floaty Isles : bientôt disponible","color":"aqua"}',
               'function mg:floaty/menu_go'],
    'foot': ['# @s entre au portail du terrain de foot (hub) : posé sur le tapis d\'entrée (x -7..-5, z -40..-38)',
             'tp @s -6.5 64 -38.5 90 0'],
    'pvp': ['# @s entre au portail de l\'arène PvP (hub) : au-dessus du trou, il y tombe',
            'tp @s 13.5 66 12.5 0 0'],
}
for k, lines in ENTER.items():
    w(f'hub/enter_{k}', lines)

# ---------------------------------------------------------------- tick (core/tick, monde des mini-jeux)
TICK = ['# Chaque tick (core/tick) : témoin du hub, entrées des cinq portails du hub, particules des huit portails',
        f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block {WITNESS[0]} {WITNESS[1]} {WITNESS[2]} {WITNESS_BLOCK} run function mg:hub/build']
for s in SLOTS:
    if s['entry']:
        TICK.append(f'execute if score $setup mg.st matches 1 in minecraft:overworld as @a[{ENTER_TAGS},{box_at(s)}] run function mg:hub/enter_{s["entry"]}')
for s in SLOTS:
    x, z = s['x'], s['z']
    TICK.append(f'particle minecraft:reverse_portal {x + 0.5} 66 {z - 0.5} 0.05 1.1 0.9 0 1')
w('hub/tick', TICK)

patch('core/tick', 'function mg:floaty/lobby_tick', ['function mg:hub/tick'])
patch('desinstaller', 'schedule clear mg:elytra/build',
      ['kill @e[tag=mg.hubp]', 'data remove storage mg:hub oldclean', 'data remove storage mg:hub floaty'])
print('Hub OK :', ', '.join(f'{s["id"]} ({s["x"]},{s["z"]})' for s in SLOTS))
