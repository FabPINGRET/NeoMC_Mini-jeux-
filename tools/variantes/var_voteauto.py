"""Lancement automatique par majorité de votes : vote/auto_tick, vote/auto_launch, crochets dans core/tick et core/go.

Jamais lancé seul : gen_variants.py appelle run() après var_votemaps.run() (relit vote/refresh et vote/show).
"""
import os
import re

import var_common as VC
from var_common import js, patch, replace, w


def run():
    # ============================================================ lancement automatique par majorité de votes
    # ≥ 3 joueurs et plus de la moitié votent pour le même jeu (votes jeu + cartes) → compte à rebours de 10 s → lancement.
    GV = []   # (n°, joueur fictif, libellé, couleur) lus dans vote/refresh et vote/show
    ref = open(os.path.join(VC.F, 'vote/refresh.mcfunction'), encoding='utf-8').read()
    shw = open(os.path.join(VC.F, 'vote/show.mcfunction'), encoding='utf-8').read()
    for fake, n in re.findall(r'execute store result score (\S+) mg\.vb if entity @a\[scores=\{mg\.vc=(\d+)\}\]', ref):
        mm = re.search(r'execute if score ' + re.escape(fake) + r' mg\.vb matches 1\.\. run tellraw @s \[\{"text":" ▸ ","color":"gray"\},\{"text":"([^"]+)","color":"(\w+)"\}', shw)
        GV.append((int(n), fake, mm.group(1) if mm else fake, mm.group(2) if mm else 'gold'))
    AUTO = 200
    L = ['# Votes à la majorité (core/tick, toutes les secondes, lobby uniquement). Généré.',
         '# Joueurs comptés : tous les joueurs connectés hors monde de survie et hors pause. Il en faut 3 au moins.',
         'execute unless score $state mg.st matches 0 run return run scoreboard players set $vat mg.st -1',
         'execute if score $setup mg.st matches 0 run return 0',
         'execute store result score $vnp mg.st if entity @a[tag=mg.init,tag=!mg.spectate,tag=!mg.surv]',
         '# recompte seulement si le nombre de joueurs a changé (un votant a pu partir) ; sinon les votes sont déjà à jour',
         'execute unless score $vnp mg.st = $vnpo mg.st run function mg:vote/refresh',
         'scoreboard players operation $vnpo mg.st = $vnp mg.st',
         'scoreboard players set $vmax mg.st 0']
    L += [f'scoreboard players operation $vmax mg.st > {fake} mg.vb' for n, fake, lab, col in GV]
    L += ['scoreboard players operation $vm2 mg.st = $vmax mg.st', 'scoreboard players operation $vm2 mg.st += $vmax mg.st',
          'scoreboard players set $vok mg.st 0',
          'execute if score $vnp mg.st matches 3.. if score $vm2 mg.st > $vnp mg.st run scoreboard players set $vok mg.st 1',
          '# Majorité perdue pendant le compte à rebours → annulé',
          'execute if score $vok mg.st matches 0 if score $vat mg.st matches 1.. run tellraw @a[tag=!mg.surv] {"text":"☑ Plus de majorité : lancement automatique annulé.","color":"gray"}',
          'execute if score $vok mg.st matches 0 run return run scoreboard players set $vat mg.st -1',
          'scoreboard players set $vlead mg.st 0']
    L += [f'execute if score {fake} mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st {n}' for n, fake, lab, col in GV]
    L += ['# Nouvelle majorité → compte à rebours',
          f'execute unless score $vat mg.st matches 1.. run scoreboard players set $vat mg.st {AUTO // 20 + 1}']
    for n, fake, lab, col in GV:
        L.append(f'execute if score $vat mg.st matches {AUTO // 20 + 1} if score $vlead mg.st matches {n} run tellraw @a[tag=!mg.surv] ' + js([
            {'text': '☑ Majorité pour ', 'color': 'green'}, {'text': lab, 'color': col, 'bold': True},
            {'text': ' (', 'color': 'gray'}, {'score': {'name': fake, 'objective': 'mg.vb'}, 'color': 'gold'}, {'text': ' / ', 'color': 'gray'},
            {'score': {'name': '$vnp', 'objective': 'mg.st'}, 'color': 'gold'}, {'text': ' joueurs) : lancement dans 10 s !', 'color': 'gray'}]))
    L += ['scoreboard players remove $vat mg.st 1',
          'execute if score $vat mg.st matches 1..10 run title @a[tag=!mg.surv] actionbar [{"text":"☑ Jeu voté : lancement dans ","color":"green"},{"score":{"name":"$vat","objective":"mg.st"},"color":"gold","bold":true},{"text":" s","color":"green"}]',
          'execute if score $vat mg.st matches 1..3 as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5',
          'execute if score $vat mg.st matches 0 run function mg:vote/auto_launch']
    w('vote/auto_tick', L)
    w('vote/auto_launch', ['# Fin du compte à rebours : un votant (marqué mg.vauto, accepté par core/go comme un admin) lance le jeu le plus voté. Généré.',
                           'scoreboard players set $vat mg.st -1',
                           'tag @r[tag=mg.init,tag=!mg.surv,scores={mg.vc=1..}] add mg.vauto',
                           'execute as @a[tag=mg.vauto,limit=1] run function mg:vote/launch',
                           'tag @a remove mg.vauto'])
    patch('core/tick', 'execute as @a[scores={mg.vote=1..}] run function mg:vote/cast', [
        '# Votes à la majorité : lancement automatique (une fois par seconde)',
        'scoreboard players add $vtk mg.st 1',
        'execute if score $vtk mg.st matches 20.. run function mg:vote/auto_tick',
        'execute if score $vtk mg.st matches 20.. run scoreboard players set $vtk mg.st 0'])
    replace('core/go', 'execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Seul un admin peut lancer un jeu.","color":"red"}]',
            'execute unless entity @s[tag=mg.admin] unless entity @s[tag=mg.vauto] run tellraw @s [{"text":"⚠ Seul un admin peut lancer un jeu.","color":"red"}]')
    replace('core/go', 'execute unless entity @s[tag=mg.admin] run return run scoreboard players reset @s mg.go',
            'execute unless entity @s[tag=mg.admin] unless entity @s[tag=mg.vauto] run return run scoreboard players reset @s mg.go')
