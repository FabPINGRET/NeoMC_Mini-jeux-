"""Parcours d'élytra du spawn + élytres libres : génère data/mg/function/elytra/*.mcfunction.

Deux parcours chronométrés au-dessus de l'île, hors du volume vidé par la reconstruction
du lobby (y > 125) et loin des murs de barrières des plots :
  1. petit parcours : boucle carrée, 8 anneaux, plateforme à y 175 (4 fusées) ;
  2. grand parcours : serpentin sur 5 lignes, 15 anneaux, plateforme à y 300 (6 fusées),
     entièrement au-dessus du petit (y > 195).
Plus un socle « élytres libres » (vol autour du spawn, fusées illimitées).
Lancer depuis la racine du dépôt : python3 tools/elytra/gen_elytra.py
"""
import os

OUT = os.path.join('data', 'mg', 'function', 'elytra')
FREE = (16, 63, -21)                  # socle « élytres libres »
DISP = 'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[%sf,%sf,%sf]}'
COL = ['light_blue', 'magenta', 'lime', 'orange']

def W(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

# ---------------------------------------------------------------- tracés
def course1():
    H, Y0, Y1, path = 45, 172, 132, []
    for side in range(4):
        for k in (30, 60):
            s = side * 90 + k
            if side == 0:   x, z, ax = -H + k, -H, 'x'
            elif side == 1: x, z, ax = H, -H + k, 'z'
            elif side == 2: x, z, ax = H - k, H, 'x'
            else:           x, z, ax = -H, H - k, 'z'
            path.append((x, round(Y0 - s * (Y0 - Y1) / 360), z, ax))
    return path

def course2():
    path, i = [], 0
    for row, z in enumerate((-48, -24, 0, 24, 48)):
        xs = (-30, 0, 30) if row % 2 == 0 else (30, 0, -30)
        for x in xs:
            path.append((x, round(292 - i * 6.5), z, 'x'))
            i += 1
    return path

C = {
    1: dict(name='Petit parcours d\'élytra', short='petit', path=course1(), pad=(16, 63, -9), back=(16.5, 64, -10.5),
            plat=(-48.5, 175, -44.5), floor=118, rockets=4, pb='mg.erb', rec='$erec', hall='ely',
            lbl='🪽 Record petit parcours d\'élytra', padcol='light_blue_concrete'),
    2: dict(name='Grand parcours d\'élytra', short='grand', path=course2(), pad=(32, 63, -15), back=(32.5, 64, -16.5),
            plat=(-52.5, 300, -47.5), floor=185, rockets=6, pb='mg.erb2', rec='$erec2', hall='ely2',
            lbl='🪽 Record grand parcours d\'élytra', padcol='purple_concrete'),
}
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- construction
b = ['# Parcours d\'élytra et élytres libres : construction (généré par tools/elytra/gen_elytra.py)',
     'kill @e[tag=mg.elyd]', 'data modify storage mg:lobby ely1 set value 1b']
def pad(p, col, title, sub, tcol):
    px, py, pz = p
    return [f'fill {px-2} {py} {pz-2} {px+2} {py} {pz+2} minecraft:smooth_quartz',
            f'fill {px-1} {py} {pz-1} {px+1} {py} {pz+1} minecraft:{col}',
            f'setblock {px} {py} {pz} minecraft:sea_lantern',
            f'summon minecraft:item_display {px+.5} {py+3} {pz+.5} {{Tags:["mg.elyd","mg.lspin","mg.lbob"],billboard:"fixed",item:{{id:"minecraft:elytra"}},{DISP % (1.4, 1.4, 1.4)}}}',
            f'summon minecraft:text_display {px+.5} {py+4.8} {pz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"{title}","color":"{tcol}","bold":true}}],{DISP % (1.2, 1.2, 1.2)}}}',
            f'summon minecraft:text_display {px+.5} {py+4.3} {pz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"{sub}","color":"gray"}}],{DISP % (0.7, 0.7, 0.7)}}}']
for c, d in C.items():
    path, N = d['path'], len(d['path'])
    b += ['', f'# ===== {d["name"]} ({N} anneaux)']
    b += pad(d['pad'], d['padcol'], f'🪽 {d["name"]}', f'{N} anneaux chronométrés — monte au centre du socle', 'aqua' if c == 1 else 'light_purple')
    qx, qy, qz = int(d['plat'][0] - .5), d['plat'][1] - 1, int(d['plat'][2] - .5)
    b += [f'fill {qx-2} {qy} {qz-2} {qx+2} {qy} {qz+2} minecraft:smooth_quartz',
          f'fill {qx-2} {qy} {qz-2} {qx-2} {qy+1} {qz+2} minecraft:light_blue_stained_glass',
          f'setblock {qx-2} {qy+2} {qz} minecraft:sea_lantern',
          f'summon minecraft:text_display {qx+.5} {qy+3.5} {qz+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"Saute vers l\'est, ouvre tes élytres (Espace en l\'air)","color":"yellow"}},{{"text":"\\n{N} anneaux dans l\'ordre — {d["rockets"]} fusées pour t\'aider","color":"gray"}}],{DISP % (0.8, 0.8, 0.8)}}}']
    for i, (x, y, z, ax) in enumerate(path, 1):
        blk = 'minecraft:gold_block' if i == N else f'minecraft:{COL[(i-1) % 4]}_concrete'
        if ax == 'x':
            b += [f'fill {x} {y-3} {z-3} {x} {y+3} {z+3} {blk}', f'fill {x} {y-2} {z-2} {x} {y+2} {z+2} minecraft:air']
            corners = [(x, y-3, z-3), (x, y-3, z+3), (x, y+3, z-3), (x, y+3, z+3)]
        else:
            b += [f'fill {x-3} {y-3} {z} {x+3} {y+3} {z} {blk}', f'fill {x-2} {y-2} {z} {x+2} {y+2} {z} minecraft:air']
            corners = [(x-3, y-3, z), (x+3, y-3, z), (x-3, y+3, z), (x+3, y+3, z)]
        b += [f'setblock {cx} {cy} {cz} minecraft:sea_lantern' for cx, cy, cz in corners]
        label = f'{i}' if i < N else '🏁'
        b.append(f'summon minecraft:text_display {x+.5} {y+4.2} {z+.5} {{Tags:["mg.elyd"],billboard:"center",background:0,text:[{{"text":"{label}","color":"white","bold":true}}],{DISP % (2, 2, 2)}}}')
b += ['', '# ===== Élytres libres'] + pad(FREE, 'white_concrete', '🪽 Élytres libres', 'Vol autour du spawn, fusées illimitées — remonte dessus pour les rendre', 'white')
b += ['function mg:elytra/spawn_clean']
W('build', b)
# Abords des socles au spawn (avenue du parkour) : haie/banc/lampadaire de la bordure retirés, arbres qui masquaient les socles
# enlevés, allées pavées avenue → petit parcours → élytres libres, et avenue → grand parcours (une fois : témoin mg:lobby elyclean)
SC = ['# Accès dégagés aux socles d\'élytra depuis l\'avenue du parkour (généré par tools/elytra/gen_elytra.py)']
for (x1, z1, x2, z2) in ((12, -19, 22, -11), (28, -13, 37, -5)):        # arbres entre l'avenue et les socles
    SC += [f'fill {x1} 64 {z1} {x2} 78 {z2} minecraft:air replace #minecraft:leaves', f'fill {x1} 64 {z1} {x2} 78 {z2} minecraft:air replace #minecraft:logs']
for (x1, z1, x2, z2) in ((13, -4, 19, -4), (29, -4, 35, -4)):          # bordure de l'avenue face aux socles
    SC.append(f'fill {x1} 64 {z1} {x2} 72 {z2} minecraft:air')
for (x1, z1, x2, z2) in ((14, -6, 18, -4), (15, -18, 17, -12), (30, -12, 34, -4)):   # allées
    SC += [f'fill {x1} 64 {z1} {x2} 70 {z2} minecraft:air', f'fill {x1} 63 {z1} {x2} 63 {z2} minecraft:stone_bricks']
SC.append('data modify storage mg:lobby elyclean set value 1b')
W('spawn_clean', SC)
def _patch(rel, anchor, line):
    pth = os.path.join('data', 'mg', 'function', rel + '.mcfunction'); t = open(pth, encoding='utf-8').read()
    if line in t: return
    assert anchor in t, (rel, anchor)
    open(pth, 'w', encoding='utf-8', newline='\n').write(t.replace(anchor, anchor + '\n' + line, 1))
_patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby ely1 run schedule function mg:elytra/build 14s',
       'execute if score $setup mg.st matches 1 unless data storage mg:lobby elyclean run schedule function mg:elytra/spawn_clean 9s')
_patch('desinstaller', 'data remove storage mg:lobby ely1', 'data remove storage mg:lobby elyclean\nschedule clear mg:elytra/spawn_clean')

# ---------------------------------------------------------------- départ (start = petit, start2 = grand)
for c, d in C.items():
    N, p0 = len(d['path']), d['path'][0]
    W('start' if c == 1 else f'start{c}', [f'# Départ du {d["name"].lower()} (@s = joueur sur le socle)',
        'execute if entity @s[tag=mg.elyf] run function mg:elytra/free_stop',
        '# Pas de baguette feu d\'artifice ni de charges de vent pendant la course (rendue à la fin)',
        'execute store result score @s mg.ehw run clear @s minecraft:blaze_rod',
        'clear @s minecraft:wind_charge',
        'tag @s add mg.ely',
        f'scoreboard players set @s mg.ecr {c}',
        'scoreboard players set @s mg.est 0', 'scoreboard players set @s mg.ec 0',
        'scoreboard players set @s mg.et 0', 'scoreboard players set @s mg.eg 0',
        'scoreboard players set #20 mg.st 20', 'scoreboard players set #5 mg.st 5',
        'item replace entity @s armor.chest with minecraft:elytra[minecraft:custom_data={mg_ely:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du parcours","color":"aqua","italic":false}]',
        f'give @s minecraft:firework_rocket[minecraft:custom_data={{mg_ely:1b}},minecraft:fireworks={{flight_duration:1}},minecraft:custom_name={{"text":"Fusée du parcours","color":"gold","italic":false}}] {d["rockets"]}',
        'effect give @s minecraft:resistance 600 4 true', 'function mg:core/heal',
        f'tp @s {d["plat"][0]} {d["plat"][1]} {d["plat"][2]} facing {p0[0]+.5} {p0[1]} {p0[2]+.5}',
        'playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 0.8 1.2',
        f'tellraw @s [{{"text":"🪽 {d["name"]} : ","color":"aqua","bold":true}},{{"text":"saute, plane à travers les {N} anneaux dans l\'ordre (une traînée lumineuse indique le suivant). Le chrono part à l\'ouverture des élytres. {d["rockets"]} fusées.","color":"gray"}}]'])
W('go', ['# Premières secondes de vol plané : le chrono démarre',
    'scoreboard players set @s mg.est 1', 'scoreboard players set @s mg.et 0',
    'title @s title [{"text":"GO !","color":"aqua","bold":true}]',
    'playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.5 1.6'])

# ---------------------------------------------------------------- chaque tick
W('player', ['# Parcours d\'élytra, chaque tick (@s = joueur tagué mg.ely, positionné)',
    'execute if entity @s[tag=mg.play] run return run function mg:elytra/stop_quiet',
    'execute if entity @s[tag=mg.surv] run return run function mg:elytra/stop_quiet',
    'execute unless score @s mg.ecr matches 1..2 run scoreboard players set @s mg.ecr 1',
    'execute if score @s mg.est matches 0 if predicate mg:gliding run function mg:elytra/go',
    'execute if score @s mg.est matches 0 run title @s actionbar [{"text":"Saute de la plateforme et ouvre tes élytres !","color":"aqua"}]',
    'execute if score @s mg.est matches 1 run scoreboard players add @s mg.et 1',
    'execute if score @s mg.est matches 1 if predicate mg:gliding run scoreboard players set @s mg.eg 0',
    'execute if score @s mg.est matches 1 unless predicate mg:gliding run scoreboard players add @s mg.eg 1',
    'execute if score @s mg.ecr matches 1 run return run function mg:elytra/rings1',
    'execute if score @s mg.ecr matches 2 run return run function mg:elytra/rings2'])

SPLIT = ['scoreboard players operation $es mg.st = @s mg.et', 'scoreboard players operation $es mg.st /= #20 mg.st',
         'scoreboard players operation $ecs mg.st = @s mg.et', 'scoreboard players operation $ecs mg.st %= #20 mg.st',
         'scoreboard players operation $ecs mg.st *= #5 mg.st']
TIME = '{"score":{"name":"$es","objective":"mg.st"},"color":"%s"},{"text":",","color":"%s"}'
def timeparts(col):
    return (f'{TIME % (col, col)},{{"text":"0","color":"{col}"}},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}',
            f'{TIME % (col, col)},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}')

for c, d in C.items():
    path, N = d['path'], len(d['path'])
    r = [f'# {d["name"]} : anneaux, échecs, guide, chrono (@s)']
    for i, (x, y, z, ax) in enumerate(path, 1):
        r.append(f'execute if score @s mg.ec matches {i-1} if entity @s[x={x-2},y={y-2},z={z-2},dx=4,dy=4,dz=4] run function mg:elytra/pass')
    r += [f'execute if score @s mg.ec matches {N}.. run return run function mg:elytra/finish{c}',
          f'execute unless entity @s[y={d["floor"]},dy=400] run return run function mg:elytra/fail',
          'execute unless entity @s[x=-76,y=-64,z=-76,dx=152,dy=500,dz=152] run return run function mg:elytra/fail',
          'execute if score @s mg.eg matches 40.. run return run function mg:elytra/fail']
    for i, (x, y, z, ax) in enumerate(path):
        r.append(f'execute if score @s mg.ec matches {i} run particle minecraft:end_rod {x+.5} {y+.5} {z+.5} 1 1 1 0.01 3 force @s')
    r.append(f'execute if score @s mg.est matches 1 run function mg:elytra/hud{c}')
    W(f'rings{c}', r)

    a, b2 = timeparts('white')
    W(f'hud{c}', ['# Chrono et progression (@s)'] + SPLIT + [
        f'execute if score $ecs mg.st matches ..9 run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{a},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.ec"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]',
        f'execute if score $ecs mg.st matches 10.. run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{b2},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.ec"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]'])

    a, b2 = timeparts('gold')
    pb, rec, nm = d['pb'], d['rec'], d['name'].lower()
    W(f'finish{c}', [f'# Arrivée du {nm} (@s) : temps, record perso, record du serveur'] + SPLIT + [
        'title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]',
        f'execute if score $ecs mg.st matches ..9 run tellraw @s [{{"text":"🪽 {d["name"]} bouclé en ","color":"aqua"}},{a},{{"text":" s","color":"gold"}}]',
        f'execute if score $ecs mg.st matches 10.. run tellraw @s [{{"text":"🪽 {d["name"]} bouclé en ","color":"aqua"}},{b2},{{"text":" s","color":"gold"}}]',
        'playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1',
        f'execute unless score @s {pb} matches 1.. run scoreboard players operation @s {pb} = @s mg.et',
        f'execute if score @s mg.et < @s {pb} run tellraw @s [{{"text":"★ Nouveau record personnel !","color":"yellow","bold":true}}]',
        f'execute if score @s mg.et < @s {pb} run scoreboard players operation @s {pb} = @s mg.et',
        f'execute unless score {rec} mg.st matches 1.. run scoreboard players set {rec} mg.st 999999',
        f'execute if score @s mg.et < {rec} mg.st if score $ecs mg.st matches ..9 run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record du {nm} : ","color":"gray"}},{a},{{"text":" s !","color":"gold"}}]',
        f'execute if score @s mg.et < {rec} mg.st if score $ecs mg.st matches 10.. run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record du {nm} : ","color":"gray"}},{b2},{{"text":" s !","color":"gold"}}]',
        f'execute if score @s mg.et < {rec} mg.st run scoreboard players operation {rec} mg.st = @s mg.et',
        f'execute if score @s mg.et = {rec} mg.st run function mg:hall/ely {{key:"{d["hall"]}",lbl:"{d["lbl"]}"}}',
        'function mg:elytra/stop'])

W('pass', ['# Anneau franchi (@s)', 'scoreboard players add @s mg.ec 1',
    'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.5',
    'particle minecraft:totem_of_undying ~ ~ ~ 0.6 0.6 0.6 0.3 15 force @s'])
W('fail', ['# Raté (@s) : retour au socle',
    'title @s actionbar [{"text":"Raté ! Remonte sur le socle pour réessayer.","color":"red"}]',
    'playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1',
    'function mg:elytra/stop'])
W('stop_quiet', ['# Fin du parcours sans téléportation (@s) : objets et effets retirés',
    'tag @s remove mg.ely', 'scoreboard players set @s mg.est 0',
    'clear @s minecraft:elytra[minecraft:custom_data~{mg_ely:1b}]',
    'clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]',
    'effect clear @s minecraft:resistance'])
st = ['# Fin du parcours (@s) : retour à son socle, protégé à l\'atterrissage, baguette rendue',
      'function mg:elytra/stop_quiet']
for c, d in C.items():
    bx, by, bz = d['back']
    st.append(f'execute if score @s mg.ecr matches {c} run tp @s {bx} {by} {bz} facing {d["pad"][0]+.5} {by} {bz-6}')
st += ['effect give @s minecraft:resistance 3 4 true', 'function mg:core/heal',
       'execute if score @s mg.ehw matches 1.. run function mg:lobby/give_wand',
       'scoreboard players set @s mg.ehw 0']
W('stop', st)

# ---------------------------------------------------------------- élytres libres
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

# anciens fichiers du premier générateur (un seul parcours)
for old in ('hud', 'finish'):
    p = os.path.join(OUT, old + '.mcfunction')
    if os.path.exists(p): os.remove(p)

os.makedirs(os.path.join('data', 'mg', 'predicate'), exist_ok=True)
with open(os.path.join('data', 'mg', 'predicate', 'gliding.json'), 'w', encoding='utf-8') as f:
    f.write('{\n  "condition": "minecraft:entity_properties",\n  "entity": "this",\n  "predicate": {\n    "flags": {\n      "is_flying": true\n    }\n  }\n}\n')
for c, d in C.items():
    print(c, len(d['path']), 'anneaux', d['path'][0], '→', d['path'][-1])
