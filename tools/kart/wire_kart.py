"""Branche le kart (jeu 61) dans le moteur : python wire_kart.py <racine du dépôt>. À exécuter une seule fois."""
import json, os, sys

R = sys.argv[1]
F = os.path.join(R, 'data/mg/function')

def patch(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    s = open(path, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, (rel, old[:60], s.count(o))
    open(path, 'w', encoding='utf-8', newline='').write(s.replace(o, n))

patch('core/go', 'matches 1..60', 'matches 1..61')
patch('core/begin', 'execute if score $game mg.st matches 59 run function mg:party/go\n',
      'execute if score $game mg.st matches 59 run function mg:party/go\nexecute if score $game mg.st matches 61 run function mg:kart/go\n')
patch('core/game_tick', 'execute if score $game mg.st matches 59 run function mg:party/tick\n',
      'execute if score $game mg.st matches 59 run function mg:party/tick\nexecute if score $game mg.st matches 61 run function mg:kart/tick\n')
patch('core/request', 'execute if score $game mg.st matches 59 run function mg:party/prepare\n',
      'execute if score $game mg.st matches 59 run function mg:party/prepare\nexecute if score $game mg.st matches 61 run function mg:kart/prepare\n')
patch('core/request', 'execute if score $game mg.st matches 59 run tellraw @a [',
      'execute if score $game mg.st matches 61 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une course de ","color":"gray"},{"text":"🏎 KART","color":"gold","bold":true},{"text":" sur le Circuit Champignon (3 tours, objets) !","color":"gray"}]\n'
      'execute if score $game mg.st matches 59 run tellraw @a [')
patch('core/return_lobby', '\nkill @e[tag=mg.ib]\n', '\nexecute if score $game mg.st matches 61 run function mg:kart/cleanup\nkill @e[tag=mg.ib]\n')
patch('core/setup_build', 'function mg:party/build\n', 'function mg:party/build\nfunction mg:kart/build\n')
OBJ = ['mg.ksp', 'mg.kdr', 'mg.kdd', 'mg.kbo', 'mg.khi', 'mg.kst', 'mg.kit', 'mg.kcp', 'mg.klp', 'mg.kvy', 'mg.kfp', 'mg.kpg', 'mg.krk']
patch('core/load', 'scoreboard objectives add mg.sv trigger\n',
      'scoreboard objectives add mg.sv trigger\n' + ''.join(f'scoreboard objectives add {o} dummy\n' for o in OBJ) +
      'scoreboard objectives add mg.kps dummy [{"text":"🏎 KART : progression %","color":"gold"}]\n')
patch('core/load', 'execute if score $setup mg.st matches 1 run function mg:core/rules\n',
      'execute if score $setup mg.st matches 1 run function mg:core/rules\n'
      'execute if score $setup mg.st matches 1 unless data storage mg:kart built run schedule function mg:kart/build 5s\n')
patch('desinstaller', 'scoreboard objectives remove mg.sv\n',
      'scoreboard objectives remove mg.sv\n' + ''.join(f'scoreboard objectives remove {o}\n' for o in OBJ + ['mg.kps']))
patch('aide', 'tellraw @s [{"text":"• Survie',
      'tellraw @s [{"text":"• Kart, Circuit Champignon (admins) : ","color":"gray"},{"text":"/trigger mg.go set 61","color":"yellow"},{"text":" ; Z/S/Q/D, ESPACE en tournant = dérapage, clic droit = objet","color":"gray"}]\n'
      'tellraw @s [{"text":"• Survie')
patch('core/menu_chat', 'tellraw @s ["",{"text":" [★ MINI PARTY 8 tours]"',
      'tellraw @s ["",{"text":" [🏎 KART : Circuit Champignon]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 61"},"hover_event":{"action":"show_text","value":"Course de karts, 3 tours, objets"}}]\n'
      'tellraw @s ["",{"text":" [★ MINI PARTY 8 tours]"')
p = os.path.join(R, 'data/mg/dialog/menu.json')
d = json.load(open(p, encoding='utf-8'))
d['actions'].insert(0, {"label": [{"text": "🏎 KART : Circuit Champignon", "color": "gold", "bold": True}],
                        "tooltip": [{"text": "Course de karts maniables : 3 tours, dérapages, boîtes à objets", "color": "gray"}],
                        "action": {"type": "minecraft:run_command", "command": "trigger mg.go set 61"}})
open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
p = os.path.join(R, 'README.md'); s = open(p, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
anchor = '| **★ Mini Party**'
row = ("| **🏎 Kart** (id 61) | Course de karts sur le **Circuit Champignon** (île à z 16500, piste de 1 km : départ sous un portique avec tribunes, "
       "S et épingle, château traversé par un tunnel, saut au-dessus d'un ruisseau, tuyaux, champignons géants, blocs ?). **Karts pilotés par le datapack** "
       "(touches lues directement) : Z avancer, S freiner / reculer, Q / D tourner (plus serré à basse vitesse), **ESPACE en tournant = dérapage** avec "
       "étincelles bleues puis orange et **mini-turbo** au relâchement ; herbe = ralentissement, plaques orange = boost, tremplin vert = saut, chute = remise en piste. "
       "**Boîtes ? → objets** (clic droit) : 🍌 banane, 🟢 carapace verte (rebondit), 🔴 carapace rouge (vise le pilote devant), 🍄 champignon, ⭐ étoile, ⚡ éclair ; "
       "les derniers reçoivent de meilleurs objets. 3 tours, classement en direct (barre du bas + tableau), 30 s pour finir après le premier, podium. "
       "Générateur : `tools/kart/`. | 1+ |" + nl)
s = s.replace(anchor, row + anchor, 1)
open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok')
