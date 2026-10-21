# Neo GTA, session : kit, tick, viseur / lunette / radio / étoiles : exécuté par gen_gta.py (exec) à sa place d'origine.
# Utilise : AIRF, AREA, ARM_PADS, ARMORY, BANK, CAR_AT, CARS, CITY, DIM, EXIT, G, HELI_AT, INTER, js, LIFT, NA, NH, PAD,
#   PAD_TYPES, PADS_AT, RET_R, RET_W, SCOPE, SHOP_CLERK, SHOW, SHOW_PADS, SIDE, STAR_E, STAR_F, STATIONS, THIN, TR, VAULT,
#   VPADS, VWEAP, VY, w, Z

def shop_label(nm):
    return [{"text": nm, "color": "white", "bold": True}, {"text": "\nbraquable : accroupi + arme devant la caisse", "color": "gray", "bold": False}]


S = ['# Entités de la session (contexte : dimension mg:gta)', 'function mg:gta/clear', 'function mg:gta/walls',
     'scoreboard players set $gvid mg.st 0', 'team add mg_gciv', 'team modify mg_gciv friendlyFire true', 'team modify mg_gciv seeFriendlyInvisibles false',
     'team modify mg_gciv nametagVisibility always', 'team join mg_gciv @a[tag=mg.gtw,scores={mg.gwl=0}]', 'function mg:gta/bars']
S += [f'summon minecraft:marker {x} 65 {Z + z} {{Tags:["mg.gta","mg.gix"]}}' for (x, z) in INTER]
S += [f'summon minecraft:marker {x} 65 {Z + z} {{Tags:["mg.gta","mg.gsw"]}}' for (x, z) in SIDE]
for (x, z), t in zip(PADS_AT, PAD_TYPES):
    n = PAD[t][0]
    px, pz = x - 5, z - 4
    S += [f'summon minecraft:marker {px} 65 {Z + pz} {{Tags:["mg.gta","mg.gpad","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {n}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {px - 0.5} 65 {Z + pz - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
for x, t in ARM_PADS:                                         # présentoirs de l'armurerie (plancher y 65)
    z = ARMORY[3] - 2
    S += [f'summon minecraft:marker {x} 66 {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[t][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {x - 0.5} 66 {Z + z - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
for x, t in SHOW_PADS:                                        # concession (plancher y 65)
    z = SHOW[3] - 3
    S += [f'summon minecraft:marker {x} 66 {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[t][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {x - 0.5} 66 {Z + z - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
S += [f'summon minecraft:text_display {(SHOW[0] + SHOW[2]) / 2 + 0.5} 71.5 {Z + SHOW[1] - 0.05} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "🏎 NEO MOTORS", "color": "light_purple", "bold": True})},'
      f'background:0,{TR % (0, 0, 0, 2.0, 2.0, 2.0)}}}',
      f'summon minecraft:text_display {(BANK[0] + BANK[2]) / 2 + 0.5} 72.6 {Z + BANK[1] - 1.1} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "🏦 BANQUE DE NEO CITY", "color": "gold", "bold": True})},'
      f'background:0,{TR % (0, 0, 0, 1.6, 1.6, 1.6)}}}',
      f'summon minecraft:marker {VAULT[0]} 66 {Z + VAULT[1]} {{Tags:["mg.gta","mg.gbank"]}}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gbank] mg.gpc 0',
      f'summon minecraft:text_display {VAULT[0] + 0.5} 68.2 {Z + VAULT[1] + 0.5} {{Tags:["mg.gta","mg.gbkl"],billboard:"center",text:{js({"text": "💰 Coffres : accroupi + arme pendant 15 s", "color": "gold"})},'
      f'background:1073741824,{TR % (0, 0, 0, 0.6, 0.6, 0.6)}}}',
      f'summon minecraft:marker {AIRF[0]} 66 {Z + AIRF[1]} {{Tags:["mg.gta","mg.gair"]}}']
for (x, z, y, ts) in [(x, z, VY, t) for x, z, t in VPADS] + [(x, z, VY, t) for x, z, t in VWEAP] + \
                     [(NH['heal_pad'][0], NH['heal_pad'][1], VY, 'heal_free'), (NH['armor_pad'][0], NH['armor_pad'][1], VY, 'g_armor'),
                      (NH['garage_pads'][-1][0] + 3, NH['garage_pads'][-1][1], VY, 'paint'), (NH['atm'][0], NH['atm'][1], 64, 'atm')]:
    S += [f'summon minecraft:marker {x} {y} {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[ts][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {x - 0.5} {y} {Z + z - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
S += ['function mg:gta/planque', 'execute unless data storage mg:gta {piste:1} run function mg:gta/piste', 'data modify storage mg:gta piste set value 1',
      f'summon minecraft:block_display {NH["trap"][0]} {VY - 1} {Z + NH["trap"][1]} {{Tags:["mg.gta"],block_state:{{Name:"minecraft:dark_oak_planks"}}}}',
      f'summon minecraft:marker {LIFT[0]} {NH["lift_y"][0]} {Z + LIFT[1]} {{Tags:["mg.gta","mg.glup"]}}',
      f'summon minecraft:marker {LIFT[0]} {NH["lift_y"][1]} {Z + LIFT[1]} {{Tags:["mg.gta","mg.gldn"]}}',
      f'summon minecraft:text_display {LIFT[0] + 0.5} {NH["lift_y"][0] + 1.8} {Z + LIFT[1] + 0.5} {{Tags:["mg.gta"],billboard:"center",text:{js({"text": "⬆ Toit-terrasse : jacuzzi et bar", "color": "aqua"})},background:1073741824,{TR % (0, 0, 0, 0.6, 0.6, 0.6)}}}',
      f'summon minecraft:text_display {LIFT[0] + 0.5} {NH["lift_y"][1] + 1.8} {Z + LIFT[1] + 0.5} {{Tags:["mg.gta"],billboard:"center",text:{js({"text": "⬇ Descendre", "color": "aqua"})},background:1073741824,{TR % (0, 0, 0, 0.6, 0.6, 0.6)}}}',
      f'summon minecraft:block_display {LIFT[0] - 0.5} {NH["lift_y"][0]} {Z + LIFT[1] - 0.5} {{Tags:["mg.gta"],block_state:{{Name:"minecraft:heavy_weighted_pressure_plate"}}}}',
      f'summon minecraft:block_display {LIFT[0] - 0.5} {NH["lift_y"][1]} {Z + LIFT[1] - 0.5} {{Tags:["mg.gta"],block_state:{{Name:"minecraft:heavy_weighted_pressure_plate"}}}}',
      f'summon minecraft:text_display {NH["sign"][0] + 0.5} {VY + 9.6} {Z + NH["sign"][1] + 0.6} {{Tags:["mg.gta"],Rotation:[0f,0f],'
      f'text:[{js({"text": "NEO HILLS", "color": "gold", "bold": True})},{js({"text": "\nla villa des joueurs : tout ce qui a été acheté une fois est ici, gratuit", "color": "gray"})}],'
      f'background:-1442840576,{TR % (0, 0, 0, 1.4, 1.4, 1.4)}}}']
for (x, z, ts) in [(p_[0], p_[1], 'slot') for p_ in CITY['places']['casino']['slots']] + [(CITY['places']['casino']['roulette'][0], CITY['places']['casino']['roulette'][1], 'roulette'),
                                                                                        (CITY['places']['casino']['roulette'][0], CITY['places']['casino']['roulette'][1] + 4, 'dice')]:
    S += [f'summon minecraft:marker {x} 66 {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[ts][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show', 'tag @e[tag=mg.gpn] remove mg.gpn']
S.append('function mg:gta/places_setup')
for k, (mx, sz, nm, col) in enumerate(CITY['shops']):                    # caissier derrière le comptoir, mode d'emploi du braquage
    S += [f'summon minecraft:villager {mx}.5 66 {Z + sz + 5}.5 {{Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,'
          f'Rotation:[180f,0f],VillagerData:{{profession:"minecraft:{SHOP_CLERK[k % len(SHOP_CLERK)]}",type:"minecraft:plains",level:2}},'
          f'CustomName:{js({"text": "Caissier", "color": "gray"})},CustomNameVisible:0b}}',
          f'summon minecraft:text_display {mx + 0.5} 67.55 {Z + sz + 3.65} {{Tags:["mg.gta"],Rotation:[180f,0f],'
          f'text:[{js({"text": "🔫 BRAQUAGE", "color": "red", "bold": True})},{js({"text": "\nAccroupis-toi devant la caisse, arme en main (5 s)", "color": "white"})},'
          f'{js({"text": "\n💰 200 à 450 $  ·  ★★ police", "color": "gold"})}],background:-1442840576,{TR % (0, 0, 0, 0.45, 0.45, 0.45)}}}']
for k, (mx, sz, nm, col) in enumerate(CITY['shops']):
    S += [f'summon minecraft:marker {mx} 66 {Z + sz + 3} {{Tags:["mg.gta","mg.gshop"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x={mx},y=66,z={Z + sz + 3}] mg.gsid {k}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x={mx},y=66,z={Z + sz + 3}] mg.gpc 0',
          f'summon minecraft:text_display {mx + 0.5} 70.4 {Z + sz - 1.2} {{Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:{js(shop_label(nm))},'
          f'background:-1442840576,{TR % (0, 0, 0, 1.1, 1.1, 1.1)}}}',
          f'scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x={mx + 0.5},y=70.4,z={Z + sz - 1.2}] mg.gsid {k}']
S += [f'summon minecraft:text_display -13.5 70.5 {Z + ARMORY[1] - 0.05} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "🔫 ARMURERIE", "color": "white", "bold": True})},'
      f'background:0,{TR % (0, 0, 0, 2.2, 2.2, 2.2)}}}',
      f'summon minecraft:text_display -13.5 70.05 {Z + ARMORY[1] - 0.05} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "Toutes les armes, en libre-service", "color": "yellow"})},'
      f'background:0,{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}']
for (car, (x, z)) in zip(CARS * 2, CAR_AT):
    S.append(f'execute positioned {x + 2} 65 {Z + z} run function mg:gta/car/spawn_{car[0]}')
for (x, z, col) in HELI_AT:
    S.append(f'execute positioned {x} 66 {Z + z} run function mg:gta/heli_spawn {{c:"{col}"}}')
ex, ez = EXIT
S += [f'summon minecraft:marker {ex} 65 {Z + ez} {{Tags:["mg.gta","mg.gexit"]}}',
      f'summon minecraft:block_display {ex - 0.5} 65 {Z + ez - 0.5} {{Tags:["mg.gta"],block_state:{{Name:"minecraft:heavy_weighted_pressure_plate"}}}}',
      f'summon minecraft:text_display {ex + 0.5} 67.2 {Z + ez + 0.5} {{Tags:["mg.gta"],billboard:"center",text:{js({"text": "🚪 Retour au lobby", "color": "gold", "bold": True})},'
      f'background:1073741824,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
      'execute as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=40] at @s run function mg:gta/ped_spawn',
      'scoreboard players set $gsu mg.st 2', 'function mg:gta/dots_init']
w('gta/setup_in', S)

# ---------------------------------------------------------------- kit
BAT = ('item replace entity @s hotbar.0 with minecraft:wooden_sword[item_model="$(m)",unbreakable={},'
       f'custom_name={js({"text": "🏏 Batte de baseball", "color": "gold", "italic": False})},'
       'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:bat",amount:4.0,operation:"add_value",slot:"mainhand"},'
       '{type:"minecraft:attack_knockback",id:"mg:batk",amount:1.0,operation:"add_value",slot:"mainhand"}]]')
w('gta/bat', ['# @s : batte (macro : $(m) = modèle)', '$' + BAT])
w('gta/kit', ['# @s : batte, pistolet', 'clear @s', 'function mg:gun/reset',
              'execute if score $rp mg.st matches 1 run function mg:gta/bat {m:"mg:bat"}',
              'execute unless score $rp mg.st matches 1 run function mg:gta/bat {m:"minecraft:stick"}', G.give(1, 'hotbar.1'),
              'scoreboard players set @s mg.grk 0',
              'function mg:gta/kit_plus',
              'item replace entity @s hotbar.7 with minecraft:warped_fungus_on_a_stick[custom_data={gtahome:1b},item_model="minecraft:oak_door",unbreakable={},'
              f'custom_name={js({"text": "🏠 Retour à la villa", "color": "aqua", "bold": True, "italic": False})},'
              f'lore=[{js({"text": "Clic droit : Neo Hills (pas avec la police aux trousses)", "color": "gray", "italic": False})}]]',
              'item replace entity @s hotbar.8 with minecraft:paper[custom_data={gtamap:1b},item_model="minecraft:filled_map",'
              f'custom_name={js({"text": "🗺 Carte de Neo City", "color": "aqua", "bold": True, "italic": False})},'
              f'lore=[{js({"text": "En main : plan de la ville et ta position", "color": "gray", "italic": False})}]]',
              'effect give @s minecraft:saturation infinite 0 true', 'effect give @s minecraft:resistance 3 4 true'])

# ---------------------------------------------------------------- tick de la session
w('gta/tick', ['# 🚓 Neo City : chaque tick tant qu\'un joueur y est', 'scoreboard players add $gtt mg.st 1',
               # armes : clic (objectif mg.gqs, la survie remet mg.qs à zéro pour les joueurs taggés mg.surv)
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtaphone:1b}] run function mg:gta/phone',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtanitro:1b}] run function mg:gta/nitro',
               'execute as @a[tag=mg.gtw,scores={mg.gmis=1..}] run function mg:gta/mis_cmd',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gnit=1..}] mg.gnit 1',
               'execute as @a[tag=mg.gtw,scores={mg.gcas=1..}] at @s run function mg:gta/cas_cmd',
               'execute as @a[tag=mg.gslot] at @s run function mg:gta/cas_slot_anim',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gcre=1..}] mg.gcre 1',
               'execute as @a[tag=mg.gtw,scores={mg.gcre=1}] run function mg:gta/cas_reopen_tick',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/panic',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] at @s if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] run function mg:gta/rpg_fire',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtahome:1b}] run function mg:gta/home',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] at @s run function mg:gun/use',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/panic',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/panic',
               'scoreboard players reset @a[scores={mg.gqs=1..}] mg.gqs',
               'execute as @e[type=minecraft:marker,tag=mg.gtraf] at @s run function mg:gta/traffic/tick',
               'execute as @e[type=minecraft:interaction,tag=mg.gcint] if data entity @s interaction run function mg:gta/car_int',
               'execute as @e[type=minecraft:interaction,tag=mg.gtint] if data entity @s interaction run function mg:gta/traffic/int',
               'execute as @e[type=minecraft:marker,tag=mg.gphel] at @s run function mg:gta/pheli_tick',
               'function mg:gta/panic_tick',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gcd=1..}] mg.gcd 1',
               'execute as @a[tag=mg.gtw,scores={mg.grl=1..}] at @s run function mg:gun/reload_tick',
               'execute as @a[tag=mg.gtw,scores={mg.gsn=1..}] at @s run function mg:gun/sneak',
               'scoreboard players reset @a[tag=mg.gtw,scores={mg.gsn=1..}] mg.gsn',
               # barre de durabilité (recharge de l'arme en main, cadence du Sniper) ; mg_gun exclut le bazooka (rpg:1b seul), sans chargeur
               'execute as @a[tag=mg.gtw] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/bar',
               'execute as @a[tag=mg.gtw] unless items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/bar_clear',
               'execute as @a[tag=mg.gscope] unless items entity @s weapon.mainhand *[custom_data~{gun:5}] run function mg:gta/unscope',
               'execute as @a[tag=mg.gscope,tag=!mg.gads] run function mg:gta/unscope',
               'execute as @e[type=minecraft:item_display,tag=mg.grkt] at @s run function mg:gta/rocket_tick',
               # interface
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gtl=1..}] mg.gtl 1',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gal=1..}] mg.gal 1',
               'scoreboard players operation $gq2 mg.st = $gtt mg.st', 'scoreboard players set #2 mg.st 2', 'scoreboard players operation $gq2 mg.st %= #2 mg.st',
               'execute if score $gq2 mg.st matches 0 if score $rp mg.st matches 1 as @a[tag=mg.gtw,scores={mg.gtl=..0}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/aim',
               'execute if score $gq2 mg.st matches 0 if score $rp mg.st matches 1 as @a[tag=mg.gtw,scores={mg.gtl=..0}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/aim',
               # véhicules, police
               'execute as @e[type=minecraft:horse,tag=mg.gcarh] at @s run function mg:gta/car_sync',
               'execute as @e[type=minecraft:happy_ghast,tag=mg.ghel] at @s run function mg:gta/heli_sync',
               'scoreboard players operation $gq mg.st = $gtt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $gq mg.st %= #20 mg.st',
               'execute if score $gq mg.st matches 0 as @e[tag=mg.gcop] at @s if entity @a[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] run function mg:gta/cop_fire',
               'execute if score $gq mg.st matches 10 as @e[tag=mg.gcop] at @s if entity @a[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] run function mg:gta/cop_fire',
               # crimes, morts
               'execute as @a[tag=mg.gtw,scores={mg.gkp=1..}] run function mg:gta/kill_player',
               'execute as @a[tag=mg.gtw,scores={mg.gkv=1..}] run function mg:gta/kill_ped',
               'execute as @a[tag=mg.gtw,scores={mg.gks=1..}] run function mg:gta/kill_cop',
               'execute as @a[tag=mg.gtw,scores={mg.gkw=1..}] run function mg:gta/kill_cop',
               f'execute as @a[tag=mg.gtw,scores={{mg.deaths=1..}}] in {DIM} run function mg:gta/wasted',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gwt=1..}] mg.gwt 1',
               'execute as @a[tag=mg.gtw,scores={mg.gwl=1..,mg.gwt=0}] run function mg:gta/wanted_down',
               # ramassages, sortie
               'execute as @e[type=minecraft:item_display,tag=mg.gpdi] at @s run tp @s ~ ~ ~ ~5 ~',
               'execute as @e[type=minecraft:item_display,tag=mg.gcash,tag=!mg.gbill] at @s run tp @s ~ ~ ~ ~4 ~',
               'execute as @a[tag=mg.gtw] at @s as @e[type=minecraft:item_display,tag=mg.gcash,distance=..1.6,limit=1] run function mg:gta/cash_take',
               'execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.gexit,distance=..1.3] in minecraft:overworld run function mg:gta/leave',
               'scoreboard players operation $gq5t mg.st = $gtt mg.st', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $gq5t mg.st %= #5 mg.st',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/rob',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/rob',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,scores={mg.grob=1..}] unless predicate mg:sneak run function mg:gta/rob_stop',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,scores={mg.gmt=1..}] at @s run function mg:gta/mis_tick',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak at @s if entity @e[type=minecraft:marker,tag=mg.gtraf,distance=..2.6] run function mg:gta/traffic/steal_near',
               'scoreboard players operation $gq4 mg.st = $gtt mg.st', 'scoreboard players set #4 mg.st 4', 'scoreboard players operation $gq4 mg.st %= #4 mg.st',
               'execute if score $gq4 mg.st matches 0 as @a[tag=mg.gtw] if items entity @s weapon.mainhand *[custom_data~{gtamap:1b}] run function mg:gta/map_show',
               'execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.glup,distance=..0.8] in mg:gta run function mg:gta/lift_up',
               'execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.gldn,distance=..0.8] in mg:gta run function mg:gta/lift_down',
               'execute if score $gq mg.st matches 0 run function mg:gta/second',
               'execute if score $gq mg.st matches 0 run function mg:gta/pads',
               'execute if score $gq mg.st matches 10 run function mg:gta/pads',
               'execute if score $gq mg.st matches 0 run function mg:gta/club_tick', 'execute if score $gq mg.st matches 10 run function mg:gta/club_tick',
               'execute if score $gq mg.st matches 5 run function mg:gta/hud',
               'execute if score $gq mg.st matches 5 run function mg:gta/radio_check',
               'execute if score $gq mg.st matches 15 run function mg:gta/hud'])
w('gta/second', ['# Chaque seconde : véhicules détruits, passants, police, sirènes, valises, ménage',
                 'execute unless score $gsu mg.st matches 1.. run return 0',
                 'execute if score $gsu mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.gvb,tag=!mg.gok] at @s run function mg:gta/wreck',
                 'execute if score $gsu mg.st matches 1 run kill @e[type=minecraft:block_display,tag=mg.gvd,tag=!mg.gok]',
                 'execute if score $gsu mg.st matches 1 run kill @e[type=minecraft:interaction,tag=mg.gcint,tag=!mg.gok]',
                 'tag @e[tag=mg.gok] remove mg.gok', 'scoreboard players set $gsu mg.st 1',
                 'execute store result score $gpn mg.st if entity @e[type=minecraft:villager,tag=mg.gped]',
                 'execute if score $gpn mg.st matches ..39 as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/ped_spawn',
                 'execute if score $gpn mg.st matches ..30 as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/ped_spawn',
                 'team join mg_gciv @a[tag=mg.gtw,scores={mg.gwl=0}]', 'team leave @a[tag=mg.gtw,scores={mg.gwl=1..}]',
                 'scoreboard players operation $gq3 mg.st = $gtt mg.st', 'scoreboard players set #40 mg.st 40', 'scoreboard players operation $gq3 mg.st %= #40 mg.st',
                 'execute store result score $gca mg.st if entity @e[tag=mg.gcop]',
                 'execute if score $gq3 mg.st matches 0 if score $gca mg.st matches ..44 as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/police_call',
                 'execute if score $gq3 mg.st matches 0 as @e[tag=mg.gcop,tag=!mg.gphel] at @s unless entity @a[tag=mg.gtw,scores={mg.gwl=1..},distance=..60] run function mg:gta/cop_leave',
                 'execute if score $gq3 mg.st matches 0 as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/police_plus',
                 'function mg:gta/police_clean', 'function mg:gta/traffic/second',
                 'scoreboard players operation $gq10 mg.st = $gtt mg.st', 'scoreboard players set #200 mg.st 200', 'scoreboard players operation $gq10 mg.st %= #200 mg.st',
                 f'execute if score $gq10 mg.st matches 0 in {DIM} run kill @e[type=minecraft:item,{AREA}]',
                 f'execute if score $gq10 mg.st matches 0 in {DIM} run kill @e[type=minecraft:item,x={NA[0] - 2},y=50,z={Z + NA[1] - 2},dx={NA[2] - NA[0] + 4},dy=60,dz={NA[3] - NA[1] + 12}]',
                 'execute as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/siren',
                 'function mg:gta/bars_tick', 'scoreboard players enable @a[tag=mg.gtw] mg.gmis',
                 'execute as @e[type=minecraft:marker,tag=mg.gshop,scores={mg.gpc=1..20}] run function mg:gta/shop_reopen',
                 'scoreboard players remove @e[type=minecraft:marker,tag=mg.gshop,scores={mg.gpc=1..}] mg.gpc 20',
                 'execute as @e[type=minecraft:marker,tag=mg.gbank,scores={mg.gpc=1..20}] run function mg:gta/bank_reopen',
                 'scoreboard players remove @e[type=minecraft:marker,tag=mg.gbank,scores={mg.gpc=1..}] mg.gpc 20',
                 'scoreboard players operation $gq5 mg.st = $gtt mg.st', 'scoreboard players set #300 mg.st 300', 'scoreboard players operation $gq5 mg.st %= #300 mg.st',
                 'execute store result score $gcn mg.st if entity @e[type=minecraft:item_display,tag=mg.gcash]',
                 'execute if score $gq5 mg.st matches 0 if score $gcn mg.st matches ..3 at @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] run function mg:gta/cash_spawn',
                 'execute store result score $gvc mg.st if entity @e[type=minecraft:horse,tag=mg.gcarh]',
                 'execute if score $gq5 mg.st matches 100 if score $gvc mg.st matches ..15 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..20] run function mg:gta/car_random',
                 'execute if score $gq5 mg.st matches 200 if score $gvc mg.st matches ..15 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..20] run function mg:gta/car_random',
                 'execute store result score $ghc mg.st if entity @e[type=minecraft:happy_ghast,tag=mg.ghel]',
                 'execute if score $gq5 mg.st matches 0 if score $ghc mg.st matches ..3 run function mg:gta/heli_random',
                 'execute as @a[tag=mg.gtw] at @s if entity @s[y=0,dy=60] run function mg:gta/place',
                 f'execute in {DIM} run kill @e[type=#minecraft:arrows,{AREA},nbt={{inGround:1b}}]'])

# ---------------------------------------------------------------- viseur, lunette, radio, étoiles
w('gta/aim', ['# @s tient une arme : viseur au centre, rouge si une cible est dans la ligne de mire (48 blocs) ; sniper en visée (clic droit) : lunette',
              'execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] if entity @s[tag=mg.gads] run return run function mg:gta/scope',
              'scoreboard players set $ga mg.st 0', 'scoreboard players set $gar mg.st 48', 'tag @s add mg.gaim',
              'execute anchored eyes positioned ^ ^ ^1 run function mg:gta/aim_ray', 'tag @s remove mg.gaim',
              'title @s times 0 5 2',
              'execute if score $ga mg.st matches 0 run title @s title ' + js({'text': RET_W, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0}),
              'execute if score $ga mg.st matches 1 run title @s title ' + js({'text': RET_R, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0})])
w('gta/aim_ray', ['# Un pas (1 bloc) de la ligne de mire',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return 0',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 if entity @e[tag=mg.gtg,tag=!mg.gaim,dx=0,dy=0,dz=0] run return run scoreboard players set $ga mg.st 1',
                  'scoreboard players remove $gar mg.st 1',
                  'execute if score $gar mg.st matches 1.. positioned ^ ^ ^1 run function mg:gta/aim_ray'])
w('gta/scope', ['# @s vise à la lunette (sniper, clic droit) : cache noir, zoom (lenteur = champ de vision réduit)',
                'tag @s add mg.gscope', 'title @s times 0 5 2', 'title @s title ' + js({'text': SCOPE, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0}),
                'effect give @s minecraft:slowness 1 6 true'])
w('gta/unscope', ['# @s quitte la lunette', 'tag @s remove mg.gscope', 'effect clear @s minecraft:slowness', 'title @s clear'])
w('gta/radio_check', ['# Toutes les 0,5 s : la radio s\'allume en montant dans une voiture ou un hélico, s\'éteint en descendant',
                      'execute as @e[type=minecraft:horse,tag=mg.gcarh] on passengers run tag @s add mg.gdrn',
                      'execute as @e[type=minecraft:happy_ghast,tag=mg.ghel] on passengers run tag @s add mg.gdrn',
                      'execute as @a[tag=mg.gdrn,tag=!mg.gdrv] at @s run function mg:gta/radio_on',
                      'execute as @a[tag=mg.gdrv,tag=!mg.gdrn] run function mg:gta/radio_off',
                      'tag @a remove mg.gdrn'])
RO = ['# @s monte dans un véhicule : une station au hasard', 'tag @s add mg.gdrv', 'scoreboard players set @s mg.gal 60',
      f'execute store result score $gr mg.st run random value 0..{len(STATIONS) - 1}']
for i, (nm, disc) in enumerate(STATIONS):
    RO += [f'execute if score $gr mg.st matches {i} run playsound minecraft:music_disc.{disc} record @s ~ ~ ~ 0.8 1 0.5',
           f'execute if score $gr mg.st matches {i} run title @s actionbar ' + js([{'text': '📻 ', 'color': 'white'}, {'text': nm, 'color': 'aqua', 'bold': True},
                                                                                {'text': '  ♪', 'color': 'gray'}])]
w('gta/radio_on', RO)
w('gta/radio_off', ['# @s descend : la radio se coupe', 'tag @s remove mg.gdrv', 'stopsound @s record'])
B = ['# Étoiles de recherche : une barre de boss par niveau (1 à 5), haut de l\'écran']
for k in range(1, 6):
    rp = js({'text': THIN.join([STAR_F] * k + [STAR_E] * (5 - k)), 'font': 'mg:gta', 'color': 'white'})
    plain = js([{'text': '★' * k, 'color': 'gold', 'bold': True}, {'text': '☆' * (5 - k), 'color': 'dark_gray', 'bold': True}])
    B += [f'bossbar add mg:gtaw{k} ""', f'bossbar set mg:gtaw{k} color white', f'bossbar set mg:gtaw{k} max 1', f'bossbar set mg:gtaw{k} value 0',
          f'execute if score $rp mg.st matches 1 run bossbar set mg:gtaw{k} name {rp}',
          f'execute unless score $rp mg.st matches 1 run bossbar set mg:gtaw{k} name {plain}']
w('gta/bars', B)
w('gta/bars_tick', ['# Chaque seconde : chaque joueur voit la barre de son niveau'] +
  [f'bossbar set mg:gtaw{k} players @a[tag=mg.gtw,scores={{mg.gwl={k}}}]' for k in range(1, 6)])
w('gta/bars_remove', [f'bossbar remove mg:gtaw{k}' for k in range(1, 6)])
