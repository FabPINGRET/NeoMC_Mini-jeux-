# Neo GTA, braquages, véhicules achetés, carte (police mg:gta_map) : exécuté par gen_gta.py (exec) à sa place d'origine.
# Utilise : AIRF, BANK, CAR_DROP, CITY, DIM, DSP, H, HX, js, LIFT, NH, shop_label, VFRONT, VY, w, Z

# ---------------------------------------------------------------- braquages
def bar(fn, label, col, need):
    L = [f'# @s : jauge de braquage ({label}), mg.grob sur {need}', 'scoreboard players set @s mg.gal 10',
         'scoreboard players operation $gbp mg.st = @s mg.grob', 'scoreboard players set #10 mg.st 10', 'scoreboard players operation $gbp mg.st *= #10 mg.st',
         f'scoreboard players set $gbn mg.st {need}', 'scoreboard players operation $gbp mg.st /= $gbn mg.st']
    for k in range(11):
        L.append(f'execute if score $gbp mg.st matches {k} run title @s actionbar ' + js([{'text': f'💰 {label}  ', 'color': col, 'bold': True},
                                                                                          {'text': '▮' * k, 'color': 'green'}, {'text': '▯' * (10 - k), 'color': 'dark_gray'}]))
    w(f'gta/{fn}', L)


bar('rob_bar_ped', 'Braquage du passant', 'yellow', 40)
bar('rob_bar_shop', 'Caisse du commerce', 'gold', 100)
bar('rob_bar_bank', 'Coffres de la banque', 'red', 300)
w('gta/rob', ['# @s (accroupi, arme en main) : banque, sinon commerce, sinon passant visé (6 blocs)',
              f'execute if entity @s[x={BANK[0] + 1},y=66,z={Z + BANK[3] - 4},dx={BANK[2] - BANK[0] - 2},dy=3,dz=3] if entity @e[type=minecraft:marker,tag=mg.gbank,scores={{mg.gpc=..0}}] run return run function mg:gta/rob_bank',
              'execute if entity @e[type=minecraft:marker,tag=mg.gshop,distance=..2.6,scores={mg.gpc=..0}] run return run function mg:gta/rob_shop',
              'tag @e[tag=mg.grt] remove mg.grt', 'scoreboard players set $gar mg.st 7', 'tag @s add mg.gaim',
              'execute anchored eyes positioned ^ ^ ^1 run function mg:gta/rob_ray', 'tag @s remove mg.gaim',
              'execute if entity @e[tag=mg.grt] run return run function mg:gta/rob_ped',
              'function mg:gta/rob_stop'])
w('gta/rob_ray', ['# Un pas (1 bloc) vers le passant visé',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return 0',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:villager,tag=mg.gped,tag=!mg.grobbed,dx=0,dy=0,dz=0,limit=1] run return run tag @s add mg.grt',
                  'scoreboard players remove $gar mg.st 1',
                  'execute if score $gar mg.st matches 1.. positioned ^ ^ ^1 run function mg:gta/rob_ray'])
w('gta/rob_stop', ['# @s arrête de braquer', 'execute if score @s mg.grob matches 15.. run title @s actionbar {"text":"✋ Braquage interrompu","color":"gray"}',
                   'scoreboard players set @s mg.grob 0'])
w('gta/rob_ped', ['# @s braque le passant visé (mg.grt) : 2 s', 'effect give @e[tag=mg.grt] minecraft:slowness 1 6 true',
                  'execute as @e[tag=mg.grt] at @s run particle minecraft:angry_villager ~ ~2.2 ~ 0.2 0.1 0.2 0 1',
                  'scoreboard players add @s mg.grob 5', 'function mg:gta/rob_bar_ped',
                  'execute if score @s mg.grob matches 40.. run function mg:gta/rob_ped_ok', 'tag @e[tag=mg.grt] remove mg.grt'])
w('gta/rob_ped_ok', ['# Passant dépouillé : 20 à 80 $, il s\'enfuit ; un témoin peut prévenir la police', 'scoreboard players set @s mg.grob 0',
                     'execute store result score $gcv mg.st run random value 20..80', 'function mg:gta/cash_gain',
                     'tag @e[tag=mg.grt] add mg.grobbed', 'effect give @e[tag=mg.grt] minecraft:speed 15 2 true',
                     'execute as @e[tag=mg.grt] at @s run particle minecraft:happy_villager ~ ~1 ~ 0.3 0.5 0.3 0 8',
                     'execute as @e[tag=mg.grt] at @s run playsound minecraft:entity.villager.hurt neutral @a ~ ~ ~ 1 1.3',
                     'execute store result score $gr mg.st run random value 0..2', 'execute if score $gr mg.st matches 0 run function mg:gta/wanted_up'])
w('gta/lift_up', ['# Ascenseur du manoir : vers le toit-terrasse', f'tp @s {LIFT[0] - 1}.5 {NH["lift_y"][1]} {Z + LIFT[1] + 2}.5', 'playsound minecraft:block.beacon.activate player @s ~ ~ ~ 0.5 2'])
w('gta/lift_down', ['# Ascenseur du manoir : vers le hall', f'tp @s {LIFT[0] - 1}.5 {NH["lift_y"][0]} {Z + LIFT[1] + 2}.5', 'playsound minecraft:block.beacon.deactivate player @s ~ ~ ~ 0.5 2'])
w('gta/rob_shop', ['# @s braque la caisse du commerce : 5 s, alarme ; le caissier lève les mains', 'scoreboard players add @s mg.grob 5', 'function mg:gta/rob_bar_shop',
                   'execute as @e[type=minecraft:villager,tag=mg.gclerk,distance=..5] at @s run particle minecraft:angry_villager ~ ~2.3 ~ 0.2 0.1 0.2 0 1',
                   'execute if score @s mg.grob matches 10 as @e[type=minecraft:villager,tag=mg.gclerk,distance=..5] at @s run playsound minecraft:entity.villager.hurt neutral @a ~ ~ ~ 1 1.4',
                   'execute if score @s mg.grob matches 5 run playsound minecraft:block.bell.use master @a ~ ~ ~ 2 1.2',
                   'execute if score @s mg.grob matches 50 run playsound minecraft:block.bell.use master @a ~ ~ ~ 2 1.2',
                   'execute if score @s mg.grob matches 100.. run function mg:gta/rob_shop_ok'])
w('gta/rob_shop_ok', ['# Caisse vidée : 200 à 450 $, deux étoiles, commerce fermé 3 min', 'scoreboard players set @s mg.grob 0',
                      'execute store result score $gcv mg.st run random value 200..450', 'function mg:gta/cash_gain',
                      'execute as @e[type=minecraft:marker,tag=mg.gshop,distance=..2.6,limit=1,sort=nearest] run function mg:gta/shop_close',
                      'function mg:gta/wanted_up', 'function mg:gta/wanted_up',
                      'title @s title {"text":" ","color":"gold"}', 'title @s subtitle {"text":"💰 Caisse vidée !","color":"gold","bold":true}'])
w('gta/shop_close', ['# @s (caisse) : fermé 3 min', 'scoreboard players set @s mg.gpc 3600', 'scoreboard players operation $gs mg.st = @s mg.gsid',
                     'execute as @e[type=minecraft:text_display,tag=mg.gshl] if score @s mg.gsid = $gs mg.st run data merge entity @s {text:{"text":"🔒 Fermé (braquage)","color":"red","bold":true}}'])
SR = ['# @s (caisse) : le commerce rouvre', 'scoreboard players operation $gs mg.st = @s mg.gsid']
for k, (mx, sz, nm, col) in enumerate(CITY['shops']):
    SR.append(f'execute if score $gs mg.st matches {k} as @e[type=minecraft:text_display,tag=mg.gshl] if score @s mg.gsid matches {k} run data merge entity @s {{text:{js(shop_label(nm))}}}')
w('gta/shop_reopen', SR)
w('gta/rob_bank', ['# @s braque la banque : 15 s dans la salle des coffres, alarme, 4 étoiles d\'un coup', 'scoreboard players add @s mg.grob 5', 'function mg:gta/rob_bar_bank',
                   'execute if score @s mg.grob matches 5 run tellraw @a[tag=mg.gtw] [{"text":"🚨 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" braque la banque de Neo City !","color":"red","bold":true}]',
                   'execute if score @s mg.grob matches 5 if score @s mg.gwl matches ..3 run scoreboard players set @s mg.gwl 4',
                   'execute if score @s mg.grob matches 5 run scoreboard players set @s mg.gwt 300', 'execute if score @s mg.grob matches 5 run team leave @s',
                   'scoreboard players operation $gbk mg.st = @s mg.grob', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $gbk mg.st %= #20 mg.st',
                   'execute if score $gbk mg.st matches 5 run playsound minecraft:block.bell.use master @a ~ ~ ~ 4 0.8',
                   'execute if score $gbk mg.st matches 15 run playsound minecraft:block.bell.use master @a ~ ~ ~ 4 1.1',
                   'execute if score @s mg.grob matches 300.. run function mg:gta/rob_bank_ok'])
w('gta/rob_bank_ok', ['# Coffres vidés : 1 500 à 2 500 $, banque fermée 7 min', 'scoreboard players set @s mg.grob 0',
                      'execute store result score $gcv mg.st run random value 1500..2500', 'function mg:gta/cash_gain',
                      'scoreboard players set @e[type=minecraft:marker,tag=mg.gbank] mg.gpc 8400',
                      'execute as @e[type=minecraft:text_display,tag=mg.gbkl] run data merge entity @s {text:{"text":"🔒 Coffres vides","color":"red","bold":true}}',
                      'function mg:gta/wanted_up',
                      'title @s title {"text":"💰 JACKPOT","color":"gold","bold":true}',
                      'tellraw @a[tag=mg.gtw] [{"text":"💰 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a vidé les coffres de la banque : ","color":"gold"},'
                      '{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $ !","color":"gold"}]',
                      'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1'])
w('gta/bank_reopen', ['# Les coffres sont de nouveau pleins',
                      'execute as @e[type=minecraft:text_display,tag=mg.gbkl] run data merge entity @s {text:' + js({"text": "💰 Coffres : accroupi + arme pendant 15 s", "color": "gold"}) + '}',
                      'tellraw @a[tag=mg.gtw] {"text":"🏦 Les coffres de la banque sont de nouveau pleins…","color":"gold"}'])

# ---------------------------------------------------------------- véhicules achetés (un par joueur : l'ancien disparaît)
w('gta/veh_buy', ['# @s achète un véhicule de type $(t) : l\'ancien disparaît, le nouveau est livré',
                  'scoreboard players operation $gv mg.st = @s mg.gveh',
                  'execute if score @s mg.gveh matches 1.. as @e[tag=mg.gta] if score @s mg.gvid = $gv mg.st run kill @s',
                  '$function mg:gta/veh_$(t)',
                  'scoreboard players operation @s mg.gveh = $gvid mg.st',
                  'execute as @e[tag=mg.gta,type=!minecraft:block_display,type=!minecraft:interaction] if score @s mg.gvid = $gvid mg.st run effect give @s minecraft:glowing 60 0 true',
                  'title @s title {"text":"🔑","color":"gold"}',
                  '$function mg:gta/veh_where_$(t)'])
for _t in ('moto', 'muscle', 'supercar', 'heli', 'plane'):
    _air = _t in ('heli', 'plane')
    _v = "à l'hélistation de la villa" if _air else 'devant le garage de la villa'
    _c = "à l'aérodrome, au nord du parc" if _air else 'devant la concession'
    w(f'gta/veh_where_{_t}', ['execute if score $gvilla mg.st matches 1 run return run title @s subtitle ' + js({'text': f"Il t'attend {_v} (il brille) !", 'color': 'yellow'}),
                               'title @s subtitle ' + js({'text': f"Il t'attend {_c} (il brille) !", 'color': 'yellow'})])
for (t, n, k) in (('moto', 11, 0), ('muscle', 12, 1), ('supercar', 13, 2)):
    cx, cz = NH['car_drop'][k]
    w(f'gta/veh_{t}', [f'execute if score $gvilla mg.st matches 1 in {DIM} positioned {cx} {VY} {Z + cz} run return run function mg:gta/car/spawn_{n}',
                       f'execute in {DIM} positioned {CAR_DROP[0] + 4 * k - 4} 65 {Z + CAR_DROP[1]} run function mg:gta/car/spawn_{n}'])
w('gta/veh_heli', [f'execute if score $gvilla mg.st matches 1 in {DIM} positioned {NH["heli"][0]} {VY} {Z + NH["heli"][1]} run return run function mg:gta/heli_spawn {{c:"yellow_concrete"}}',
                   f'execute in {DIM} positioned {AIRF[0] - 4} 66 {Z + AIRF[1]} run function mg:gta/heli_spawn {{c:"yellow_concrete"}}'])
w('gta/veh_plane', [f'execute if score $gvilla mg.st matches 1 in {DIM} positioned {NH["plane"][0]} {VY} {Z + NH["plane"][1]} run return run function mg:gta/plane_spawn',
                    f'execute in {DIM} positioned {AIRF[0] + 4} 66 {Z + AIRF[1]} run function mg:gta/plane_spawn'])
BUY_CARS = [  # n°, carrosserie, toit, nom, vitesse, échelle du cheval, modèle
    (11, 'red_concrete', 'black_concrete', '🏍 Moto', 0.46, 0.45, 'moto'),
    (12, 'red_concrete', 'black_concrete', '🚗 Muscle car', 0.44, 0.55, 'muscle'),
    (13, 'purple_concrete', 'black_stained_glass', '🏎 Supercar', 0.52, 0.5, 'super')]
for (n, body, roof, name, spd, sc, kind) in BUY_CARS:
    def D(*a, **k): return DSP('mg.gcard', *a, **k)
    L = [f'# Véhicule acheté n° {n} : {name}', 'scoreboard players add $gvid mg.st 1',
         'summon minecraft:horse ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcarh","mg.gvn","mg.npc"],Tame:1b,Silent:1b,PersistenceRequired:1b,Health:40f,'
         'equipment:{saddle:{id:"minecraft:saddle",count:1}},drop_chances:{saddle:0f},'
         f'CustomName:{js({"text": name, "color": "gold"})},CustomNameVisible:0b,'
         'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
         f'attributes:[{{id:"minecraft:movement_speed",base:{spd}}},{{id:"minecraft:jump_strength",base:0.0}},{{id:"minecraft:step_height",base:1.1}},'
         f'{{id:"minecraft:max_health",base:40}},{{id:"minecraft:scale",base:{sc}}}]}}']
    if kind == 'moto':
        L += [D('black_concrete', -0.12, 0.0, 0.55, 0.24, 0.6, 0.6), D('black_concrete', -0.12, 0.0, -0.95, 0.24, 0.6, 0.6),   # roues
              D(body, -0.2, 0.45, -0.7, 0.4, 0.3, 1.4, body=True), D('gray_concrete', -0.15, 0.3, -0.6, 0.3, 0.2, 1.2),          # réservoir, cadre
              D('black_concrete', -0.2, 0.7, -0.75, 0.4, 0.08, 0.6), D('gray_concrete', -0.4, 0.95, 0.55, 0.8, 0.06, 0.06),     # selle, guidon
              D('sea_lantern', -0.1, 0.65, 0.75, 0.2, 0.15, 0.05), D('redstone_block', -0.08, 0.6, -0.97, 0.16, 0.1, 0.04)]
    elif kind == 'muscle':
        L += [D(body, -0.95, 0.05, -1.8, 1.9, 0.7, 3.6, body=True), D(roof, -0.8, 0.75, -1.0, 1.6, 0.55, 1.5),
              D('white_concrete', -0.25, 0.76, -1.8, 0.18, 0.01, 3.6), D('white_concrete', 0.07, 0.76, -1.8, 0.18, 0.01, 3.6),        # bandes de course
              D('gray_concrete', -0.3, 0.75, 0.6, 0.6, 0.15, 0.6),                                                                  # prise d'air
              D('black_concrete', -1.0, 0.0, -1.3, 0.25, 0.5, 0.65), D('black_concrete', 0.75, 0.0, -1.3, 0.25, 0.5, 0.65),
              D('black_concrete', -1.0, 0.0, 0.9, 0.25, 0.5, 0.65), D('black_concrete', 0.75, 0.0, 0.9, 0.25, 0.5, 0.65),
              D('sea_lantern', -0.8, 0.35, 1.78, 0.35, 0.2, 0.05), D('sea_lantern', 0.45, 0.35, 1.78, 0.35, 0.2, 0.05),
              D('redstone_block', -0.8, 0.35, -1.83, 0.35, 0.2, 0.05), D('redstone_block', 0.45, 0.35, -1.83, 0.35, 0.2, 0.05)]
    else:
        L += [D(body, -1.0, 0.05, -1.9, 2.0, 0.5, 3.8, body=True), D(roof, -0.75, 0.55, -0.9, 1.5, 0.45, 1.5),
              D(body, -0.95, 0.85, -1.95, 1.9, 0.08, 0.45), D('black_concrete', -0.85, 0.55, -1.85, 0.08, 0.3, 0.08),                 # aileron
              D('black_concrete', 0.77, 0.55, -1.85, 0.08, 0.3, 0.08),
              D('black_concrete', -1.05, 0.0, -1.35, 0.25, 0.45, 0.65), D('black_concrete', 0.8, 0.0, -1.35, 0.25, 0.45, 0.65),
              D('black_concrete', -1.05, 0.0, 0.95, 0.25, 0.45, 0.65), D('black_concrete', 0.8, 0.0, 0.95, 0.25, 0.45, 0.65),
              D('sea_lantern', -0.85, 0.25, 1.88, 0.4, 0.12, 0.05), D('sea_lantern', 0.45, 0.25, 1.88, 0.4, 0.12, 0.05),
              D('redstone_block', -0.9, 0.3, -1.93, 1.8, 0.08, 0.04)]
    L += ['summon minecraft:interaction ~ ~ ~ {Tags:["mg.gta","mg.gcint","mg.gvn"],width:2.4f,height:1.7f,response:1b}', 'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
    w(f'gta/car/spawn_{n}', L)
PL = ['# Avion : happy ghast invisible et rapetissé, très rapide, fuselage, ailes et dérive', 'scoreboard players add $gvid mg.st 1',
      'summon minecraft:happy_ghast ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.ghel","mg.gvn","mg.npc"],PersistenceRequired:1b,Health:60f,'
      'equipment:{body:{id:"minecraft:white_harness",count:1}},drop_chances:{body:0f},'
      f'CustomName:{js({"text": "✈ Avion", "color": "aqua", "bold": True})},CustomNameVisible:0b,'
      'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
      'attributes:[{id:"minecraft:flying_speed",base:0.24},{id:"minecraft:movement_speed",base:0.2},{id:"minecraft:max_health",base:60},{id:"minecraft:scale",base:0.5}]}',
      H('white_concrete', -0.6, -0.5, -3.0, 1.2, 1.1, 5.4, body=True), H('red_concrete', -0.45, -0.4, 2.4, 0.9, 0.8, 0.7),       # fuselage, nez
      H('light_blue_stained_glass', -0.5, 0.55, 0.6, 1.0, 0.45, 1.2),                                                            # verrière
      H('red_concrete', -4.6, -0.15, -0.5, 9.2, 0.12, 1.3), H('white_concrete', -4.6, -0.05, -0.5, 0.6, 0.12, 1.3),              # ailes
      H('white_concrete', 4.0, -0.05, -0.5, 0.6, 0.12, 1.3),
      H('red_concrete', -1.7, 0.1, -3.0, 3.4, 0.1, 0.8), H('red_concrete', -0.06, 0.1, -3.1, 0.12, 1.3, 0.9),                    # empennage
      H('black_concrete', -0.05, -0.75, 2.95, 0.1, 1.5, 0.08), H('black_concrete', -0.75, -0.05, 2.95, 1.5, 0.1, 0.08),          # hélice
      H('gray_concrete', -0.6, -1.3, 0.8, 0.1, 0.6, 0.1), H('gray_concrete', 0.5, -1.3, 0.8, 0.1, 0.6, 0.1),                     # train
      H('black_concrete', -0.7, -1.45, 0.65, 0.3, 0.3, 0.4), H('black_concrete', 0.4, -1.45, 0.65, 0.3, 0.3, 0.4),
      'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
w('gta/plane_spawn', PL)

# ---------------------------------------------------------------- carte (police mg:gta_map) : plan + point « tu es ici » sur une grille 30 × 30
CELL = ['scoreboard players set #30 mg.st 30', 'scoreboard players set #177 mg.st 177']


def cell(src, si, sj):
    """Case 30 × 30 de la position de src (sélecteur) → scores si / sj, bornés."""
    return [f'execute store result score {si} mg.st run data get entity {src} Pos[0]', f'execute store result score {sj} mg.st run data get entity {src} Pos[2]',
            f'scoreboard players add {si} mg.st {HX}', f'scoreboard players remove {sj} mg.st {Z - HX}',
            f'scoreboard players operation {si} mg.st *= #30 mg.st', f'scoreboard players operation {si} mg.st /= #177 mg.st',
            f'scoreboard players operation {sj} mg.st *= #30 mg.st', f'scoreboard players operation {sj} mg.st /= #177 mg.st',
            f'execute if score {si} mg.st matches ..-1 run scoreboard players set {si} mg.st 0', f'execute if score {si} mg.st matches 30.. run scoreboard players set {si} mg.st 29',
            f'execute if score {sj} mg.st matches ..-1 run scoreboard players set {sj} mg.st 0', f'execute if score {sj} mg.st matches 30.. run scoreboard players set {sj} mg.st 29',
            f'scoreboard players operation {sj} mg.st *= #30 mg.st', f'scoreboard players operation {sj} mg.st += {si} mg.st']


w('gta/dots_init', ['# Les 900 points de la carte (police mg:gta_map), indexés ligne × 30 + colonne',
                    'data modify storage mg:gta dots set value ' + js([chr(0xE500 + k) for k in range(900)])])
w('gta/map_show', ['# @s tient la carte : plan de la ville, sa position (rouge), l\'objectif de sa mission (or)',
                   'execute unless score $rp mg.st matches 1 run return run title @s actionbar [{"text":"🗺 Carte : active le resource pack (/function mg:rp_on)","color":"gray"}]',
                   'execute unless data storage mg:gta dots run function mg:gta/dots_init'] + CELL + cell('@s', '$gmi', '$gmj') +
  ['execute store result storage mg:gta mi.p int 1 run scoreboard players get $gmj mg.st',
   'function mg:gta/map_pick_p with storage mg:gta mi',
   'data modify storage mg:gta mp.t set value "\ue402"',
   'scoreboard players operation $gb mg.st = @s mg.bid', 'tag @e remove mg.gmine',
   'execute as @e[tag=mg.gmo] if score @s mg.bid = $gb mg.st run tag @s add mg.gmine',
   'execute if entity @e[tag=mg.gmine] run function mg:gta/map_target',
   'data modify storage mg:gta mp.o set value [{"text":""}]', 'tag @s add mg.gme',
   'execute as @a[tag=mg.gtw,tag=!mg.gme,gamemode=!spectator] run function mg:gta/map_other', 'tag @s remove mg.gme',
   'title @s times 0 6 2', 'scoreboard players set @s mg.gal 6',
   'title @s actionbar [{"text":"● ","color":"red"},{"text":"toi  ","color":"gray"},{"text":"● ","color":"#3FA9FF"},{"text":"potes  ","color":"gray"},{"text":"● ","color":"gold"},{"text":"mission  ","color":"gray"},'
   '{"text":"■ ","color":"#9646C8"},{"text":"concession ","color":"gray"},{"text":"■ ","color":"#C82828"},{"text":"armurerie ","color":"gray"},'
   '{"text":"■ ","color":"#E8BA24"},{"text":"banque ","color":"gray"},{"text":"■ ","color":"#F58C1E"},{"text":"commerces","color":"gray"}]',
   'function mg:gta/map_title with storage mg:gta mp'])
w('gta/map_target', ['# Case de l\'objectif de la mission (@e[tag=mg.gmine])'] + cell('@e[tag=mg.gmine,limit=1]', '$gti', '$gtj') +
  ['execute store result storage mg:gta mi.t int 1 run scoreboard players get $gtj mg.st', 'function mg:gta/map_pick_t with storage mg:gta mi'])
w('gta/map_other', ['# @s : un autre joueur de Neo GTA, ajouté (point bleu) à la carte de celui qui la regarde'] + cell('@s', '$goi', '$goj') +
  ['execute store result storage mg:gta mi.o int 1 run scoreboard players get $goj mg.st', 'function mg:gta/map_pick_o with storage mg:gta mi',
   'function mg:gta/map_add_o with storage mg:gta mi'])
w('gta/map_pick_o', ['$data modify storage mg:gta mi.d set from storage mg:gta dots[$(o)]'])
w('gta/map_add_o', ['$data modify storage mg:gta mp.o append value {"text":"\ue401$(d)"}'])
w('gta/map_pick_p', ['$data modify storage mg:gta mp.p set from storage mg:gta dots[$(p)]'])
w('gta/map_pick_t', ['$data modify storage mg:gta mp.t set from storage mg:gta dots[$(t)]'])
w('gta/map_title', ['# Titre : plan, puis (retour au bord gauche) le point rouge, puis l\'objectif doré (ou un espace de même largeur)',
                    '$title @s title [{"text":"\ue400\ue401","font":"mg:gta_map","color":"white","shadow_color":0},{"text":"$(p)","font":"mg:gta_map","color":"#FF2A2A","shadow_color":0},'
                    '{"text":"\ue401$(t)","font":"mg:gta_map","color":"#FFC020","shadow_color":0},{"text":"","font":"mg:gta_map","color":"#3FA9FF","shadow_color":0,"extra":$(o)}]'])

w('gta/home', ['# @s : retour à la villa (Neo Hills), refusé si la police le recherche', 'scoreboard players reset @s mg.gqs',
                'execute if score @s mg.gwl matches 1.. run return run title @s actionbar {"text":"🚔 Impossible : la police te recherche !","color":"red"}',
                'execute on vehicle run return 0',
                f'execute in {DIM} run tp @s {VFRONT[0] + 0.5} {VY} {Z + VFRONT[1] + 0.5} 180 0',
                f'execute in {DIM} run spawnpoint @s {VFRONT[0]} {VY} {Z + VFRONT[1]}',
                'execute at @s run playsound minecraft:block.portal.travel player @s ~ ~ ~ 0.2 2',
                'title @s actionbar {"text":"🏠 Neo Hills","color":"aqua","bold":true}'])
