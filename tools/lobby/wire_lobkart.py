"""Branche le kart libre du spawn (lobkart/, kart/t4/) dans le moteur : python wire_lobkart.py <racine du dépôt>. Une seule fois."""
import os, sys

R = sys.argv[1]
F = os.path.join(R, 'data/mg/function')

def patch(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    s = open(path, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, (rel, old[:60], s.count(o))
    open(path, 'w', encoding='utf-8', newline='').write(s.replace(o, n))

# aiguillages du moteur : pendant le tick du kart libre ($klob = 1), tables du circuit du spawn
for name in ('cp_check', 'cp_tp', 'bill_step'):
    patch(f'kart/{name}', 'execute if score $ktr mg.st matches 2 run function mg:kart/t2/' + name + '\n',
          'execute if score $klob mg.st matches 1 run return run function mg:kart/t4/' + name + '\n'
          'execute if score $ktr mg.st matches 2 run function mg:kart/t2/' + name + '\n')
patch('kart/lap', 'scoreboard players add @s mg.klp 1\n',
      'execute if score $klob mg.st matches 1 run return run function mg:lobkart/lap\nscoreboard players add @s mg.klp 1\n')
patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick\n',
      'execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick\n\n# Kart libre du spawn\n'
      'execute if score $setup mg.st matches 1 run function mg:lobkart/tick\n')
patch('core/tick', 'tag=!mg.pkr,tag=!mg.visit,gamemode=!spectator', 'tag=!mg.pkr,tag=!mg.lk,tag=!mg.visit,gamemode=!spectator')
patch('core/opt', 'execute if score @s mg.opt matches 26 ', 'execute if score @s mg.opt matches 27 run function mg:lobkart/exit\nexecute if score @s mg.opt matches 26 ')
patch('core/load', 'scoreboard objectives add mg.kstk dummy\n', 'scoreboard objectives add mg.kstk dummy\nscoreboard objectives add mg.klt dummy\nscoreboard objectives add mg.klb dummy\n')
patch('core/reconnect', 'scoreboard players reset @s mg.lg\n', 'scoreboard players reset @s mg.lg\nfunction mg:lobkart/leave\n')
patch('plot/enter', 'function mg:parkour/quit\n', 'function mg:parkour/quit\nfunction mg:lobkart/leave\n')
patch('plot/visit', 'function mg:parkour/quit\n', 'function mg:parkour/quit\nfunction mg:lobkart/leave\n')
patch('survie/enter', 'execute unless score @s mg.svid matches 1.. run function mg:survie/assign\n',
      'function mg:lobkart/leave\nexecute unless score @s mg.svid matches 1.. run function mg:survie/assign\n')
patch('desinstaller', 'kill @e[tag=mg.lby]\n', 'kill @e[tag=mg.lby]\nkill @e[tag=mg.lkart]\n')
print('ok')
