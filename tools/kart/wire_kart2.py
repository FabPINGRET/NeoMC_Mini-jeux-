"""Branche le circuit 2 du kart (Royaume Koopa, id 62 → jeu 61 avec $ktr = 2) : python wire_kart2.py <racine du dépôt>. Une seule fois."""
import json, os, sys

R = sys.argv[1]
F = os.path.join(R, 'data/mg/function')

def patch(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    s = open(path, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, (rel, old[:60], s.count(o))
    open(path, 'w', encoding='utf-8', newline='').write(s.replace(o, n))

patch('core/go', 'matches 1..61', 'matches 1..62')
patch('core/request', 'scoreboard players operation $game mg.st = @s mg.go\nscoreboard players reset @s mg.go\n',
      'scoreboard players operation $game mg.st = @s mg.go\nscoreboard players reset @s mg.go\n'
      '# Kart : 61 = Circuit Champignon, 62 = Royaume Koopa → jeu 61 + circuit $ktr\n'
      'scoreboard players set $ktr mg.st 1\n'
      'execute if score $game mg.st matches 62 run scoreboard players set $ktr mg.st 2\n'
      'execute if score $game mg.st matches 62 run scoreboard players set $game mg.st 61\n')
s = open(os.path.join(F, 'core/request.mcfunction'), encoding='utf-8').read()
old = 'execute if score $game mg.st matches 61 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une course de ","color":"gray"},{"text":"🏎 KART","color":"gold","bold":true},{"text":" sur le Circuit Champignon (3 tours, objets) !","color":"gray"}]'
assert s.count(old) == 1
patch('core/request', old,
      old.replace('matches 61 run', 'matches 61 if score $ktr mg.st matches 1 run') + '\n'
      + old.replace('matches 61 run', 'matches 61 if score $ktr mg.st matches 2 run')
           .replace(' sur le Circuit Champignon (3 tours, objets) !', ' dans le Royaume Koopa (3 tours, pièges, objets) !'))
patch('core/setup_build', 'function mg:kart/build\n', 'data remove storage mg:kart built2\nfunction mg:kart/build\n')
patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:kart built run schedule function mg:kart/build 5s\n',
      'execute if score $setup mg.st matches 1 unless data storage mg:kart built run schedule function mg:kart/build 5s\n'
      'execute if score $setup mg.st matches 1 if data storage mg:kart built unless data storage mg:kart built2 run schedule function mg:kart/t2/build 8s\n')
patch('aide', 'tellraw @s [{"text":"• Kart, Circuit Champignon (admins) : ","color":"gray"}',
      'tellraw @s [{"text":"• Kart, Royaume Koopa (admins) : ","color":"gray"},{"text":"/trigger mg.go set 62","color":"yellow"},{"text":" ; grand circuit avec montées, pièges et animaux (reconstruire : /function mg:kart/build_koopa)","color":"gray"}]\n'
      'tellraw @s [{"text":"• Kart, Circuit Champignon (admins) : ","color":"gray"}')
patch('core/menu_chat', 'tellraw @s ["",{"text":" [🏎 KART : Circuit Champignon]"',
      'tellraw @s ["",{"text":" [🏎 KART : Royaume Koopa]","color":"red","click_event":{"action":"run_command","command":"trigger mg.go set 62"},"hover_event":{"action":"show_text","value":"Grand circuit : montées, château de Bowser, pièges, 3 tours"}}]\n'
      'tellraw @s ["",{"text":" [🏎 KART : Circuit Champignon]"')
p = os.path.join(R, 'data/mg/dialog/menu.json')
d = json.load(open(p, encoding='utf-8'))
d['actions'].insert(1, {"label": [{"text": "🏎 KART : Royaume Koopa", "color": "red", "bold": True}],
                        "tooltip": [{"text": "Grand circuit de 1,6 km : plage, jungle, désert, château de Bowser ; montées, sauts, Thwomps, plantes Piranha, Chomp...", "color": "gray"}],
                        "action": {"type": "minecraft:run_command", "command": "trigger mg.go set 62"}})
open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
p = os.path.join(R, 'tools/party_pool.py'); s = open(p, encoding='utf-8').read()
s = s.replace("(56, 'COURSE DE BATEAUX', 'aqua', 5 * M), (61, 'KART', 'gold', 8 * M),",
              "(56, 'COURSE DE BATEAUX', 'aqua', 5 * M), (61, 'KART', 'gold', 8 * M), (62, 'KART : ROYAUME KOOPA', 'red', 9 * M),")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
