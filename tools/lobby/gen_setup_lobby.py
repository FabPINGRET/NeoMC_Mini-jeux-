"""Commande admin /function mg:setup_lobby : reconstruit SEULEMENT le spawn (lobby), comme mg:setup mais sans les arènes ni les mondes.

    python tools/lobby/gen_setup_lobby.py .     (après gen_hub.py et gen_decofix.py)

Ordre : spawn (lobby/build, en quelques ticks : sa fin refait décor, armurerie, parkour et terrain de foot), puis buffet, socles d'élytra
et leurs abords, Hall, arène PvP, étang, hub des portails (qui relance hub/decofix 20 s plus tard). Fin annoncée au bout d'une minute.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = sys.argv[1] if len(sys.argv) > 1 else '.'
sys.path.insert(0, os.path.join(HERE, '..', 'lib'))
import mcfn  # noqa: E402

_fn = mcfn.Fn(os.path.join(R, 'data/mg/function'))
w, patch = _fn.write, _fn.patch
ADMIN = '[{"text":"[Mini-Jeux] ","color":"gold"},{"text":"%s","color":"%s"}]'

w('setup_lobby', [
    '# /function mg:setup_lobby (OP) : reconstruit seulement le spawn, ses constructions et son décor (pas les arènes ni les mondes)',
    'execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : lance d\'abord /function mg:setup","color":"red"}',
    'execute if score $slb mg.st matches 1 run return run tellraw @s {"text":"⏳ Reconstruction du lobby déjà en cours.","color":"yellow"}',
    'scoreboard players set $slb mg.st 1',
    'tellraw @a[tag=mg.admin] ' + ADMIN % ('Reconstruction du lobby lancée (environ 1 minute)...', 'gray'),
    'execute unless entity @s[tag=mg.admin] run tellraw @s ' + ADMIN % ('Reconstruction du lobby lancée (environ 1 minute)...', 'gray'),
    # drapeaux des constructions du spawn (reposés à la fin de chacune)
    'data remove storage mg:lobby v6', 'data remove storage mg:lobby food1', 'data remove storage mg:lobby ely4',
    'data remove storage mg:lobby elyclean5', 'data remove storage mg:lobby deco3', 'data remove storage mg:lobby decofix2',
    'function mg:lobby/build',
    'schedule function mg:lobby/food_build 20s',
    'schedule function mg:elytra/spawn_clean 22s',
    'schedule function mg:elytra/build 24s',
    'schedule function mg:hall/build 26s',
    'schedule function mg:pvpc/build_start 28s',
    'schedule function mg:lobby/fish/build 30s',
    'schedule function mg:hub/build 32s',
    'schedule function mg:core/setup_lobby_done 60s'])
w('core/setup_lobby_done', [
    '# Fin de mg:setup_lobby (hub/decofix part encore 20 s après hub/build)',
    'scoreboard players reset $slb mg.st',
    'tellraw @a[tag=mg.admin] ' + ADMIN % ('Lobby reconstruit.', 'green')])
patch('desinstaller', 'data remove storage mg:lobby decofix2',
      ['schedule clear mg:core/setup_lobby_done', 'schedule clear mg:hub/build', 'schedule clear mg:lobby/fish/build', 'scoreboard players reset $slb mg.st'])
print('setup_lobby OK')
