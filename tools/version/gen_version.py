"""ℹ Version du datapack en place (menu admin ≡ → « ℹ Version du datapack », ou /function mg:version/show).

    python tools/version/gen_version.py .

Trois infos, écrites par datapack-sync (DockerMC) :
- « en place »  : data/mg/function/sync/stamp.mcfunction, écrit DANS le pack déployé (pas dans le dépôt) et exécuté
                  au chargement (tag #mg:version, entrée facultative) → storage mg:version files {commit,date,subject} ;
                  ce n'est à jour qu'une fois le /reload (ou le redémarrage) réussi ;
- « reçue »     : RCON à chaque nouveau commit → storage mg:version recv {commit,date,subject,at} ;
- « vérif »     : RCON à chaque passage réussi de la synchro (60 s) → mg:version seen {at,gt}.
Comparaison : recv.commit ≠ files.commit → mise à jour reçue mais pas (ou mal) appliquée.
"""
import json
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def w(rel, lines):
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def patch(rel, anchor, new, where='after'):
    p = os.path.join(F, rel + '.mcfunction')
    L = open(p, encoding='utf-8').read().split('\n')
    if all(l in L for l in new):
        return
    i = L.index(anchor) + (1 if where == 'after' else 0)
    L[i:i] = new
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


os.makedirs(os.path.join(R, 'data/mg/tags/function'), exist_ok=True)
with open(os.path.join(R, 'data/mg/tags/function/version.json'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(js({'values': [{'id': 'mg:sync/stamp', 'required': False}]}) + '\n')

S = 'mg:version'
TAG = {'text': '[Version] ', 'color': 'gold'}


def nbt(path, col='yellow', **k):
    return dict({'nbt': path, 'storage': S, 'color': col}, **k)


w('version/load', ['# Au chargement (/reload ou démarrage) : version des fichiers chargés + heure de jeu. Généré par tools/version/gen_version.py.',
                   f'data remove storage {S} files',
                   'function #mg:version',
                   f'execute store result storage {S} gt long 1 run time query gametime'])
w('version/ago', ['# $vm = minutes de jeu depuis la valeur de jeu $vg (→ $vh h $vm min)',
                  'execute store result score $vn mg.st run time query gametime',
                  'scoreboard players operation $vn mg.st -= $vg mg.st',
                  'scoreboard players set #1200 mg.st 1200', 'scoreboard players set #60 mg.st 60',
                  'scoreboard players operation $vn mg.st /= #1200 mg.st',
                  'scoreboard players operation $vh mg.st = $vn mg.st', 'scoreboard players operation $vh mg.st /= #60 mg.st',
                  'scoreboard players operation $vm mg.st = $vn mg.st', 'scoreboard players operation $vm mg.st %= #60 mg.st'])
AGO = [{'text': ' (il y a ', 'color': 'gray'}, {'score': {'name': '$vh', 'objective': 'mg.st'}, 'color': 'gray'}, {'text': ' h ', 'color': 'gray'},
       {'score': {'name': '$vm', 'objective': 'mg.st'}, 'color': 'gray'}, {'text': ' min de serveur allumé)', 'color': 'gray'}]
RELOAD = {'text': '[Appliquer : /reload]', 'color': 'green', 'bold': True,
          'click_event': {'action': 'run_command', 'command': '/minecraft:reload'},
          'hover_event': {'action': 'show_text', 'value': 'OP : /minecraft:reload (entre deux parties)'}}
w('version/show', ['# Fenêtre texte « version du datapack » (@s = admin)',
                   'tellraw @s ' + js([{'text': '\n', 'color': 'gold'}, {'text': 'ℹ VERSION DU DATAPACK', 'color': 'gold', 'bold': True}]),
                   # en place
                   f'execute unless data storage {S} files run tellraw @s ' + js([TAG, {'text': 'En place : ', 'color': 'white', 'bold': True},
                       {'text': 'inconnue (pack non déployé par datapack-sync, ou datapack-sync pas encore mis à jour)', 'color': 'gray'}]),
                   f'execute if data storage {S} files run tellraw @s ' + js([TAG, {'text': 'En place : ', 'color': 'white', 'bold': True},
                       nbt('files.commit', bold=True), {'text': ' du ', 'color': 'gray'}, nbt('files.date'),
                       {'text': '\n   ', 'color': 'gray'}, nbt('files.subject', 'gray', italic=True)]),
                   f'execute store result score $vg mg.st run data get storage {S} gt', 'function mg:version/ago',
                   'tellraw @s ' + js([TAG, {'text': 'Chargée', 'color': 'white'}] + AGO),
                   # reçue
                   f'execute unless data storage {S} recv run tellraw @s ' + js([TAG, {'text': 'Reçue de GitHub : ', 'color': 'white', 'bold': True},
                       {'text': 'rien (datapack-sync ne l\'a jamais signalée)', 'color': 'gray'}]),
                   f'execute if data storage {S} recv run tellraw @s ' + js([TAG, {'text': 'Reçue de GitHub : ', 'color': 'white', 'bold': True},
                       nbt('recv.commit', bold=True), {'text': ' du ', 'color': 'gray'}, nbt('recv.date'),
                       {'text': ', déposée le ', 'color': 'gray'}, nbt('recv.at')]),
                   # dernière vérif
                   f'execute if data storage {S} seen run execute store result score $vg mg.st run data get storage {S} seen.gt',
                   f'execute if data storage {S} seen run function mg:version/ago',
                   f'execute if data storage {S} seen run tellraw @s ' + js([TAG, {'text': 'Dernière vérif GitHub : ', 'color': 'white'}, nbt('seen.at')] + AGO),
                   # verdict
                   'scoreboard players set $vd mg.st 0',
                   f'data modify storage {S} tmp set from storage {S} recv.commit',
                   f'execute if data storage {S} recv unless data storage {S} files run scoreboard players set $vd mg.st 1',
                   f'execute if data storage {S} recv if data storage {S} files store success score $vd mg.st run data modify storage {S} tmp set from storage {S} files.commit',
                   f'data remove storage {S} tmp',
                   'execute if score $vd mg.st matches 1 run tellraw @s ' + js([TAG, {'text': '⚠ La version reçue n\'est pas celle en place. ', 'color': 'red', 'bold': True}, RELOAD,
                       {'text': '\n   Si ça reste rouge après le reload : le chargement a échoué → logs du serveur (scripts/logs.ps1 mc).', 'color': 'gray'}]),
                   f'execute if score $vd mg.st matches 0 if data storage {S} files run tellraw @s ' + js([TAG, {'text': '✔ À jour : la dernière version reçue est en place.', 'color': 'green', 'bold': True}]),
                   'tellraw @s ' + js({'text': '   Vérif GitHub figée depuis longtemps (> 5 min) = datapack-sync arrêté ou planté (scripts/etat.ps1).', 'color': 'dark_gray'})])

patch('core/load', 'data modify storage mg:hall sbon set value 1b', ['function mg:version/load'])
patch('core/opt', 'execute if score @s mg.opt matches 12 if entity @s[tag=mg.admin] run function mg:vote/launch',
      ['execute if score @s mg.opt matches 48 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Réservé aux admins.","color":"red"}',
       'execute if score @s mg.opt matches 48 if entity @s[tag=mg.admin] run function mg:version/show'])
print('version OK')
