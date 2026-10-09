"""Balises lumineuses du spawn (faisceaux de balise) : python tools/lobby/gen_beacons.py .

- blanche au centre des 3 socles d'élytra (petit parcours, grand parcours, élytres libres) ;
- rouge à côté du guichet de la montagne russe (verre teinté rouge sur la balise).
Pyramide de fer 3×3 enterrée sous chaque balise (y 62), colonne dégagée au-dessus (feuillages).
Construites une fois (drapeau mg:lobby beacon1) et à chaque mg:setup.
"""
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
sys.path.insert(0, os.path.join(R, 'tools/elytra'))

PADS = [(16, -9), (32, -15), (16, -21)]                  # socles d'élytra (tools/elytra/gen_elytra.py)
ELY = (round(sum(p[0] for p in PADS) / 3), 63, round(sum(p[1] for p in PADS) / 3))   # (21, 63, -15)
COASTER = (-48, 63, 41)                                  # à l'ouest du guichet (-45, 64, 41) de tools/arcade/gen_coaster.py
BEACONS = [(ELY, None, 'blanche, élytra'), (COASTER, 'red_stained_glass', 'rouge, montagne russe')]


def patch(rel, anchor, new, where='after'):
    p = os.path.join(F, rel + '.mcfunction')
    L = open(p, encoding='utf-8').read().split('\n')
    if all(l in L for l in new):
        return
    i = L.index(anchor) + (1 if where == 'after' else 0)
    L[i:i] = new
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


L = ['# Balises du spawn (générées par tools/lobby/gen_beacons.py)']
for (x, y, z), glass, lab in BEACONS:
    L += [f'# {lab}',
          f'fill {x - 1} {y - 1} {z - 1} {x + 1} {y - 1} {z + 1} minecraft:iron_block',
          f'setblock {x} {y} {z} minecraft:beacon',
          f'fill {x} {y + 1} {z} {x} 319 {z} minecraft:air']
    if glass:
        L.append(f'setblock {x} {y + 1} {z} minecraft:{glass}')
L.append('data modify storage mg:lobby beacon1 set value 1b')
with open(os.path.join(F, 'lobby/beacons.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(L) + '\n')

patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby food1 run schedule function mg:lobby/food_build 12s',
      ['execute if score $setup mg.st matches 1 unless data storage mg:lobby beacon1 run schedule function mg:lobby/beacons 18s'])
patch('core/setup_build', 'schedule function mg:sky/build 40s', ['schedule function mg:lobby/beacons 55s'])
patch('desinstaller', 'schedule clear mg:lobby/food_build', ['schedule clear mg:lobby/beacons', 'data remove storage mg:lobby beacon1'])
print('Balises OK :', ELY, COASTER)
