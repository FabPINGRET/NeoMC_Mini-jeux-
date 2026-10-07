"""Branche Dropper : Défi (id 65, compétitif, niveau de l'Aventure au hasard) : python wire_dropdefi.py <racine du dépôt>. Une seule fois."""
import json, os, sys

R = sys.argv[1]
F = os.path.join(R, 'data/mg/function')

def patch(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    s = open(path, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, (rel, old[:60], s.count(o))
    open(path, 'w', encoding='utf-8', newline='').write(s.replace(o, n))

patch('core/go', 'matches 1..64', 'matches 1..65')
patch('core/request', 'execute if score $game mg.st matches 64 run function mg:dropadv/prepare\n',
      'execute if score $game mg.st matches 64 run function mg:dropadv/prepare\nexecute if score $game mg.st matches 65 run function mg:dropadv/c_prepare\n')
patch('core/request', 'execute if score $game mg.st matches 64 run tellraw',
      'execute if score $game mg.st matches 65 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⬇ DROPPER : DÉFI","color":"aqua","bold":true},{"text":" (même puits pour tous, niveau au hasard, premier à 3 manches) !","color":"gray"}]\n'
      'execute if score $game mg.st matches 64 run tellraw')
patch('core/begin', 'execute if score $game mg.st matches 64 run function mg:dropadv/go\n',
      'execute if score $game mg.st matches 64 run function mg:dropadv/go\nexecute if score $game mg.st matches 65 run function mg:dropadv/c_go\n')
patch('core/game_tick', 'execute if score $game mg.st matches 64 run function mg:dropadv/tick\n',
      'execute if score $game mg.st matches 64 run function mg:dropadv/tick\nexecute if score $game mg.st matches 65 run function mg:dropadv/c_tick\n')
patch('core/return_lobby', 'execute if score $game mg.st matches 64 run function mg:dropadv/cleanup\n',
      'execute if score $game mg.st matches 64..65 run function mg:dropadv/cleanup\n')
patch('core/sub/dropper', 'tellraw @s ["",{"text":" [« Retour au menu]"',
      'tellraw @s ["",{"text":" [⬇ Dropper : Défi]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 65"},"hover_event":{"action":"show_text","value":"Compétitif : tout le monde dans le même niveau de l\'Aventure tiré au hasard, le premier dans l\'eau gagne la manche"}}]\n'
      'tellraw @s ["",{"text":" [« Retour au menu]"')
patch('aide', 'tellraw @s [{"text":"• Dropper : Aventure (admins) : ","color":"gray"}',
      'tellraw @s [{"text":"• Dropper : Défi (admins) : ","color":"gray"},{"text":"/trigger mg.go set 65","color":"yellow"},{"text":" ; même puits pour tous, premier dans l\'eau, premier à 3 manches","color":"gray"}]\n'
      'tellraw @s [{"text":"• Dropper : Aventure (admins) : ","color":"gray"}')
p = os.path.join(R, 'data/mg/dialog/sub_dropper.json')
d = json.load(open(p, encoding='utf-8'))
d['actions'].insert(1, {"label": [{"text": "⬇ Dropper : Défi", "color": "aqua", "bold": True}],
                        "tooltip": [{"text": "Compétitif : un niveau de l'Aventure tiré au hasard à chaque manche, tout le monde dans le même puits, le premier dans l'eau gagne la manche (premier à 3)", "color": "gray"}],
                        "action": {"type": "minecraft:run_command", "command": "trigger mg.go set 65"}})
open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
p = os.path.join(R, 'tools/party_pool.py'); s = open(p, encoding='utf-8').read()
a = "(64, 'DROPPER : AVENTURE', 'aqua', 8 * M),"
assert a in s
s = s.replace(a, a + " (65, 'DROPPER : DÉFI', 'aqua', 6 * M),")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
p = os.path.join(R, 'README.md'); s = open(p, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
anchor = '| **⬇ The Dropper : Aventure** (id 64) |'
assert s.count(anchor) == 1
row = ("| **⬇ Dropper : Défi** (id 65) | Version compétitive de l'Aventure, comme le tube commun : à chaque manche, un des 10 niveaux est tiré au hasard "
       "(jamais deux fois de suite le même) et tout le monde saute dans le même puits (réparti sur les 4 côtés du rebord). Le premier dans l'eau gagne "
       "la manche, raté = retour en haut ; premier à 3 manches. Manche annulée au bout de 90 s sans gagnant. | 2+ |" + nl)
s = s.replace(anchor, row + anchor, 1)
open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok')
