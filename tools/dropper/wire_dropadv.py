"""Branche The Dropper : Aventure (id 64) dans le moteur et les menus : python wire_dropadv.py <racine du dépôt>. Une seule fois."""
import json, os, sys

R = sys.argv[1]
F = os.path.join(R, 'data/mg/function')

def patch(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    s = open(path, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, (rel, old[:60], s.count(o))
    open(path, 'w', encoding='utf-8', newline='').write(s.replace(o, n))

patch('core/go', 'matches 1..63', 'matches 1..64')
patch('core/request', 'execute if score $game mg.st matches 23 run function mg:dropper/prepare\n',
      'execute if score $game mg.st matches 23 run function mg:dropper/prepare\nexecute if score $game mg.st matches 64 run function mg:dropadv/prepare\n')
patch('core/request', 'execute if score $game mg.st matches 23 unless score $sg mg.st matches 1 run tellraw',
      'execute if score $game mg.st matches 64 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⬇ THE DROPPER : AVENTURE","color":"aqua","bold":true},{"text":" (10 niveaux à thème, le premier qui les finit gagne) !","color":"gray"}]\n'
      'execute if score $game mg.st matches 23 unless score $sg mg.st matches 1 run tellraw')
patch('core/begin', 'execute if score $game mg.st matches 23 run function mg:dropper/go\n',
      'execute if score $game mg.st matches 23 run function mg:dropper/go\nexecute if score $game mg.st matches 64 run function mg:dropadv/go\n')
patch('core/game_tick', 'execute if score $game mg.st matches 23 run function mg:dropper/tick\n',
      'execute if score $game mg.st matches 23 run function mg:dropper/tick\nexecute if score $game mg.st matches 64 run function mg:dropadv/tick\n')
patch('core/return_lobby', 'execute if score $game mg.st matches 61 run function mg:kart/cleanup\n',
      'execute if score $game mg.st matches 61 run function mg:kart/cleanup\nexecute if score $game mg.st matches 64 run function mg:dropadv/cleanup\n')
patch('core/setup_build', 'data remove storage mg:kart built2\n', 'data remove storage mg:kart built2\ndata remove storage mg:dropadv built\nschedule function mg:dropadv/build 30s\n')
patch('core/load', 'execute if score $setup mg.st matches 1 if data storage mg:kart built2 unless data storage mg:kart built3 run schedule function mg:kart/t3/build 10s\n',
      'execute if score $setup mg.st matches 1 if data storage mg:kart built2 unless data storage mg:kart built3 run schedule function mg:kart/t3/build 10s\n'
      'execute if score $setup mg.st matches 1 unless data storage mg:dropadv built run schedule function mg:dropadv/build 40s\n')
patch('core/sub/dropper', 'tellraw @s ["",{"text":" [« Retour au menu]"',
      'tellraw @s ["",{"text":" [⬇ Dropper : Aventure (10 niveaux)]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 64"},"hover_event":{"action":"show_text","value":"10 grands niveaux à thème enchaînés : le premier qui les finit gagne"}}]\n'
      'tellraw @s ["",{"text":" [« Retour au menu]"')
patch('aide', 'tellraw @s [{"text":"• Bataille de karts (admins) : ","color":"gray"}',
      'tellraw @s [{"text":"• Dropper : Aventure (admins) : ","color":"gray"},{"text":"/trigger mg.go set 64","color":"yellow"},{"text":" ; 10 niveaux à thème (reconstruire : /function mg:dropadv/build)","color":"gray"}]\n'
      'tellraw @s [{"text":"• Bataille de karts (admins) : ","color":"gray"}')
p = os.path.join(R, 'data/mg/dialog/sub_dropper.json')
d = json.load(open(p, encoding='utf-8'))
d['actions'].insert(0, {"label": [{"text": "⬇ Dropper : Aventure", "color": "aqua", "bold": True}],
                        "tooltip": [{"text": "10 grands niveaux à thème enchaînés (arc-en-ciel, mine, enfer, salon géant, nuages...) : le premier qui les finit gagne", "color": "gray"}],
                        "action": {"type": "minecraft:run_command", "command": "trigger mg.go set 64"}})
open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
p = os.path.join(R, 'tools/party_pool.py'); s = open(p, encoding='utf-8').read()
a = "(25, 'DROPPER : TUBE COMMUN', 'aqua', 6 * M),"
assert a in s
s = s.replace(a, a + " (64, 'DROPPER : AVENTURE', 'aqua', 8 * M),")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
p = os.path.join(R, 'README.md'); s = open(p, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
anchor = '| **The Dropper** |'
assert s.count(anchor) == 1
row = ("| **⬇ The Dropper : Aventure** (id 64) | Dix grands puits à thème (21 × 21, 105 blocs de haut, z 24000) enchaînés, dans l'esprit des maps de dropper "
       "classiques : **Arc-en-ciel** (anneaux en entonnoir), **Spirale** (boules de lumière qui tournent), **La mine** (poutres, rails, toiles), "
       "**Rideaux** (nappes de laine percées), **Trous piégés** (certains trous sont fermés par du verre), **L'Enfer** (basalte, champignons géants), "
       "**Le salon géant** (on est minuscule : lampe, table, chaise, bocal à poisson), **La bibliothèque** (étagères, livres volants, encrier), "
       "**La forêt** (branches, toiles, nénuphars pièges) et **Les nuages** (final sur un seul bloc d'eau). On saute du rebord, on doit finir dans l'eau ; "
       "tout le reste renvoie en haut du niveau. Le premier à finir les 10 niveaux gagne, sinon le plus avancé au bout de 10 minutes (niveau de chacun "
       "dans le tableau de droite). Générateur : `tools/dropper/gen_dropper_adv.py`. | 1+ |" + nl)
s = s.replace(anchor, row + anchor, 1)
open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok')
