"""Parcours d'élytra du spawn : génère data/mg/function/elytra/*.mcfunction.

Boucle carrée au-dessus de l'île (au-dessus de y 125 : hors du volume vidé par
la reconstruction du lobby, et loin des murs de barrières des plots), 8 anneaux
à traverser dans l'ordre en descendant, départ d'une plateforme à y 175.
Lancer depuis la racine du dépôt : python3 tools/elytra/gen_elytra.py
"""
import os

OUT = os.path.join('data', 'mg', 'function', 'elytra')
PAD = (16, 63, -9)                    # bloc central du socle de départ (sol du spawn)
BACK = (16.5, 64, -10.5)
FREE = (16, 63, -21)                  # socle « élytres libres » (vol autour du spawn)              # retour après le parcours (bord du socle, pas le centre)
PLAT = (-48.5, 175, -44.5)            # point d'apparition sur la plateforme (face à l'est)
H, Y0, Y1 = 45, 172, 132              # demi-côté du carré, hauteur au départ et à l'arrivée
COLORS = ['light_blue', 'magenta', 'lime', 'orange', 'light_blue', 'magenta', 'lime', None]

# anneaux : (centre x, y, z, axe de traversée) le long du carré, aux 1/3 et 2/3 de chaque côté
path = []
for side in range(4):
    for k in (30, 60):
        s = side * 90 + k
        if side == 0:   x, z, ax = -H + k, -H, 'x'
        elif side == 1: x, z, ax = H, -H + k, 'z'
        elif side == 2: x, z, ax = H - k, H, 'x'
        else:           x, z, ax = -H, H - k, 'z'
        y = round(Y0 - s * (Y0 - Y1) / 360)
        path.append((x, y, z, ax))
N = len(path)

def W(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

os.makedirs(OUT, exist_ok=True)
DISP = 'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[%sf,%sf,%sf]}'

# ---------------------------------------------------------------- build
b = ['# Parcours d\'élytra : construction (généré par tools/elytra/gen_elytra.py)',
     'kill @e[tag=mg.elyd]',
     'data modify storage mg:lobby ely1 set value 1b', '',
     '# Socle de départ au sol']
px, py, pz = PAD
b += [f'fill {px-2} {py} {pz-2} {px+2} {py} {pz+2} minecraft:smooth_quartz',
      f'fill {px-1} {py} {pz-1} {px+1} {py} {pz+1} minecraft:light_blue_concrete',
      f'setblock {px} {py} {pz} minecraft:sea_lantern',
      f'summon minecraft:item_display {px+.5} {py+3} {pz+.5} {{Tags:["mg.elyd","mg.lspin","mg.lbob"],billboard:"fixed",item:{{id:"minecraft:elytra"}},{DISP % (1.4, 1.4, 1.4)}}}',
      f'summon minecraft:text_display {px+.5} {py+4.8} {pz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"🪽 Parcours d\'élytra","color":"aqua","bold":true}}],{DISP % (1.2, 1.2, 1.2)}}}',
      f'summon minecraft:text_display {px+.5} {py+4.3} {pz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"Monte au centre du socle","color":"gray"}}],{DISP % (0.7, 0.7, 0.7)}}}',
      '', '# Plateforme de départ']
qx, qy, qz = int(PLAT[0] - .5), PLAT[1] - 1, int(PLAT[2] - .5)
b += [f'fill {qx-2} {qy} {qz-2} {qx+2} {qy} {qz+2} minecraft:smooth_quartz',
      f'fill {qx-2} {qy} {qz-2} {qx-2} {qy+1} {qz+2} minecraft:light_blue_stained_glass',
      f'setblock {qx-2} {qy+2} {qz} minecraft:sea_lantern',
      f'summon minecraft:text_display {qx+.5} {qy+3.5} {qz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"Saute vers l\'est, ouvre tes élytres (Espace en l\'air)","color":"yellow"}},{{"text":"\\n{N} anneaux dans l\'ordre — 3 fusées pour t\'aider","color":"gray"}}],{DISP % (0.8, 0.8, 0.8)}}}',
      '', '# Anneaux (cadre 7x7, ouverture 5x5)']
for i, (x, y, z, ax) in enumerate(path, 1):
    c = COLORS[i-1]
    blk = f'minecraft:{c}_concrete' if c else 'minecraft:gold_block'
    if ax == 'x':
        b += [f'fill {x} {y-3} {z-3} {x} {y+3} {z+3} {blk}', f'fill {x} {y-2} {z-2} {x} {y+2} {z+2} minecraft:air']
        corners = [(x, y-3, z-3), (x, y-3, z+3), (x, y+3, z-3), (x, y+3, z+3)]
    else:
        b += [f'fill {x-3} {y-3} {z} {x+3} {y+3} {z} {blk}', f'fill {x-2} {y-2} {z} {x+2} {y+2} {z} minecraft:air']
        corners = [(x-3, y-3, z), (x+3, y-3, z), (x-3, y+3, z), (x+3, y+3, z)]
    b += [f'setblock {cx} {cy} {cz} minecraft:sea_lantern' for cx, cy, cz in corners]
    label = f'{i}' if i < N else '🏁'
    b.append(f'summon minecraft:text_display {x+.5} {y+4.2} {z+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"{label}","color":"white","bold":true}}],{DISP % (2, 2, 2)}}}')
fx, fy, fz = FREE
b += ['', '# Socle « élytres libres »',
      f'fill {fx-2} {fy} {fz-2} {fx+2} {fy} {fz+2} minecraft:smooth_quartz',
      f'fill {fx-1} {fy} {fz-1} {fx+1} {fy} {fz+1} minecraft:white_concrete',
      f'setblock {fx} {fy} {fz} minecraft:sea_lantern',
      f'summon minecraft:item_display {fx+.5} {fy+3} {fz+.5} {{Tags:["mg.elyd","mg.lspin","mg.lbob"],billboard:"fixed",item:{{id:"minecraft:elytra"}},{DISP % (1.4, 1.4, 1.4)}}}',
      f'summon minecraft:text_display {fx+.5} {fy+4.8} {fz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"🪽 Élytres libres","color":"white","bold":true}}],{DISP % (1.2, 1.2, 1.2)}}}',
      f'summon minecraft:text_display {fx+.5} {fy+4.3} {fz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"Vol autour du spawn, fusées illimitées — remonte dessus pour les rendre","color":"gray"}}],{DISP % (0.7, 0.7, 0.7)}}}']
W('build', b)

# ---------------------------------------------------------------- start / go
W('start', ['# Départ du parcours (@s = joueur sur le socle)',
    'execute if entity @s[tag=mg.elyf] run function mg:elytra/free_stop',
    '# Pas de baguette feu d\'artifice ni de charges de vent pendant la course (rendue à la fin)',
    'execute store result score @s mg.ehw run clear @s minecraft:blaze_rod',
    'clear @s minecraft:wind_charge',
    'tag @s add mg.ely',
    'scoreboard players set @s mg.est 0', 'scoreboard players set @s mg.ec 0',
    'scoreboard players set @s mg.et 0', 'scoreboard players set @s mg.eg 0',
    'scoreboard players set #20 mg.st 20', 'scoreboard players set #5 mg.st 5',
    'item replace entity @s armor.chest with minecraft:elytra[minecraft:custom_data={mg_ely:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du parcours","color":"aqua","italic":false}]',
    'give @s minecraft:firework_rocket[minecraft:custom_data={mg_ely:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du parcours","color":"gold","italic":false}] 3',
    'effect give @s minecraft:resistance 600 4 true',
    f'tp @s {PLAT[0]} {PLAT[1]} {PLAT[2]} facing {path[0][0]+.5} {path[0][1]} {path[0][2]+.5}',
    'playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 0.8 1.2',
    f'tellraw @s [{{"text":"🪽 Parcours d\'élytra : ","color":"aqua","bold":true}},{{"text":"saute, plane à travers les {N} anneaux dans l\'ordre (une traînée lumineuse indique le suivant). Le chrono part à l\'ouverture des élytres.","color":"gray"}}]'])
W('go', ['# Premières secondes de vol plané : le chrono démarre',
    'scoreboard players set @s mg.est 1', 'scoreboard players set @s mg.et 0',
    'title @s title [{"text":"GO !","color":"aqua","bold":true}]',
    'playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.5 1.6'])

# ---------------------------------------------------------------- player (chaque tick, @s = participant)
p = ['# Parcours d\'élytra, chaque tick (@s = joueur tagué mg.ely, positionné)',
     'execute if entity @s[tag=mg.play] run return run function mg:elytra/stop_quiet',
     'execute if entity @s[tag=mg.surv] run return run function mg:elytra/stop_quiet',
     'execute if score @s mg.est matches 0 if predicate mg:gliding run function mg:elytra/go',
     'execute if score @s mg.est matches 0 run title @s actionbar [{"text":"Saute de la plateforme et ouvre tes élytres !","color":"aqua"}]',
     'execute if score @s mg.est matches 1 run scoreboard players add @s mg.et 1',
     'execute if score @s mg.est matches 1 if predicate mg:gliding run scoreboard players set @s mg.eg 0',
     'execute if score @s mg.est matches 1 unless predicate mg:gliding run scoreboard players add @s mg.eg 1', '',
     '# Anneaux, dans l\'ordre']
for i, (x, y, z, ax) in enumerate(path, 1):
    p.append(f'execute if score @s mg.ec matches {i-1} if entity @s[x={x-2},y={y-2},z={z-2},dx=4,dy=4,dz=4] run function mg:elytra/pass')
p += [f'execute if score @s mg.ec matches {N}.. run return run function mg:elytra/finish', '',
      '# Échecs : sous le parcours, trop loin, ou posé plus de 2 s',
      'execute unless entity @s[y=118,dy=400] run return run function mg:elytra/fail',
      'execute unless entity @s[x=-76,y=-64,z=-76,dx=152,dy=500,dz=152] run return run function mg:elytra/fail',
      'execute if score @s mg.eg matches 40.. run return run function mg:elytra/fail', '',
      '# Guide lumineux vers le prochain anneau + chrono']
for i, (x, y, z, ax) in enumerate(path):
    p.append(f'execute if score @s mg.ec matches {i} run particle minecraft:end_rod {x+.5} {y+.5} {z+.5} 1 1 1 0.01 3 force @s')
p.append('execute if score @s mg.est matches 1 run function mg:elytra/hud')
W('player', p)

W('pass', ['# Anneau franchi (@s)', 'scoreboard players add @s mg.ec 1',
    'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.5',
    'particle minecraft:totem_of_undying ~ ~ ~ 0.6 0.6 0.6 0.3 15 force @s'])

TIME = '{"score":{"name":"$es","objective":"mg.st"},"color":"%s"},{"text":",","color":"%s"}'
def timeparts(col):
    return (f'{TIME % (col, col)},{{"text":"0","color":"{col}"}},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}',
            f'{TIME % (col, col)},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}')
SPLIT = ['scoreboard players operation $es mg.st = @s mg.et', 'scoreboard players operation $es mg.st /= #20 mg.st',
         'scoreboard players operation $ecs mg.st = @s mg.et', 'scoreboard players operation $ecs mg.st %= #20 mg.st',
         'scoreboard players operation $ecs mg.st *= #5 mg.st']
a, b2 = timeparts('white')
W('hud', ['# Chrono et progression (@s)'] + SPLIT + [
    f'execute if score $ecs mg.st matches ..9 run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{a},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.ec"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]',
    f'execute if score $ecs mg.st matches 10.. run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{b2},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.ec"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]'])

a, b2 = timeparts('gold')
W('finish', ['# Arrivée (@s) : temps, record perso, record du serveur'] + SPLIT + [
    'title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]',
    f'execute if score $ecs mg.st matches ..9 run tellraw @s [{{"text":"🪽 Parcours d\'élytra bouclé en ","color":"aqua"}},{a},{{"text":" s","color":"gold"}}]',
    f'execute if score $ecs mg.st matches 10.. run tellraw @s [{{"text":"🪽 Parcours d\'élytra bouclé en ","color":"aqua"}},{b2},{{"text":" s","color":"gold"}}]',
    'playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1',
    'execute unless score @s mg.erb matches 1.. run scoreboard players operation @s mg.erb = @s mg.et',
    'execute if score @s mg.et < @s mg.erb run tellraw @s [{"text":"★ Nouveau record personnel !","color":"yellow","bold":true}]',
    'execute if score @s mg.et < @s mg.erb run scoreboard players operation @s mg.erb = @s mg.et',
    'execute unless score $erec mg.st matches 1.. run scoreboard players set $erec mg.st 999999',
    f'execute if score @s mg.et < $erec mg.st if score $ecs mg.st matches ..9 run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record du parcours d\'élytra : ","color":"gray"}},{a},{{"text":" s !","color":"gold"}}]',
    f'execute if score @s mg.et < $erec mg.st if score $ecs mg.st matches 10.. run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record du parcours d\'élytra : ","color":"gray"}},{b2},{{"text":" s !","color":"gold"}}]',
    'execute if score @s mg.et < $erec mg.st run scoreboard players operation $erec mg.st = @s mg.et',
    'execute if score @s mg.et = $erec mg.st run function mg:hall/ely',
    'function mg:elytra/stop'])
W('fail', ['# Raté (@s) : retour au socle',
    'title @s actionbar [{"text":"Raté ! Remonte sur le socle pour réessayer.","color":"red"}]',
    'playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1',
    'function mg:elytra/stop'])
W('stop_quiet', ['# Fin du parcours sans téléportation (@s) : objets et effets retirés',
    'tag @s remove mg.ely', 'scoreboard players set @s mg.est 0',
    'clear @s minecraft:elytra[minecraft:custom_data~{mg_ely:1b}]',
    'clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]',
    'effect clear @s minecraft:resistance'])
W('stop', ['# Fin du parcours (@s) : retour au socle, protégé à l\'atterrissage',
    'function mg:elytra/stop_quiet',
    f'tp @s {BACK[0]} {BACK[1]} {BACK[2]} facing {PAD[0]+.5} {BACK[1]} {PAD[2]-6}',
    'effect give @s minecraft:resistance 3 4 true',
    'execute if score @s mg.ehw matches 1.. run function mg:lobby/give_wand',
    'scoreboard players set @s mg.ehw 0'])

ELYF = 'minecraft:elytra[minecraft:custom_data={mg_elyf:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du spawn","color":"white","italic":false}]'
ROCF = 'minecraft:firework_rocket[minecraft:custom_data={mg_elyf:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du spawn","color":"gold","italic":false}]'
W('free_pad', ['# Socle « élytres libres » (@s, une fois par passage) : prendre ou rendre',
    'tag @s add mg.efp',
    'execute if entity @s[tag=mg.elyf] run return run function mg:elytra/free_off',
    'tag @s add mg.elyf',
    f'item replace entity @s armor.chest with {ELYF}',
    f'give @s {ROCF} 3',
    'effect give @s minecraft:resistance 600 4 true',
    'effect give @s minecraft:levitation 2 14 true',
    'playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 0.8 1.4',
    'title @s actionbar [{"text":"🪽 Ouvre tes élytres en l\'air (Espace) — fusées illimitées. Remonte sur le socle pour les rendre.","color":"white"}]'])
W('free_tick', ['# Élytres libres, chaque tick (@s) : retirées en partie, en survie, sur un plot, en visite',
    'execute if entity @s[tag=mg.play] run return run function mg:elytra/free_stop',
    'execute if entity @s[tag=mg.surv] run return run function mg:elytra/free_stop',
    'execute if entity @s[tag=mg.inplot] run return run function mg:elytra/free_stop',
    'execute if entity @s[tag=mg.visit] run return run function mg:elytra/free_stop',
    'execute unless entity @s[gamemode=adventure] run return run function mg:elytra/free_stop',
    'execute if score $lan mg.t matches 30 run function mg:elytra/free_refill'])
W('free_refill', ['# Fusées illimitées : jamais moins de 3 (toutes les 2 s), protection renouvelée',
    'execute store result score $efn mg.st run clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}] 0',
    f'execute if score $efn mg.st matches ..2 run give @s {ROCF} 1',
    'effect give @s minecraft:resistance 600 4 true'])
W('free_off', ['# Élytres rendues sur le socle (@s)',
    'function mg:elytra/free_stop',
    'playsound minecraft:entity.item.pickup master @s ~ ~ ~ 0.8 0.8',
    'title @s actionbar [{"text":"Élytres rendues.","color":"gray"}]'])
W('free_stop', ['# Fin du vol libre (@s) : élytres et fusées retirées, courte protection à l\'atterrissage',
    'tag @s remove mg.elyf',
    'clear @s minecraft:elytra[minecraft:custom_data~{mg_elyf:1b}]',
    'clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}]',
    'effect clear @s minecraft:levitation',
    'effect clear @s minecraft:resistance',
    'effect give @s minecraft:resistance 5 4 true'])

os.makedirs(os.path.join('data', 'mg', 'predicate'), exist_ok=True)
with open(os.path.join('data', 'mg', 'predicate', 'gliding.json'), 'w', encoding='utf-8') as f:
    f.write('{\n  "condition": "minecraft:entity_properties",\n  "entity": "this",\n  "predicate": {\n    "flags": {\n      "is_flying": true\n    }\n  }\n}\n')
print(N, 'anneaux :', path)
