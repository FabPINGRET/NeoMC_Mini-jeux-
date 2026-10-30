"""Balises lumineuses du spawn (faisceaux de balise) : python tools/lobby/gen_beacons.py .

- blanche au centre des 3 socles d'élytra (petit parcours, grand parcours, élytres libres) ;
Pyramide de fer 3×3 enterrée sous chaque balise (y 62), colonne dégagée au-dessus (feuillages).
Construites une fois (drapeau mg:lobby beacon1) et à chaque mg:setup.
"""
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
sys.path.insert(0, os.path.join(R, 'tools/elytra'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
import mcfn
_fn = mcfn.Fn(F)
w, patch = _fn.write, _fn.patch

PADS = [(16, -9), (32, -15), (16, -21)]                  # socles d'élytra (tools/elytra/gen_elytra.py)
ELY = (round(sum(p[0] for p in PADS) / 3), 63, round(sum(p[1] for p in PADS) / 3))   # (21, 63, -15)
BEACONS = [(ELY, None, 'blanche, élytra')]
# ancienne balise rouge de la montagne russe (-48, 63, 41) : supprimée une fois par mg:lobby/coaster_beacon_off
OLD_COASTER = (-48, 63, 41)


L = ['# Balises du spawn (générées par tools/lobby/gen_beacons.py)']
for (x, y, z), glass, lab in BEACONS:
    L += [f'# {lab}',
          f'fill {x - 1} {y - 1} {z - 1} {x + 1} {y - 1} {z + 1} minecraft:iron_block',
          f'setblock {x} {y} {z} minecraft:beacon',
          f'fill {x} {y + 1} {z} {x} 319 {z} minecraft:air']
    if glass:
        L.append(f'setblock {x} {y + 1} {z} minecraft:{glass}')
L.append('data modify storage mg:lobby beacon1 set value 1b')
w('lobby/beacons', L)

patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby food1 run schedule function mg:lobby/food_build 12s',
      ['execute if score $setup mg.st matches 1 unless data storage mg:lobby beacon1 run schedule function mg:lobby/beacons 18s'])
patch('core/setup_build', 'schedule function mg:sky/build 40s', ['schedule function mg:lobby/beacons 55s'])
patch('desinstaller', 'schedule clear mg:lobby/food_build', ['schedule clear mg:lobby/beacons', 'data remove storage mg:lobby beacon1'])
w('lobby/coaster_beacon_off', ['# Ancienne balise de la montagne russe (supprimée) : une seule fois, drapeau mg:lobby coasterbeacon',
                              f'setblock {OLD_COASTER[0]} {OLD_COASTER[1]} {OLD_COASTER[2]} minecraft:air',
                              f'setblock {OLD_COASTER[0]} {OLD_COASTER[1] + 1} {OLD_COASTER[2]} minecraft:air',
                              'kill @e[type=minecraft:text_display,tag=mg.csd]',
                              'kill @e[type=minecraft:minecart,tag=mg.cst]',
                              'data modify storage mg:lobby coasterbeacon set value 1b'])
patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby beacon1 run schedule function mg:lobby/beacons 18s',
      ['execute unless data storage mg:lobby coasterbeacon run function mg:lobby/coaster_beacon_off'])
print('Balises OK :', ELY)
