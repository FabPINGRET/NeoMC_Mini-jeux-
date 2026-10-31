"""Parcours d'élytra du spawn + élytres permanentes au spawn : génère data/mg/function/elytra/*.mcfunction.

Deux parcours chronométrés au-dessus de l'île, hors du volume vidé par la reconstruction
du lobby (y > 125) et loin des murs de barrières des plots :
  1. petit parcours : boucle carrée, 8 anneaux, plateforme à y 175 (4 fusées) ;
  2. grand parcours : serpentin sur 5 lignes, 15 anneaux, plateforme à y 300 (6 fusées),
     entièrement au-dessus du petit (y > 195).
Plus l'équipement permanent du spawn (tag mg.lgear, objets custom_data mg_elyf) : élytres, fusées illimitées, ⚡ Vitesse et
🐇 Super saut (bonus d'attribut tant que l'objet est en main), donnés à tout joueur en aventure au spawn et pas occupé ailleurs,
retirés dès qu'il quitte le spawn ou entre en partie, parkour, kart, parcours d'élytra... Le socle « élytres libres » n'existe plus.
Lancer depuis la racine du dépôt : python3 tools/elytra/gen_elytra.py
"""
import os

OUT = os.path.join('data', 'mg', 'function', 'elytra')
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
    1: dict(name='Petit parcours d\'élytra', short='petit', path=course1(), pad=(24, 63, 9), back=(24.5, 64, 10.5),
            plat=(-48.5, 175, -44.5), floor=118, rockets=4, pb='mg.erb', rec='$erec', hall='ely',
            lbl='🪽 Record petit parcours d\'élytra', padcol='light_blue_concrete'),
    2: dict(name='Grand parcours d\'élytra', short='grand', path=course2(), pad=(34, 63, 9), back=(34.5, 64, 10.5),
            plat=(-52.5, 300, -47.5), floor=185, rockets=6, pb='mg.erb2', rec='$erec2', hall='ely2',
            lbl='🪽 Record grand parcours d\'élytra', padcol='purple_concrete'),
}
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- construction
b = ['# Parcours d\'élytra : construction (généré par tools/elytra/gen_elytra.py)',
     'kill @e[tag=mg.elyd]', 'data modify storage mg:lobby ely4 set value 1b']
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
b += ['function mg:elytra/spawn_clean']
W('build', b)
# Abords des socles au spawn (avenue du parkour) : haie/banc/lampadaire de la bordure retirés, arbres qui masquaient les socles
# enlevés, allées pavées avenue → petit parcours → élytres libres, et avenue → grand parcours (une fois : témoin mg:lobby elyclean)
SC = ['# Accès aux socles d\'élytra depuis l\'avenue du parkour (généré par tools/elytra/gen_elytra.py)']
# anciens socles (nord) rendus à l'herbe : petit, grand, élytres libres d'avant ; anciennes allées et haie percée côté nord
for (x1, z1, x2, z2) in ((14, -11, 18, -7), (30, -17, 34, -13), (14, -23, 18, -19), (30, -12, 34, -4), (15, -18, 17, -12)):
    SC.append(f'fill {x1} 63 {z1} {x2} 63 {z2} minecraft:grass_block')
SC.append('fill 29 64 -4 35 64 -4 minecraft:azalea_leaves[persistent=true]')          # haie du nord rétablie
# nord : ancien socle des élytres libres (24, -10), sa haie percée et son allée : rendus par hub/decofix (plus construits ici) ;
# le bosquet de cerisiers ci-dessous garde sa clairière (arbres d'origine retirés)
for (x1, z1, x2, z2) in ((20, -19, 30, -7),):
    SC += [f'fill {x1} 64 {z1} {x2} 78 {z2} minecraft:air replace #minecraft:leaves', f'fill {x1} 64 {z1} {x2} 78 {z2} minecraft:air replace #minecraft:logs']
# sud (à droite de l'avenue) : petit parcours en (16, 9), grand parcours en (32, 15) ; haie percée en z 4
# sud, anciens socles (petit en (16, 9), grand en (32, 15)) et leurs allées rendus à l'herbe, haie de l'avenue refermée (z 4)
for (x1, z1, x2, z2) in ((14, 5, 18, 11), (30, 5, 31, 17), (32, 12, 34, 17)):      # sans toucher au nouveau socle (32..36, 7..11)
    SC.append(f'fill {x1} 63 {z1} {x2} 63 {z2} minecraft:grass_block')
SC += ['fill 13 64 4 16 64 4 minecraft:azalea_leaves[persistent=true]', 'fill 18 64 4 19 64 4 minecraft:azalea_leaves[persistent=true]',
       'fill 29 64 4 35 64 4 minecraft:azalea_leaves[persistent=true]']
# sud (à droite de l'avenue) : petit parcours en (24, 9), grand parcours en (34, 9), à quelques blocs de l'avenue ; haie percée en z 4
for (x1, z1, x2, z2) in ((20, 5, 28, 13), (30, 5, 39, 13)):                         # arbres entre l'avenue et les socles
    SC += [f'fill {x1} 64 {z1} {x2} 78 {z2} minecraft:air replace #minecraft:leaves', f'fill {x1} 64 {z1} {x2} 78 {z2} minecraft:air replace #minecraft:logs']
for (x1, z1, x2, z2) in ((21, 4, 27, 4), (31, 4, 36, 4)):                          # bordure de l'avenue face aux socles (lampadaire en x37 gardé)
    SC.append(f'fill {x1} 64 {z1} {x2} 72 {z2} minecraft:air')
for (x1, z1, x2, z2) in ((22, 5, 26, 6), (32, 5, 36, 6)):                          # allées pavées avenue → socles
    SC += [f'fill {x1} 64 {z1} {x2} 70 {z2} minecraft:air', f'fill {x1} 63 {z1} {x2} 63 {z2} minecraft:stone_bricks']
# ancienne balise blanche des élytres (21, 63, -15) : supprimée
SC += ['fill 20 62 -16 22 62 -14 minecraft:dirt', 'setblock 21 63 -15 minecraft:grass_block', 'setblock 21 64 -15 minecraft:air']   # trou rebouché
# bosquet de cerisiers au nord de l'avenue (hors des boîtes d'arbres coupés ci-dessus : x 20..30, z -19..-7)
for (tx, tz) in ((16, -10), (34, -10), (17, -18), (36, -17)):   # hors de la boîte d'eau de l'étang (x 22..35, z -35..-22 : theme_water)
    SC += [f'# cerisier en ({tx}, {tz})',
           f'fill {tx - 2} 67 {tz - 1} {tx + 2} 68 {tz + 1} minecraft:cherry_leaves[persistent=true]',
           f'fill {tx - 1} 67 {tz - 2} {tx + 1} 68 {tz + 2} minecraft:cherry_leaves[persistent=true]',
           f'fill {tx - 1} 69 {tz - 1} {tx + 1} 69 {tz + 1} minecraft:cherry_leaves[persistent=true]',
           f'fill {tx - 1} 70 {tz} {tx + 1} 70 {tz} minecraft:cherry_leaves[persistent=true]',
           f'fill {tx} 70 {tz - 1} {tx} 70 {tz + 1} minecraft:cherry_leaves[persistent=true]',
           f'fill {tx} 64 {tz} {tx} 68 {tz} minecraft:cherry_log']
SC.append('data modify storage mg:lobby elyclean6 set value 1b')
W('spawn_clean', SC)
def _patch(rel, anchor, line):
    pth = os.path.join('data', 'mg', 'function', rel + '.mcfunction'); t = open(pth, encoding='utf-8').read()
    if line in t: return
    assert anchor in t, (rel, anchor)
    open(pth, 'w', encoding='utf-8', newline='\n').write(t.replace(anchor, anchor + '\n' + line, 1))
_patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby ely4 run schedule function mg:elytra/build 14s',
       'execute if score $setup mg.st matches 1 unless data storage mg:lobby elyclean6 run schedule function mg:elytra/spawn_clean 9s')
_patch('desinstaller', 'data remove storage mg:lobby ely1', 'data remove storage mg:lobby ely4\ndata remove storage mg:lobby elyclean6\nschedule clear mg:elytra/spawn_clean')

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
        'execute at @s run playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 0.8 1.2',
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
    st.append(f'execute if score @s mg.ecr matches {c} run tp @s {bx} {by} {bz} facing {d["pad"][0]+.5} {by} {bz+6 if bz > 0 else bz-6}')
st += ['effect give @s minecraft:resistance 3 4 true', 'function mg:core/heal',
       'execute if score @s mg.ehw matches 1.. run function mg:lobby/give_wand',
       'scoreboard players set @s mg.ehw 0']
W('stop', st)

# ---------------------------------------------------------------- équipement permanent du spawn (élytres, fusées, vitesse, saut)
# Tag mg.lgear (PAS mg.elyf : ce tag-là compte comme « occupé » pour les portails, le duel, les emotes...). Tout objet porte
# custom_data mg_elyf : un seul clear le retire. Base des objets en main : pomme de terre empoisonnée sans nourriture ni consommation
# (aucune recette ne l'utilise : la table de craft du spawn ne peut pas s'en servir), habillée par item_model.
LOBBY_BOX = 'x=-80,y=30,z=-80,dx=160,dy=120,dz=160'                 # = theme_world.LOBBY_BOX
# Occupé ailleurs = pas d'équipement : sit_item.BUSY (partie, survie, plot, visite, parkour, kart, parcours d'élytra, duel, GTA,
# Terra Nova, Mini Party, arène PvP, ragoût) sans mg.elyf
GEAR_BUSY = ['mg.play', 'mg.out', 'mg.surv', 'mg.inplot', 'mg.visit', 'mg.pkr', 'mg.lk', 'mg.ely', 'mg.xso', 'mg.dl', 'mg.gtw',
             'mg.tvw', 'mg.mpp', 'mg.pvpc', 'mg.thbun', 'mg.thmini']
ANY = '*[minecraft:custom_data~{mg_elyf:1b}]'
ELYF = ('minecraft:elytra[minecraft:custom_data={mg_elyf:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},'
        'minecraft:attribute_modifiers=[{type:"minecraft:fall_damage_multiplier",id:"mg:lobby_fall",amount:-1,operation:"add_multiplied_total",slot:"chest"}],'
        'minecraft:custom_name={"text":"Élytres du spawn","color":"white","italic":false}]')
ROCF = 'minecraft:firework_rocket[minecraft:custom_data={mg_elyf:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du spawn","color":"gold","italic":false}]'


def held(key, model, name, col, lore, attr, op, amount):
    return ('minecraft:poisonous_potato[!minecraft:food,!minecraft:consumable,minecraft:item_model="minecraft:' + model + '",'
            'minecraft:custom_data={mg_elyf:1b,' + key + ':1b},minecraft:max_stack_size=1,minecraft:enchantment_glint_override=true,'
            f'minecraft:attribute_modifiers=[{{type:"minecraft:{attr}",id:"mg:lobby_{key}",amount:{amount},operation:"{op}",slot:"mainhand"}}],'
            'minecraft:tooltip_display={hidden_components:["minecraft:attribute_modifiers"]},'
            f'minecraft:custom_name={{"text":"{name}","color":"{col}","bold":true,"italic":false}},'
            f'minecraft:lore=[{{"text":"{lore}","color":"gray","italic":false}}]]')


SPEED = held('mg_spd', 'sugar', '⚡ Vitesse', 'yellow', 'En main : on marche (et court) deux fois plus vite',
             'movement_speed', 'add_multiplied_base', 1.0)
JUMP = held('mg_jmp', 'rabbit_foot', '🐇 Super saut', 'green', 'En main : on saute environ 4 blocs',
            'jump_strength', 'add_value', 0.4)
ROCKETS, SLOTS = 3, {'rocket': 'hotbar.5', 'speed': 'hotbar.6', 'jump': 'hotbar.7'}   # le spawn n'utilise que 0..4, emotes en 8


def give_one(item, slot, n=1):
    return [f'execute unless items entity @s {slot} * run return run item replace entity @s {slot} with {item} {n}',
            f'give @s {item} {n}']


W('gear_keep', ['# @s garde-t-il l\'équipement du spawn ? 1 ou 0 (au spawn, overworld, en aventure, pas occupé ailleurs)',
    'execute at @s unless dimension minecraft:overworld run return 0',
    f'execute unless entity @s[{LOBBY_BOX},gamemode=adventure,' + ','.join(f'tag=!{t}' for t in GEAR_BUSY) + '] run return 0',
    'return 1'])
W('gear_check', ['# @s (gear_keep vrai, toutes les 2 s) : élytres sur le dos, fusées (au moins %d), ⚡ Vitesse et 🐇 Super saut' % ROCKETS,
    'execute unless entity @s[tag=mg.lgear] run title @s actionbar [{"text":"🪽 Élytres + fusées","color":"white"},{"text":"  ⚡ Vitesse","color":"yellow"},{"text":"  🐇 Super saut","color":"green"},{"text":" : tiens l\'objet en main","color":"gray"}]',
    'tag @s add mg.lgear',
    f'execute unless items entity @s armor.chest * run item replace entity @s armor.chest with {ELYF}',
    f'execute store result score $efn mg.st run clear @s minecraft:firework_rocket[minecraft:custom_data~{{mg_elyf:1b}}] 0',
    f'execute if score $efn mg.st matches 0 run function mg:elytra/gear_rockets',
    f'execute if score $efn mg.st matches 1..{ROCKETS - 1} run give @s {ROCF} 1',
    'execute unless items entity @s container.* *[minecraft:custom_data~{mg_spd:1b}] unless items entity @s player.cursor *[minecraft:custom_data~{mg_spd:1b}] run function mg:elytra/gear_speed',
    'execute unless items entity @s container.* *[minecraft:custom_data~{mg_jmp:1b}] unless items entity @s player.cursor *[minecraft:custom_data~{mg_jmp:1b}] run function mg:elytra/gear_jump'])
W('gear_rockets', ['# @s : fusées du spawn rendues'] + give_one(ROCF, SLOTS['rocket'], ROCKETS))
W('gear_speed', ['# @s : objet ⚡ Vitesse rendu'] + give_one(SPEED, SLOTS['speed']))
W('gear_jump', ['# @s : objet 🐇 Super saut rendu'] + give_one(JUMP, SLOTS['jump']))
W('gear_second', ['# Toutes les 2 s (core/tick) : équipement du spawn rendu à qui le garde, objets jetés au sol détruits',
    f'execute as @e[type=minecraft:item] if items entity @s contents {ANY} run kill @s',
    'execute as @a[gamemode=adventure] if function mg:elytra/gear_keep run function mg:elytra/gear_check'])
W('gear_tick', ['# Chaque tick (@s = mg.lgear) : équipement retiré dès qu\'il quitte le spawn ou s\'occupe ailleurs ; protégé en vol plané',
    'execute unless function mg:elytra/gear_keep run return run function mg:elytra/free_stop',
    'execute if predicate mg:gliding run effect give @s minecraft:resistance 2 4 true'])
W('free_stop', ['# Fin de l\'équipement du spawn (@s) : élytres, fusées, ⚡ Vitesse et 🐇 Super saut retirés (appelé aussi à chaque entrée en jeu)',
    'tag @s remove mg.lgear',
    'tag @s remove mg.elyf',
    f'clear @s {ANY}'])
TICK_ELY = [
    '# Parcours d\'élytra : socle de départ, joueurs en vol (généré par tools/elytra/gen_elytra.py)']
for c, d in C.items():
    px, py, pz = d['pad']
    TICK_ELY.append(f'execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.ely,tag=!mg.pkr,gamemode=adventure,'
                    f'x={px},y={py},z={pz},dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/{"start" if c == 1 else f"start{c}"}')
TICK_ELY += ['execute as @a[tag=mg.ely] at @s run function mg:elytra/player',
             '# Équipement permanent du spawn : élytres, fusées, vitesse, saut (gen_elytra.py)',
             'execute as @a[tag=mg.lgear] run function mg:elytra/gear_tick',
             'execute if score $setup mg.st matches 1 if score $lan mg.t matches 30 run function mg:elytra/gear_second',
             f'execute if score $lan mg.t matches 20 run clear @a[tag=!mg.lgear] {ANY}']
_tp = os.path.join('data', 'mg', 'function', 'core', 'tick.mcfunction')
_tl = open(_tp, encoding='utf-8').read().split('\n')
_i = next(k for k, l in enumerate(_tl) if l.startswith('# Parcours d\'élytra : socle de départ'))
_j = _i + 1
while _j < len(_tl) and ('elytra/' in _tl[_j] or 'mg_elyf' in _tl[_j] or 'mg.efp' in _tl[_j] or _tl[_j].startswith('# Élytres libres')
                         or _tl[_j].startswith('# Équipement permanent du spawn')):
    _j += 1
_tl[_i:_j] = TICK_ELY
open(_tp, 'w', encoding='utf-8', newline='\n').write('\n'.join(_tl))
_patch('desinstaller', 'tag @a remove mg.elyf', f'clear @a {ANY}\ntag @a remove mg.lgear')

# anciens fichiers du premier générateur (un seul parcours)
for old in ('hud', 'finish', 'free_pad', 'free_off', 'free_tick', 'free_refill'):   # + anciennes « élytres libres »
    p = os.path.join(OUT, old + '.mcfunction')
    if os.path.exists(p): os.remove(p)

os.makedirs(os.path.join('data', 'mg', 'predicate'), exist_ok=True)
with open(os.path.join('data', 'mg', 'predicate', 'gliding.json'), 'w', encoding='utf-8') as f:
    f.write('{\n  "condition": "minecraft:entity_properties",\n  "entity": "this",\n  "predicate": {\n    "flags": {\n      "is_flying": true\n    }\n  }\n}\n')
for c, d in C.items():
    print(c, len(d['path']), 'anneaux', d['path'][0], '→', d['path'][-1])
