"""Branche le mode bataille (id 63 → jeu 61, arène $ktr = 3, $kbat = 1) et le choix du kart : python wire_kart3.py <racine>. Une seule fois."""
import json, os, sys

R = sys.argv[1]
F = os.path.join(R, 'data/mg/function')

def patch(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    s = open(path, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, (rel, old[:60], s.count(o))
    open(path, 'w', encoding='utf-8', newline='').write(s.replace(o, n))

patch('core/go', 'matches 1..62', 'matches 1..63')
patch('core/request', 'execute if score $game mg.st matches 62 run scoreboard players set $ktr mg.st 2\n',
      'execute if score $game mg.st matches 62 run scoreboard players set $ktr mg.st 2\n'
      'scoreboard players set $kbat mg.st 0\n'
      'execute if score $game mg.st matches 63 run scoreboard players set $kbat mg.st 1\n'
      'execute if score $game mg.st matches 63 run scoreboard players set $ktr mg.st 3\n'
      'execute if score $game mg.st matches 63 run scoreboard players set $game mg.st 61\n')
old = 'execute if score $game mg.st matches 61 if score $ktr mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une course de ","color":"gray"},{"text":"🏎 KART","color":"gold","bold":true},{"text":" dans le Royaume Koopa (3 tours, pièges, objets) !","color":"gray"}]'
patch('core/request', old, old + '\n' +
      'execute if score $game mg.st matches 61 if score $ktr mg.st matches 3 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une ","color":"gray"},{"text":"🎈 BATAILLE DE KARTS","color":"red","bold":true},{"text":" dans la Forteresse Bob-omb (3 ballons chacun, dernier en lice gagne) !","color":"gray"}]')
patch('core/setup_build', 'data remove storage mg:kart built2\n', 'data remove storage mg:kart built2\ndata remove storage mg:kart built3\n')
patch('core/load', 'execute if score $setup mg.st matches 1 if data storage mg:kart built unless data storage mg:kart built2 run schedule function mg:kart/t2/build 8s\n',
      'execute if score $setup mg.st matches 1 if data storage mg:kart built unless data storage mg:kart built2 run schedule function mg:kart/t2/build 8s\n'
      'execute if score $setup mg.st matches 1 if data storage mg:kart built2 unless data storage mg:kart built3 run schedule function mg:kart/t3/build 10s\n')
OBJ = ['mg.kty', 'mg.kcol', 'mg.kbl']
patch('core/load', 'scoreboard objectives add mg.sv trigger\n',
      'scoreboard objectives add mg.sv trigger\n' + ''.join(f'scoreboard objectives add {o} dummy\n' for o in OBJ) + 'scoreboard objectives add mg.kch trigger\n')
patch('desinstaller', 'scoreboard objectives remove mg.sv\n',
      'scoreboard objectives remove mg.sv\n' + ''.join(f'scoreboard objectives remove {o}\n' for o in OBJ + ['mg.kch']))
patch('aide', 'tellraw @s [{"text":"• Kart, Royaume Koopa (admins) : ","color":"gray"}',
      'tellraw @s [{"text":"• Bataille de karts (admins) : ","color":"gray"},{"text":"/trigger mg.go set 63","color":"yellow"},{"text":" ; 3 ballons, dernier en lice gagne (arène : /function mg:kart/build_arena)","color":"gray"}]\n'
      'tellraw @s [{"text":"• Choisir son kart (en course) : ","color":"gray"},{"text":"/trigger mg.kch set 1..4","color":"yellow"},{"text":" (Standard, Bolide, Mini, Costaud), 11..18 = couleur","color":"gray"}]\n'
      'tellraw @s [{"text":"• Kart, Royaume Koopa (admins) : ","color":"gray"}')
patch('core/menu_chat', 'tellraw @s ["",{"text":" [🏎 KART : Royaume Koopa]"',
      'tellraw @s ["",{"text":" [🎈 KART : Bataille]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.go set 63"},"hover_event":{"action":"show_text","value":"3 ballons chacun dans la Forteresse Bob-omb, dernier en lice gagne"}}]\n'
      'tellraw @s ["",{"text":" [🏎 KART : Royaume Koopa]"')
p = os.path.join(R, 'data/mg/dialog/menu.json')
d = json.load(open(p, encoding='utf-8'))
d['actions'].insert(2, {"label": [{"text": "🎈 KART : Bataille", "color": "light_purple", "bold": True}],
                        "tooltip": [{"text": "Bataille de ballons dans la Forteresse Bob-omb : 3 ballons chacun, chaque coup en crève un, dernier en lice gagne", "color": "gray"}],
                        "action": {"type": "minecraft:run_command", "command": "trigger mg.go set 63"}})
open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
p = os.path.join(R, 'tools/party_pool.py'); s = open(p, encoding='utf-8').read()
a = "(62, 'KART : ROYAUME KOOPA', 'red', 9 * M),"
assert a in s
s = s.replace(a, a + " (63, 'KART : BATAILLE', 'light_purple', 4 * M),")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
