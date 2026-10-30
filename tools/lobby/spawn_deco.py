# Spawn : entités de décor, tick de l'armurerie et fonctions du parkour ; exécuté par gen_lobby.py (exec) après l'émission des commandes de construction.
# Utilise : CPS, F, FIN, FINY, JETS, PADS, PIPES, PK, S1, W, get, is_conn, math, merge, os, path, rnd, spiral, wr

# ------------------------------------------------------------------ entités de décor
TF = 'transformation:{{translation:[0f,{ty}f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[{s}f,{s}f,{s}f]}}'
def face_spawn(x, z):
    # orientation fixe du panneau, face lisible tournée vers le centre de la place (opposé du regard d'un joueur au centre)
    return round((math.degrees(math.atan2(-(x - 0.5), z - 0.5)) + 360) % 360 - 180, 1)
def tdisp(x, y, z, text, s, tags='', bill='vertical', yaw=None):
    rot = '' if yaw is None else f'Rotation:[{yaw}f,0f],'
    if yaw is not None: bill = 'fixed'
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.lby"{tags}],billboard:"{bill}",{rot}background:0,text:{text},'
            + TF.format(ty=0, s=s) + '}')
def idisp(x, y, z, item, s, tags='', bill='fixed', yaw=0, extra=''):
    return (f'summon minecraft:item_display {x} {y} {z} {{Tags:["mg.lby"{tags}],billboard:"{bill}",Rotation:[{yaw}f,0f],item:{item},'
            + TF.format(ty=0, s=s) + extra + '}')
def rp(model, base='minecraft:paper', color=None):
    comp = f'"minecraft:item_model":"mg:{model}"' + (f',"minecraft:dyed_color":{color}' if color is not None else '')
    return f'{{id:"{base}",components:{{{comp}}}}}'
def vi(i): return f'{{id:"minecraft:{i}"}}'
SPIN, BOB, BOTH = ',"mg.lspin"', ',"mg.lbob"', ',"mg.lspin","mg.lbob"'
G_ = lambda c: '{"text":"' + c + '","font":"mg:lobby"}'
SIGNS = [  # glyphe, texte vanilla, position, échelle rp, échelle vanilla
    ('', '[{"text":"✦ NEOMC ✦","color":"gold","bold":true},{"text":"\\nMINI-JEUX","color":"aqua","bold":true}]', (0.5, 72.5, 17.5), 4, 5),
    ('', '[{"text":"⚔ ARMURERIE ⚔","color":"gold","bold":true}]', (-33.3, 74, 0.5), 3.4, 3),
    ('', '[{"text":"◎ STAND DE TIR ◎","color":"red","bold":true}]', (-46.5, 72.5, -33.2), 2.6, 2.4),
    ('', '[{"text":"⚑ PARKOUR ⚑","color":"green","bold":true}]', (64.5, 75, 0.5), 3.2, 3),
    ('', '[{"text":"🏁 GARAGE KART 🏁","color":"red","bold":true}]', (0.5, 75, 36.5), 3.2, 3),
    ('', '[{"text":"★ ARRIVÉE ★","color":"aqua","bold":true}]', (FIN[0], FIN[1] + 5, FIN[2]), 3.4, 3),
]
HINTS = [
    ('[{"text":"Marche sur un socle pour t\'équiper !","color":"gray"}]', (-33.3, 69.4, 0.5), 1.3),
    ('[{"text":"Le railgun marque les points : vise le cœur des cibles !","color":"gray"}]', (-46.5, 71.6, -33.2), 1.1),
    ('[{"text":"Bienvenue ! ","color":"yellow","bold":true},{"text":"⚔ Armurerie à l\'ouest, ⚑ Parkour à l\'est, ◈ Portails au nord, 🏁 Kart au sud","color":"gray"}]', (0.5, 70.2, 17.5), 1.2),
]
common = ['# Décor commun (rp ou vanilla)']
for (t, pos, s) in HINTS: common.append(tdisp(*pos, t, s, yaw=face_spawn(pos[0], pos[2])))
for (z, it) in ((-5, 'iron_sword'), (-3, 'bow'), (-1, 'trident'), (1, 'crossbow'), (3, 'mace'), (5, 'diamond_sword')):
    common.append(idisp(-56.4, 67.2, z + 0.5, vi(it), 1.3, yaw=90).replace('left_rotation:[0f,0f,0f,1f]', 'left_rotation:[0f,0f,0.3827f,0.9239f]'))
for (x, z, yaw, set_) in ((-55.5, -3.5, -90, 'iron'), (-55.5, 4.5, -90, 'diamond'), (-37.5, 9.5, 180, 'golden'), (-37.5, -8.5, 0, 'netherite')):
    common.append(f'summon minecraft:armor_stand {x} 64 {z} {{Tags:["mg.lby"],Invulnerable:1b,NoGravity:1b,ShowArms:1b,DisabledSlots:4144959,Rotation:[{yaw}f,0f],'
                  f'equipment:{{head:{{id:"minecraft:{set_}_helmet"}},chest:{{id:"minecraft:{set_}_chestplate"}},legs:{{id:"minecraft:{set_}_leggings"}},'
                  f'feet:{{id:"minecraft:{set_}_boots"}},mainhand:{{id:"minecraft:{set_}_sword"}}}}}}')
rpl, vnl = ['# Décor du resource pack (modèles mg:*)'], ['# Décor vanilla (sans resource pack)']
for (g, txt, pos, s1, s2) in SIGNS:
    yaw = None if pos == (FIN[0], FIN[1] + 5, FIN[2]) else face_spawn(pos[0], pos[2])   # ARRIVÉE (haut du parkour) : reste tournante
    rpl.append(tdisp(*pos, G_(g), s1, yaw=yaw)); vnl.append(tdisp(*pos, txt, s2, yaw=yaw))
# boîtes ? en couronne au-dessus du point d'apparition + étoile
for k in range(8):
    a = math.radians(45 * k)
    rpl.append(idisp(round(0.5 + 3.6 * math.cos(a), 2), 69.5, round(0.5 + 3.6 * math.sin(a), 2), rp('item_box'), 0.9, BOTH))
rpl.append(idisp(0.5, 70.6, 0.5, rp('star'), 2.6, BOB, bill='vertical'))
vnl.append(idisp(0.5, 70.6, 0.5, vi('nether_star'), 2.2, BOB, bill='vertical'))
# ballons autour de la place
COLS = [16711680, 3368703, 16766720, 6750054, 16738740, 10053375]
for k in range(4):
    a = math.radians(45 + 90 * k); cx, cz = 11.6 * math.cos(a) + 0.5, 11.6 * math.sin(a) + 0.5
    for j in range(3):
        rpl.append(idisp(round(cx + (j - 1) * 0.7, 2), 66.6 + (j % 2) * 0.8, round(cz + (1 - j) * 0.5, 2),
                         rp('balloon', 'minecraft:leather_horse_armor', COLS[(k + j) % 6]), 1.3, BOB))
# garage : karts sur le podium et sur la piste, boîtes ?, tuyaux, Thwomp, Goombas
KC = [15022389, 2712319, 6610199, 16766720, 9315498, 16739584]
for (x, y, m, c) in ((0.5, 67, 'kart_bolide', KC[0]), (-2.5, 66, 'kart', KC[1]), (3.5, 65, 'kart_costaud', KC[2])):
    # le modèle est centré sur l'entité : on le remonte de la moitié de sa taille pour qu'il soit posé sur le podium
    rpl.append(idisp(x, round(y + 0.5 * 1.4 + 0.02, 2), 48.5, rp(m, 'minecraft:leather_horse_armor', c), 1.4, SPIN))
    vnl.append(idisp(x, round(y + 0.5 * 1.2 + 0.02, 2), 48.5, vi('minecart'), 1.2, SPIN))
for k, ang in enumerate((40, 160, 280)):
    a = math.radians(ang); x, z = 8.5 * math.cos(a) + 0.5, 48.5 + 8.5 * math.sin(a)
    yaw = (math.degrees(math.atan2(-math.cos(a + math.pi / 2), math.sin(a + math.pi / 2)))) % 360
    rpl.append(idisp(round(x, 2), round(64 + 0.5 * 1.1 + 0.02, 2), round(z, 2), rp(['kart_mini', 'kart', 'kart_bolide'][k], 'minecraft:leather_horse_armor', KC[3 + k]), 1.1, yaw=round(yaw, 1)))
for x in (-4.5, -1.5, 1.5, 4.5):
    rpl.append(idisp(x + 0.5, 74, 36.5, rp('item_box'), 1.0, BOTH))
for (cx, cz) in PIPES: rpl.append(idisp(cx + 0.5, 68.2, cz + 0.5, rp('piranha'), 1.3, BOB, yaw=rnd.choice((0, 90, 180, 270))))
rpl.append(idisp(0.5, 75.5, 48.5, rp('thwomp'), 3.0, BOB))
for (x, z, yaw) in ((-11.5, 47.5, 90), (10.5, 52.5, -90), (-4.5, 59.5, 180)):
    rpl.append(idisp(x, 64.55, z, rp('goomba'), 1.1, yaw=yaw))
# parkour : trophée et cristaux au sommet de la tour, cristaux du portail
rpl.append(idisp(FIN[0], FIN[1] + 1.6, FIN[2], rp('trophy'), 2.4, BOTH))
vnl.append(idisp(FIN[0], FIN[1] + 1.6, FIN[2], vi('gold_block'), 1.0, BOTH))
for k, c in enumerate((6740479, 16738740, 8453888, 16766720)):
    a = math.radians(45 + 90 * k)
    rpl.append(idisp(round(FIN[0] + 7 * math.cos(a), 2), FIN[1] + 3, round(FIN[2] + 7 * math.sin(a), 2), rp('crystal', 'minecraft:leather_horse_armor', c), 2.2, BOTH))
# boîtes ? au-dessus des jardins aux champignons
for (x, y, z) in ((24.5, 72, 22.5), (30.5, 74, 30.5), (20.5, 73, 36.5), (38.5, 71, 20.5)):
    rpl.append(idisp(x, y, z, rp('item_box'), 1.2, BOTH))
wr('lobby/deco', ['# Décor du spawn (entités mg.lby) : modèles du resource pack si $rp = 1, sinon vanilla (généré)',
                  'kill @e[tag=mg.lby]', 'kill @e[type=minecraft:text_display,tag=mg.deco]', 'function mg:lobby/deco_common',
                  'execute if score $rp mg.st matches 1 run function mg:lobby/deco_rp',
                  'execute unless score $rp mg.st matches 1 run function mg:lobby/deco_vn',
                  'data modify storage mg:lobby deco3 set value 1b'])
wr('lobby/deco_common', common)
wr('lobby/deco_rp', rpl)
wr('lobby/deco_vn', vnl)

# animation (toutes les 2 s) et ambiance (toutes les 0,5 s)
Q = ['[0f,0f,0f,1f]', '[0f,0.7071f,0f,0.7071f]', '[0f,1f,0f,0f]', '[0f,0.7071f,0f,-0.7071f]']
anim = ['# Décor du spawn : rotation (mg.lspin) et flottement (mg.lbob), interpolés sur 2 s',
        'scoreboard players add $lph mg.st 1', 'execute if score $lph mg.st matches 4.. run scoreboard players set $lph mg.st 0',
        'execute as @e[type=minecraft:item_display,tag=mg.lby] run data merge entity @s {start_interpolation:0,interpolation_duration:40}']
for i in range(4):
    anim.append(f'execute if score $lph mg.st matches {i} as @e[type=minecraft:item_display,tag=mg.lspin] run data modify entity @s transformation.left_rotation set value {Q[(i + 1) % 4]}')
anim.append('execute if score $lph mg.st matches 0..3 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0f,0f]')
anim.append('execute if score $lph mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0.35f,0f]')
anim.append('execute if score $lph mg.st matches 2 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0.35f,0f]')
wr('lobby/anim', anim)
fx = ['# Ambiance du spawn (particules)',
      'particle minecraft:end_rod 67.5 64.3 0.5 1.2 0.2 1.2 0.01 2',
      f'particle minecraft:end_rod {FIN[0]} {FIN[1] + 2} {FIN[2]} 3 1.5 3 0.01 3',
      'particle minecraft:cherry_leaves 30 72 -30 12 5 12 0 4',
      'particle minecraft:cherry_leaves 31 88 -31 4 1 4 0 2',
      'particle minecraft:glow 0.5 66 0.5 6 0.6 6 0 3',
      'particle minecraft:falling_water 0.5 67 0.5 7 0.5 7 0 4',
      'particle minecraft:wax_on 0.5 70 0.5 3.5 0.6 3.5 0 2']
for (x, y, z) in JETS[:4]: fx.append(f'particle minecraft:splash {x + 0.5} 64 {z + 0.5} 0.8 0.1 0.8 0 6')
wr('lobby/fx', fx)

# ------------------------------------------------------------------ armurerie : socles, tick, armes avec le resource pack
PADM = [('warped_fungus_on_a_stick', 'laser_gun', '⚡ Railgun', 'red'), ('blaze_rod', 'magic_wand', '✦ Baguette feu d\'artifice', 'gold'),
        ('wind_charge', 'wind_orb', '☁ Lance-vent', 'aqua'), ('snowball', 'snow_orb', '❄ Lance-neige', 'white')]
ab = ['# Armurerie du spawn : armes au-dessus des socles (généré par tools/lobby/gen_lobby.py)', 'kill @e[tag=mg.arm]']
for (px, pz, c), (it, mdl, name, col) in zip(PADS, PADM):
    cx, cz = px + 1.5, pz + 1.5
    item = f'{{id:"minecraft:{it}"}}'
    for tag, itm in (('rp', rp(mdl, f'minecraft:{it}')), ('vn', item)):
        cond = 'execute if score $rp mg.st matches 1 run ' if tag == 'rp' else 'execute unless score $rp mg.st matches 1 run '
        ab.append(cond + f'summon minecraft:item_display {cx} 65.6 {cz} {{Tags:["mg.arm","mg.lspin","mg.lbob"],billboard:"fixed",item:{itm},' + TF.format(ty=0, s=1.4) + '}')
    ab.append(f'summon minecraft:text_display {cx} 67.2 {cz} {{Tags:["mg.arm"],billboard:"center",background:0,text:[{{"text":"{name}","color":"{col}","bold":true}}],'
              + TF.format(ty=0, s=1.0) + '}')
# grande carte du lobby (modèle mg:lobby_map, tools/resourcepack/lobbymap_rp.py) : disque de 11 blocs contre le mur ouest (x -57), au-dessus du panneau d'armes
MAP_C, MAP_D = (-55.97, 75.5, 0.5), 11
for my, mz in ((y, z) for y in range(70, 82) for z in range(-5, 7)):
    if math.hypot(max(my - MAP_C[1], MAP_C[1] - my - 1, 0), max(mz - MAP_C[2], MAP_C[2] - mz - 1, 0)) < MAP_D / 2:   # case (y, z) touchée par le disque
        assert get(-56, my, mz) is None, ('carte du lobby : case occupée', -56, my, mz, get(-56, my, mz))
ab.append('execute if score $rp mg.st matches 1 run summon minecraft:item_display ' + ' '.join(str(c) for c in MAP_C)
          + ' {Tags:["mg.arm","mg.lmap"],billboard:"fixed",Rotation:[-90f,0f],brightness:{sky:15,block:15},item:' + rp('lobby_map') + ',' + TF.format(ty=0, s=MAP_D) + '}')
wr('lobby/armory_build', ab)
at = ['# Spawn (chaque tick après le setup) : socles de l\'armurerie, armes, portail des plots, animation du décor']
for i, (px, pz, c) in enumerate(PADS, 1):
    at.append(f'execute as @a[tag=!mg.play,x={px},y=63,z={pz},dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_{i}')
at += ['', '# Recharge de la baguette et du railgun', 'scoreboard players remove @a[scores={mg.wd=1..}] mg.wd 1', 'scoreboard players remove @a[scores={mg.lcd=1..}] mg.lcd 1', '',
       '# Utilisation (seulement dans le lobby, hors partie)',
       'execute if score $state mg.st matches 0 as @a[scores={mg.qs=1..},tag=!mg.surv] unless items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:lobby/laser',
       'execute if score $state mg.st matches 0 as @a[scores={mg.fw=1..},tag=!mg.surv] at @s run function mg:lobby/wand',
       'execute as @a[scores={mg.wc=1..},tag=!mg.surv] run function mg:lobby/wind_used',
       'execute if score $state mg.st matches 0 as @e[type=minecraft:snowball,tag=mg.sn] at @s run function mg:lobby/snow_tick',
       'execute if score $state mg.st matches 0 as @a[scores={mg.us=1..},tag=!mg.surv] at @s run function mg:lobby/snow_thrown',
       'execute unless score $state mg.st matches 0 run scoreboard players reset @a mg.fw', '',
       '', '# Décor : animation toutes les 2 s, particules toutes les 0,5 s',
       'scoreboard players add $lan mg.t 1',
       'execute if score $lan mg.t matches 40.. run function mg:lobby/anim',
       'execute if score $lan mg.t matches 40.. run scoreboard players set $lan mg.t 0',
       'scoreboard players operation $lfx mg.t = $lan mg.t', 'scoreboard players set $l10 mg.t 10', 'scoreboard players operation $lfx mg.t %= $l10 mg.t',
       'execute if score $lfx mg.t matches 0 if entity @a[x=0,y=64,z=0,distance=..160] run function mg:lobby/fx']
wr('lobby/armory_tick', at)
GIVE_SLOT = {1: 'hotbar.0', 3: 'hotbar.2', 4: 'hotbar.3'}
for i, slot in GIVE_SLOT.items():
    p = os.path.join(F, 'lobby', f'pad_{i}_give.mcfunction')
    s = open(p, encoding='utf-8').read().rstrip('\n').split('\n')
    s = [l for l in s if 'item_model' not in l]
    s.append(f'execute if score $rp mg.st matches 1 run item modify entity @s {slot} {{"function":"minecraft:set_components","components":{{"minecraft:item_model":"mg:{PADM[i - 1][1]}"}}}}')
    wr(f'lobby/pad_{i}_give', s)
p = os.path.join(F, 'lobby', 'give_wand.mcfunction')
s = [l for l in open(p, encoding='utf-8').read().rstrip('\n').split('\n') if 'item_model' not in l]
s.insert(2, 'execute if score $rp mg.st matches 1 run item modify entity @s hotbar.1 {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:magic_wand"}}')
wr('lobby/give_wand', s)
wr('lobby/laser_hit', ['# Impact du laser sur un bloc (@s = tireur) : cibles du stand de tir',
                       'execute if block ~ ~ ~ minecraft:target run return run function mg:lobby/laser_bull',
                       'execute if block ~ ~ ~ #minecraft:wool run function mg:lobby/laser_ring',
                       'particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0.4 18',
                       'particle minecraft:end_rod ~ ~ ~ 0.15 0.15 0.15 0.08 10',
                       'particle minecraft:dust{color:[1.0,0.2,0.2],scale:1.5} ~ ~ ~ 0.15 0.15 0.15 0 10',
                       'particle minecraft:smoke ~ ~ ~ 0.1 0.1 0.1 0.02 6',
                       'playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 0.8 1.6'])
wr('lobby/laser_bull', ['# Laser dans le mille (cœur d\'une cible)',
                        'particle minecraft:firework ~ ~ ~ 0.2 0.2 0.2 0.15 30',
                        'particle minecraft:dust{color:[1.0,0.85,0.1],scale:1.4} ~ ~ ~ 0.3 0.3 0.3 0 20',
                        'playsound minecraft:block.note_block.bell master @a ~ ~ ~ 1 1.5',
                        'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.8 1.2',
                        'title @s actionbar [{"text":"★ DANS LE MILLE ! ★","color":"gold","bold":true}]'])
wr('lobby/laser_ring', ['# Laser sur les anneaux d\'une cible',
                        'particle minecraft:crit ~ ~ ~ 0.2 0.2 0.2 0.1 12',
                        'playsound minecraft:block.note_block.pling master @a ~ ~ ~ 0.8 1.1',
                        'title @s actionbar [{"text":"◎ Cible touchée, vise le centre !","color":"yellow"}]'])

# ------------------------------------------------------------------ parkour : blocs, marqueurs, chutes
def yaw_to(a, b): return round(math.degrees(math.atan2(-(b[0] - a[0]), b[2] - a[2])), 1)
seq = [(67.5, 63, 0.5)] + [(x + 0.5, y, z + 0.5) for (x, z, y, b) in S1]
pb = ['# Parkour du spawn (généré par tools/lobby/gen_lobby.py) : jardin suspendu puis la Tour céleste en spirale',
      'kill @e[type=minecraft:marker,tag=mg.pkm]', 'kill @e[type=minecraft:text_display,tag=mg.pkd]']
pkc = {}
for (x, y, z, b) in PK: pkc[(x, y, z)] = b
pb += merge({k: v for k, v in pkc.items() if not is_conn(v)}, ' strict') + merge({k: v for k, v in pkc.items() if is_conn(v)}, '')
for (x, y, z, b) in [(x, y, z, b) for (x, y, z), b in W.items() if x >= 112 and b in ('beacon', 'lime_stained_glass', 'iron_block')]:
    pb.append(f'setblock {x} {y} {z} minecraft:{b}')
nexts = {0: (71.5, 0.5), 1: (106.5, 1.5)}
for (sx, sy, sz, i) in spiral:
    if i in (14, 28):
        nx = spiral[i + 1]; nexts[2 if i == 14 else 3] = (nx[0] + 0.5, nx[2] + 0.5)
for (pos, n, by) in CPS:
    tags = '"mg.pkc","mg.pks","mg.pkm","mg.pkn"' if n == 0 else '"mg.pkc","mg.pkm","mg.pkn"'
    nx = nexts[n]
    pb.append(f'summon minecraft:marker {pos[0]} {pos[1]} {pos[2]} {{Tags:[{tags}],Rotation:[{yaw_to((pos[0], 0, pos[2]), (nx[0], 0, nx[1]))}f,0f]}}')
    pb.append(f'scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t {n}')
    pb.append('tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn')
pb.append(f'summon minecraft:marker {FIN[0]} {FIN[1]} {FIN[2]} {{Tags:["mg.pkf","mg.pkm","mg.pkn"]}}')
pb.append('scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 4')
pb.append('tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn')
pb.append('summon minecraft:text_display 67.5 66.9 0.5 {Tags:["mg.pkd","mg.pkboard"],billboard:"center",text:[{"text":"3 checkpoints : grimpe au sommet de la Tour céleste !","color":"gray"}],'
          + TF.format(ty=0, s=1) + '}')
pb.append('summon minecraft:text_display 67.5 67.4 0.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"Pose-toi sur l\'émeraude pour démarrer le chrono","color":"green"}],'
          + TF.format(ty=0, s=0.9) + '}')
for (pos, n, by) in CPS[1:]:
    pb.append(f'summon minecraft:text_display {pos[0]} {pos[1] + 1.6} {pos[2]} {{Tags:["mg.pkd"],billboard:"center",text:[{{"text":"✔ Checkpoint {n}/3","color":"aqua","bold":true}}],'
              + TF.format(ty=0, s=1.2) + '}')
pb.append('execute if score $pkrec mg.st matches 1.. run function mg:parkour/board_refresh')
wr('parkour/build', pb)
wr('parkour/board_refresh', ['# Réaffiche le record du parkour sur le panneau (après reconstruction)',
                             'scoreboard players set $pk20 mg.st 20', 'scoreboard players set $pk2 mg.st 2',
                             'scoreboard players operation $s mg.st = $pkrec mg.st', 'scoreboard players operation $s mg.st /= $pk20 mg.st',
                             'scoreboard players operation $d mg.st = $pkrec mg.st', 'scoreboard players operation $d mg.st %= $pk20 mg.st',
                             'scoreboard players operation $d mg.st /= $pk2 mg.st',
                             'execute store result storage mg:pk s int 1 run scoreboard players get $s mg.st',
                             'execute store result storage mg:pk d int 1 run scoreboard players get $d mg.st',
                             'function mg:parkour/board with storage mg:pk'])
segmin = {}
allpts = [(63, 0)] + [(y, 0) for (x, z, y, b) in S1] + [(67, 1), (67, 1), (68, 1)]
for (x, y, z, i) in spiral: allpts.append((y, 1 if i < 14 else (2 if i < 28 else 3)))
allpts.append((FINY, 3))
for (y, sgm) in allpts: segmin[sgm] = min(segmin.get(sgm, 999), y)
fc = ['# Chute : en dessous du point le plus bas du tronçon → retour au dernier checkpoint (@s = coureur) (généré)']
for sgm in range(4):
    fc.append(f'execute if score @s mg.ppc matches {sgm} at @s if entity @s[y={segmin[sgm] - 3 - 2048},dy=2048] run return run function mg:parkour/fall')
wr('parkour/fall_check', fc)
wr('parkour/fall', ['# Chute (@s = coureur) : retour au dernier checkpoint, tourné vers le saut suivant',
                    'scoreboard players add @s mg.ppf 1', 'scoreboard players operation $ck mg.st = @s mg.ppc', 'tag @s add mg.pkx',
                    'execute as @e[type=minecraft:marker,tag=mg.pkc] if score @s mg.t = $ck mg.st at @s run tp @a[tag=mg.pkx,limit=1] ~ ~ ~ ~ 0',
                    'tag @s remove mg.pkx',
                    'title @s actionbar [{"text":"↺ Retour au checkpoint","color":"yellow"}]',
                    'execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.6 1.2',
                    'function mg:core/fall_heal'])
print('parkour : fin y', FINY, '| seuils', {k: v - 3 for k, v in segmin.items()}, '| sauts', len(path))

