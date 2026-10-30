"""Suppression one-shot de l'ancienne balise de la montagne russe : python tools/lobby/gen_beacons.py .

La balise des élytra est retirée par elytra/spawn_clean (drapeau mg:lobby elyclean5).
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

# ancienne balise rouge de la montagne russe (-48, 63, 41) : supprimée une fois par mg:lobby/coaster_beacon_off
OLD_COASTER = (-48, 63, 41)

w('lobby/coaster_beacon_off', ['# Ancienne balise de la montagne russe (supprimée) : une seule fois, drapeau mg:lobby coasterbeacon',
                              f'setblock {OLD_COASTER[0]} {OLD_COASTER[1]} {OLD_COASTER[2]} minecraft:air',
                              f'setblock {OLD_COASTER[0]} {OLD_COASTER[1] + 1} {OLD_COASTER[2]} minecraft:air',
                              'kill @e[type=minecraft:text_display,tag=mg.csd]',
                              'kill @e[type=minecraft:minecart,tag=mg.cst]',
                              'data modify storage mg:lobby coasterbeacon set value 1b'])
patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby ely4 run schedule function mg:elytra/build 14s',
      ['execute unless data storage mg:lobby coasterbeacon run function mg:lobby/coaster_beacon_off'], 'before')
print('Balise montagne russe OK')
