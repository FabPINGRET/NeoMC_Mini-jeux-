# Neo GTA, dollars, crimes, recherche, police (cop / swat), points d'armes, lance-roquettes : exécuté par gen_gta.py (exec) à sa place d'origine.
# Utilise : BASE, COPS_FOR, G, GUNM, js, NAMES, PAD, PRICE, TR, VTYPES, w

# ---------------------------------------------------------------- dollars, crimes, recherche
def money(n, why, col='green'):
    return [f'scoreboard players add @s mg.gta {n}',
            f'title @s actionbar [{{"text":"+{n} $ ","color":"{col}","bold":true}},{{"text":"{why}","color":"gray"}}]',
            'execute at @s run playsound minecraft:block.note_block.bit player @s ~ ~ ~ 0.7 1.6', 'scoreboard players set @s mg.gal 40']


w('gta/kill_player', ['# @s a tué un joueur'] + money(100, 'joueur éliminé') + ['scoreboard players remove @s mg.gkp 1',
                      'execute if score @s mg.gkp matches 1.. run function mg:gta/kill_player'])
w('gta/kill_ped', ['# @s a tué un passant : +5 $, une étoile de plus'] + money(5, 'passant', 'yellow') +
  ['scoreboard players remove @s mg.gkv 1', 'function mg:gta/wanted_up', 'execute if score @s mg.gkv matches 1.. run function mg:gta/kill_ped'])
w('gta/kill_cop', ['# @s a tué un policier : +25 $, une étoile de plus'] + money(25, 'policier abattu', 'aqua') +
  ['scoreboard players reset @s mg.gks', 'scoreboard players reset @s mg.gkw', 'function mg:gta/wanted_up'])
w('gta/wanted_up', ['# @s : une étoile de plus (5 max), 15 s avant de redescendre',
                    'execute if score @s mg.gwl matches ..4 run scoreboard players add @s mg.gwl 1', 'scoreboard players set @s mg.gwt 300',
                    'team leave @s',
                    'execute at @s run playsound minecraft:block.note_block.pling player @s ~ ~ ~ 0.8 0.6',
                    'execute at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.6 1.8'])
w('gta/wanted_down', ['# @s : toutes les 15 s, une étoile de moins', 'scoreboard players remove @s mg.gwl 1', 'scoreboard players set @s mg.gwt 300',
                      'execute if score @s mg.gwl matches 0 run team join mg_gciv @s',
                      'execute if score @s mg.gwl matches 0 run scoreboard players set @s mg.gal 40',
                      'execute if score @s mg.gwl matches 0 run title @s actionbar {"text":"☆ La police a perdu ta trace","color":"green"}'])
w('gta/wasted', ['# @s est mort (contexte : dimension mg:gta) : WASTED, ou BUSTED s\'il était recherché ; -25 % lâchés en liasse',
                 'scoreboard players set @s mg.deaths 0', 'scoreboard players set @s mg.gtl 60',
                 'execute if score @s mg.gwl matches 1.. run tag @s add mg.gbust',
                 'scoreboard players operation $gl mg.st = @s mg.gta', 'scoreboard players set #4 mg.st 4', 'scoreboard players operation $gl mg.st /= #4 mg.st',
                 'scoreboard players operation @s mg.gta -= $gl mg.st',
                 'title @s times 5 45 15',
                 'execute if score @s mg.gwl matches 1.. run title @s title {"text":"BUSTED","color":"#4A7BD8","bold":true}',
                 'execute if score @s mg.gwl matches 1.. run title @s subtitle [{"text":"-","color":"#4A7BD8"},{"score":{"name":"$gl","objective":"mg.st"},"color":"#4A7BD8"},{"text":" $ (caution)","color":"gray"}]',
                 'execute unless score @s mg.gwl matches 1.. run title @s title {"text":"WASTED","color":"#C8102E","bold":true}',
                 'execute unless score @s mg.gwl matches 1.. run title @s subtitle [{"text":"-","color":"#C8102E"},{"score":{"name":"$gl","objective":"mg.st"},"color":"#C8102E"},{"text":" $ (frais d\'hôpital)","color":"gray"}]',
                 'scoreboard players set @s mg.gwl 0', 'scoreboard players set @s mg.gwt 0', 'team join mg_gciv @s',
                 'execute if score $gl mg.st matches 1.. run function mg:gta/drop_cash',
                 'function mg:gta/mis_fail', 'function mg:gta/radio_off', 'function mg:gta/unscope', 'function mg:gta/respawn_at', 'function mg:gta/kit',
                 'execute at @s run playsound minecraft:entity.wither.death player @s ~ ~ ~ 0.4 1.6',
                 'execute at @s run playsound minecraft:block.bell.resonate player @s ~ ~ ~ 0.8 0.5'])
w('gta/drop_cash', ['# @s vient de mourir : les dollars perdus ($gl) tombent en liasse là où il est mort',
                    'data modify storage mg:gta d set value {x:0,y:0,z:0}',
                    'execute store result storage mg:gta d.x int 1 run data get entity @s LastDeathLocation.pos[0]',
                    'execute store result storage mg:gta d.y int 1 run data get entity @s LastDeathLocation.pos[1]',
                    'execute store result storage mg:gta d.z int 1 run data get entity @s LastDeathLocation.pos[2]',
                    'scoreboard players operation $gcv mg.st = $gl mg.st', 'function mg:gta/drop_cash_at with storage mg:gta d'])
w('gta/drop_cash_at', ['# Liasse à la position de la mort (macro : $(x) $(y) $(z))',
                       '$execute positioned $(x) $(y) $(z) align xyz positioned ~0.5 ~0.8 ~0.5 run function mg:gta/cash_new'])
w('gta/siren', ['# @s est recherché : sirène (deux tons) et lumières', 'scoreboard players operation $gs mg.st = $gtt mg.st',
                'scoreboard players set #40 mg.st 40', 'scoreboard players operation $gs mg.st %= #40 mg.st',
                'execute if score $gs mg.st matches 0 run playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 1.2 1.4',
                'execute if score $gs mg.st matches 20 run playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 1.2 1.0',
                'execute if score @s mg.gwl matches 3.. run particle minecraft:dust{color:[0.1,0.3,1.0],scale:1.5} ~ ~2.4 ~ 0.3 0.1 0.3 0 3',
                'execute if score @s mg.gwl matches 3.. run particle minecraft:dust{color:[1.0,0.1,0.1],scale:1.5} ~ ~2.4 ~ 0.3 0.1 0.3 0 3'])

# ---------------------------------------------------------------- police
PC = [f'# @s est recherché : renforts toutes les 2 s tant qu\'il y a moins de policiers que voulu dans les 40 blocs {COPS_FOR}',
      'execute store result score $gc mg.st if entity @e[tag=mg.gcop,distance=..40]']
PC += [f'execute if score @s mg.gwl matches {k} run scoreboard players set $gw mg.st {v}' for k, v in COPS_FOR.items()]
PC += ['execute if score $gc mg.st >= $gw mg.st run return 0',
       'execute as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn',
       'execute if score @s mg.gwl matches 2.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn',
       'execute if score @s mg.gwl matches 5 as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn',
       'execute if score @s mg.gwl matches 3.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn',
       'execute if score @s mg.gwl matches 4.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn',
       'execute if score @s mg.gwl matches 5 as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn']
w('gta/police_call', PC)


def cop(model):
    return ('summon minecraft:skeleton ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcop","mg.npc","mg.gcopn"],PersistenceRequired:1b,'
            'CustomName:{"text":"Policier","color":"blue"},'
            'equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":1981031}},'
            'legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":1981031}},feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":1315860}},'
            f'mainhand:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"{model}"}}}}}},'
            'drop_chances:{head:0f,chest:0f,legs:0f,feet:0f,mainhand:0f},attributes:[{id:"minecraft:movement_speed",base:0.28}]}')


def swat(model):
    return ('summon minecraft:wither_skeleton ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcop","mg.gswat","mg.npc","mg.gcopn"],PersistenceRequired:1b,'
            'CustomName:{"text":"SWAT","color":"dark_gray","bold":true},'
            'equipment:{head:{id:"minecraft:netherite_helmet",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":1315860}},'
            'legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":1315860}},'
            f'mainhand:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"{model}"}}}}}},'
            'drop_chances:{head:0f,chest:0f,legs:0f,mainhand:0f},attributes:[{id:"minecraft:movement_speed",base:0.3}]}')


w('gta/cop_spawn', ['# Arrivée de deux policiers armés à ce carrefour (gyrophare)',
                    'execute if score $rp mg.st matches 1 run ' + cop('mg:gun_pistol'),
                    'execute if score $rp mg.st matches 1 positioned ~1 ~ ~ run ' + cop('mg:gun_pistol'),
                    'execute unless score $rp mg.st matches 1 run ' + cop('minecraft:crossbow'),
                    'execute unless score $rp mg.st matches 1 positioned ~1 ~ ~ run ' + cop('minecraft:crossbow'),
                    'team join mg_gciv @e[tag=mg.gcopn]', 'tag @e[tag=mg.gcopn] remove mg.gcopn',
                    'particle minecraft:dust{color:[0.1,0.3,1.0],scale:2} ~ ~2 ~ 0.6 0.3 0.6 0 12',
                    'particle minecraft:dust{color:[1.0,0.1,0.1],scale:2} ~ ~2 ~ 0.6 0.3 0.6 0 12',
                    'playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 2 1.4'])
w('gta/swat_spawn', ['# SWAT (3 ★ et plus) : deux agents au fusil',
                     'execute if score $rp mg.st matches 1 run ' + swat('mg:gun_rifle'),
                     'execute if score $rp mg.st matches 1 positioned ~ ~ ~1 run ' + swat('mg:gun_rifle'),
                     'execute unless score $rp mg.st matches 1 run ' + swat('minecraft:crossbow'),
                     'execute unless score $rp mg.st matches 1 positioned ~ ~ ~1 run ' + swat('minecraft:crossbow'),
                     'team join mg_gciv @e[tag=mg.gcopn]', 'tag @e[tag=mg.gcopn] remove mg.gcopn',
                     'playsound minecraft:entity.iron_golem.attack hostile @a ~ ~ ~ 2 0.6'])
w('gta/cop_fire', ['# @s (policier) : tire sur le joueur recherché le plus proche s\'il le voit (une chance sur trois toutes les 0,5 s)',
                   'execute store result score $gr mg.st run random value 0..3', 'execute if score $gr mg.st matches 1.. run return 0',
                   'tag @s add mg.gcsh', 'scoreboard players set $gcd2 mg.st 2', 'execute if entity @s[tag=mg.gswat] run scoreboard players set $gcd2 mg.st 3',
                   'execute store result storage mg:gta s.a int 1 run random value -6..6', 'execute store result storage mg:gta s.b int 1 run random value -4..4',
                   'execute if entity @s[tag=mg.gswat] store result storage mg:gta s.a int 1 run random value -4..4',
                   'scoreboard players set $gcr mg.st 56', 'function mg:gta/cop_shot with storage mg:gta s', 'tag @s remove mg.gcsh',
                   'playsound minecraft:entity.firework_rocket.blast hostile @a ~ ~ ~ 1.6 1.7',
                   'execute anchored eyes positioned ^-0.3 ^-0.2 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3'])
w('gta/cop_shot', ['# Balle du policier vers sa cible, écartée de $(a)° / $(b)°',
                   '$execute anchored eyes facing entity @p[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] eyes rotated ~$(a) ~$(b) positioned ^ ^ ^0.8 run function mg:gta/cop_ray'])
w('gta/cop_ray', ['# Un pas (0,5 bloc) de la balle du policier',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return run particle minecraft:smoke ~ ~ ~ 0.05 0.05 0.05 0 2',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 as @a[tag=mg.gtw,gamemode=!spectator,dx=0,dy=0,dz=0,limit=1] run return run function mg:gta/cop_hit',
                  'particle minecraft:crit ~ ~ ~ 0 0 0 0 1',
                  'scoreboard players remove $gcr mg.st 1',
                  'execute if score $gcr mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:gta/cop_ray'])
w('gta/cop_hit', ['# @s touché par une balle de la police',
                  'execute if score $gcd2 mg.st matches 2 run damage @s 2 minecraft:mob_attack by @e[tag=mg.gcsh,limit=1]',
                  'execute if score $gcd2 mg.st matches 3 run damage @s 3 minecraft:mob_attack by @e[tag=mg.gcsh,limit=1]',
                  'particle minecraft:damage_indicator ~ ~1.2 ~ 0.2 0.3 0.2 0 2'])
w('gta/cop_leave', ['# Plus personne de recherché à proximité : le policier s\'en va', 'particle minecraft:poof ~ ~1 ~ 0.3 0.6 0.3 0.02 10', 'execute on vehicle run function mg:gta/veh_remove', 'tp @s ~ -300 ~'])
w('gta/ped_spawn', ['# Un passant sur ce trottoir (habits et prénom au hasard)', 'execute store result score $gr mg.st run random value 0..15'] +
  [f'execute if score $gr mg.st matches {i} run summon minecraft:villager ~ ~ ~ {{Tags:["mg.gta","mg.gtg","mg.gped","mg.npc"],PersistenceRequired:1b,'
   f'VillagerData:{{profession:"minecraft:nitwit",type:"minecraft:{VTYPES[i % len(VTYPES)]}",level:1}},'
   f'CustomName:{{"text":"{nm}","color":"gray"}},CustomNameVisible:0b}}' for i, nm in enumerate(NAMES)])

# ---------------------------------------------------------------- points d'armes
PS = ['# @s (marqueur du point) : objet qui tourne + étiquette']
for t, (n, lab, col, it) in PAD.items():
    if n in GUNM:
        PS.append(f'execute if score @s mg.gpt matches {n} if score $rp mg.st matches 1 run summon minecraft:item_display ~ ~1.1 ~ {{Tags:["mg.gta","mg.gpdi"],'
                  f'item:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"mg:gun_{GUNM[n]}"}}}},'
                  f'teleport_duration:1,glow_color_override:16766720,Glowing:1b,{TR % (0, 0, 0, 1.3, 1.3, 1.3)}}}')
        PS.append(f'execute if score @s mg.gpt matches {n} unless score $rp mg.st matches 1 run summon minecraft:item_display ~ ~1.1 ~ {{Tags:["mg.gta","mg.gpdi"],'
                  f'item:{{id:"{it}",count:1}},teleport_duration:1,glow_color_override:16766720,Glowing:1b,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}')
    else:
        PS.append(f'execute if score @s mg.gpt matches {n} run summon minecraft:item_display ~ ~1.1 ~ {{Tags:["mg.gta","mg.gpdi"],item:{{id:"{it}",count:1}},'
                  f'teleport_duration:1,glow_color_override:16766720,Glowing:1b,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}')
    LBL = [{"text": lab, "color": col, "bold": True}] + ([{"text": f"\n{PRICE[n]} $", "color": "green", "bold": True}] if PRICE.get(n) else []) + \
          ([{"text": "\ngratuit une fois acheté", "color": "gray"}] if n in BASE else [])
    PS.append(f'execute if score @s mg.gpt matches {n} run summon minecraft:text_display ~ ~2 ~ {{Tags:["mg.gta","mg.gpdt"],billboard:"center",'
              f'text:{js(LBL)},background:1073741824,{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}')
w('gta/pad_show', PS)
w('gta/pads', ['# Présentoirs : réassort, achat par le joueur le plus proche (une fois par passage : tag mg.gbz sur le présentoir, retiré quand plus personne n\'est devant)',
               'scoreboard players remove @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=1..}] mg.gpc 10',
               'execute as @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=0}] at @s unless entity @e[type=minecraft:item_display,tag=mg.gpdi,distance=..1.5] run function mg:gta/pad_show',
               'execute as @e[type=minecraft:marker,tag=mg.gpad,tag=mg.gbz] at @s unless entity @a[tag=mg.gtw,gamemode=!spectator,distance=..2] run tag @s remove mg.gbz',
               'execute as @e[type=minecraft:marker,tag=mg.gpad,tag=!mg.gbz,scores={mg.gpc=..0}] at @s if entity @a[tag=mg.gtw,gamemode=!spectator,distance=..1.6] run function mg:gta/pad_take',
               'tag @a remove mg.gbuy'])
w('gta/pad_take', ['# @s (présentoir) : le joueur le plus proche achète (ou prend, si c\'est gratuit)',
                   'scoreboard players operation $gpt mg.st = @s mg.gpt', 'scoreboard players set $gok mg.st 0', 'tag @s add mg.gbz',
                   'execute as @a[tag=mg.gtw,tag=!mg.gbuy,gamemode=!spectator,distance=..1.6,sort=nearest,limit=1] at @s run function mg:gta/pad_buy',
                   'execute unless score $gok mg.st matches 1 run return 0',
                   'scoreboard players set @s mg.gpc 600', 'execute if entity @s[tag=mg.garm] run scoreboard players set @s mg.gpc 40', 'execute if score $gpt mg.st matches 80 run scoreboard players set @s mg.gpc 100',
                   'kill @e[type=minecraft:item_display,tag=mg.gpdi,distance=..1.5]', 'kill @e[type=minecraft:text_display,tag=mg.gpdt,distance=..2.5]',
                   'playsound minecraft:entity.villager.yes player @a ~ ~ ~ 0.6 1.2'])
PB_ = ['# @s : achat du contenu du présentoir ($gpt) si assez de dollars (villa : gratuit si déjà acheté)', 'tag @s add mg.gbuy', 'scoreboard players set $gpr mg.st 0',
       'execute if score $gpt mg.st matches 31..49 run return run function mg:gta/villa_take']
PB_ += [f'execute if score $gpt mg.st matches {n} run scoreboard players set $gpr mg.st {v}' for n, v in PRICE.items() if v]
PB_ += ['execute if score @s mg.gta < $gpr mg.st run scoreboard players set @s mg.gal 40',
        'execute if score @s mg.gta < $gpr mg.st run playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1',
        'execute if score @s mg.gta < $gpr mg.st run return run title @s actionbar [{"text":"💸 Pas assez d\'argent : il faut ","color":"red"},'
        '{"score":{"name":"$gpr","objective":"mg.st"},"color":"gold","bold":true},{"text":" $. Braque des passants, des commerces ou la banque !","color":"red"}]',
        'scoreboard players operation @s mg.gta -= $gpr mg.st', 'scoreboard players set $gok mg.st 1', 'function mg:gta/unlock', 'execute if score $gpt mg.st matches 52..57 run scoreboard players remove $gpt mg.st 50', 'function mg:gta/pad_give',
        'execute if score $gpr mg.st matches 1.. run playsound minecraft:block.note_block.chime player @s ~ ~ ~ 0.8 1.4']
w('gta/pad_buy', PB_)
w('gta/unlock', ['# Achat de $gpt : désormais disponible gratuitement à la villa, pour tout le monde'] +
  [f'execute if score $gpt mg.st matches {b} run data modify storage mg:gta unl.t{b} set value 1b' for b in sorted(set(BASE.values()))] +
  ['execute if score $gpt mg.st matches 2..9 run tellraw @s {"text":"🏠 Débloqué : il est aussi au râtelier de la villa, gratuit pour tous.","color":"aqua"}',
   'execute if score $gpt mg.st matches 21..25 run tellraw @s {"text":"🏠 Débloqué : il est aussi au garage de la villa, gratuit pour tous.","color":"aqua"}'])
VT = ['# @s prend un objet à la villa ($gpt) : seulement s\'il a déjà été acheté une fois']
for v, b in BASE.items():
    VT += [f'execute if score $gpt mg.st matches {v} unless data storage mg:gta unl.t{b} run return run function mg:gta/villa_locked',
           f'execute if score $gpt mg.st matches {v} run scoreboard players set $gpt mg.st {b}']
VT += ['scoreboard players set $gvilla mg.st 1', 'scoreboard players set $gok mg.st 1', 'function mg:gta/pad_give', 'scoreboard players set $gvilla mg.st 0']
w('gta/villa_take', VT)
w('gta/villa_locked', ['# Pas encore acheté', 'scoreboard players set @s mg.gal 50', 'playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1',
                       'title @s actionbar {"text":"🔒 Pas encore acheté : achète-le une fois (armurerie ou concession), il sera ici gratuitement pour tous","color":"red"}'])
GV = ['# @s reçoit le contenu du point ($gpt)']
for t, (n, lab, col, it) in PAD.items():
    msg = f'title @s actionbar {js({"text": lab, "color": col, "bold": True})}'
    GV.append(f'execute if score $gpt mg.st matches {n} run scoreboard players set @s mg.gal 40')
    if n in (2, 3, 4):
        GV += [f'execute if score $gpt mg.st matches {n} run {G.give(n, "hotbar.2")}', f'execute if score $gpt mg.st matches {n} run {msg}']
    elif n in (5, 6):
        GV += [f'execute if score $gpt mg.st matches {n} run {G.give(n, "hotbar.3")}', f'execute if score $gpt mg.st matches {n} run {msg}']
    elif n == 7:
        GV += ['execute if score $gpt mg.st matches 7 run function mg:gta/rpg_give', f'execute if score $gpt mg.st matches 7 run {msg}']
    elif n == 8:
        GV += ['execute if score $gpt mg.st matches 8 run effect give @s minecraft:instant_health 1 2 true',
               'execute if score $gpt mg.st matches 8 run effect give @s minecraft:regeneration 8 1 true', f'execute if score $gpt mg.st matches 8 run {msg}']
    elif n == 9:
        GV += ['execute if score $gpt mg.st matches 9 run item replace entity @s armor.chest with minecraft:iron_chestplate[unbreakable={},'
               f'custom_name={js({"text": "🛡 Gilet pare-balles", "color": "gray", "italic": False})}]',
               'execute if score $gpt mg.st matches 9 run effect give @s minecraft:absorption 60 1 true', f'execute if score $gpt mg.st matches 9 run {msg}']
GV += ['execute if score $gpt mg.st matches 70 run function mg:gta/cas_ui_slot', 'execute if score $gpt mg.st matches 71 run function mg:gta/cas_ui_roulette',
       'execute if score $gpt mg.st matches 72 run function mg:gta/cas_ui_dice',
       'execute if score $gpt mg.st matches 60 run function mg:gta/paint',
       'execute if score $gpt mg.st matches 80 run function mg:gta/atm',
       'execute if score $gpt mg.st matches 11 run effect give @s minecraft:instant_health 1 1 true',
       'execute if score $gpt mg.st matches 11 run title @s actionbar {"text":"✚ Soigné","color":"red","bold":true}']
GV += [f'execute if score $gpt mg.st matches {PAD[t][0]} run function mg:gta/veh_buy {{t:"{t}"}}' for t in ('moto', 'muscle', 'supercar', 'heli', 'plane')]
w('gta/pad_give', GV)
w('gta/atm', ['# @s : distributeur de la planque secrète, 2 000 $ gratuits (toutes les 5 s)',
              'scoreboard players set $gcv mg.st 2000', 'function mg:gta/cash_gain',
              'title @s actionbar [{"text":"💵 +","color":"green","bold":true},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $ ","color":"green","bold":true},{"text":"retirés au distributeur secret","color":"gray"}]',
              'playsound minecraft:block.chain.place player @s ~ ~ ~ 1 0.6', 'playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 1 1.2',
              'particle minecraft:happy_villager ~ ~1.2 ~ 0.4 0.4 0.4 0 12'])

# ---------------------------------------------------------------- lance-roquettes
RPG_BASE = ('minecraft:warped_fungus_on_a_stick[custom_data={rpg:1b},unbreakable={},'
            f'custom_name={js({"text": "🚀 Lance-roquettes", "color": "red", "bold": True, "italic": False})},'
            f'lore=[{js({"text": "Clic droit : tirer une roquette", "color": "gray", "italic": False})},'
            f'{js({"text": "Roquettes : à l\'armurerie (+5)", "color": "dark_gray", "italic": False})}]')
w('gta/rpg_give', ['# @s : lance-roquettes (+5 roquettes, 15 au plus)',
                   f'execute if score $rp mg.st matches 1 run item replace entity @s hotbar.4 with {RPG_BASE},item_model="mg:gun_rpg"]',
                   f'execute unless score $rp mg.st matches 1 run item replace entity @s hotbar.4 with {RPG_BASE},item_model="minecraft:crossbow"]',
                   'scoreboard players add @s mg.grk 5', 'execute if score @s mg.grk matches 16.. run scoreboard players set @s mg.grk 15'])
w('gta/rpg_fire', ['# @s tire une roquette (cadence 1,25 s)', 'scoreboard players reset @s mg.gqs',
                   'execute if score @s mg.gcd matches 1.. run return 0',
                   'execute unless score @s mg.grk matches 1.. run return run title @s actionbar {"text":"🚀 Plus de roquettes : trouve un point 🚀","color":"red"}',
                   'scoreboard players remove @s mg.grk 1', 'scoreboard players set @s mg.gcd 25',
                   'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.grkt","mg.grkn"],'
                   'item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,'
                   'transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}',
                   'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.grkn] ~ ~ ~ ~ ~',
                   'scoreboard players operation @e[type=minecraft:item_display,tag=mg.grkn] mg.bid = @s mg.bid',
                   'scoreboard players set @e[type=minecraft:item_display,tag=mg.grkn] mg.gpc 0',
                   'tag @e[tag=mg.grkn] remove mg.grkn',
                   'playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6',
                   'playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5',
                   'particle minecraft:cloud ~ ~1.4 ~ 0.2 0.2 0.2 0.05 10', 'scoreboard players set @s mg.gal 0'])
w('gta/rocket_tick', ['# @s : roquette en vol (âge mg.gpc, tireur mg.bid) : 3 pas de 0,7 bloc par tick',
                      'scoreboard players add @s mg.gpc 1',
                      'execute if score @s mg.gpc matches 60.. run return run function mg:gta/rocket_boom',
                      'execute at @s run function mg:gta/rocket_step', 'execute if entity @s at @s run function mg:gta/rocket_step',
                      'execute if entity @s at @s run function mg:gta/rocket_step',
                      'particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3', 'particle minecraft:large_smoke ~ ~ ~ 0.1 0.1 0.1 0.01 2'])
w('gta/rocket_step', ['# Un pas de la roquette (@s, à sa position, orientée)',
                      'execute unless block ^ ^ ^0.7 #mg:ray_pass positioned ^ ^ ^0.4 run return run function mg:gta/rocket_boom',
                      'scoreboard players operation $bid mg.st = @s mg.bid',
                      'execute positioned ^ ^ ^0.7 positioned ~ ~-0.9 ~ as @e[tag=mg.gtg,distance=..1.3] unless score @s mg.bid = $bid mg.st run tag @s add mg.grhit',
                      'execute if entity @e[tag=mg.grhit] positioned ^ ^ ^0.7 run return run function mg:gta/rocket_boom',
                      'tp @s ^ ^ ^0.7'])
w('gta/rocket_boom', ['# La roquette explose ici : destruction (rayon 3), 16 dégâts dans un rayon de 4, dollars pour les dégâts matériels',
                      'tag @e[tag=mg.grhit] remove mg.grhit',
                      'scoreboard players operation $bid mg.st = @s mg.bid',
                      'function mg:bomber/boom/r3',
                      'execute as @a[tag=mg.gtw] if score @s mg.bid = $bid mg.st run tag @s add mg.gro',
                      'execute as @e[tag=mg.gtg,distance=..4] run damage @s 16 minecraft:player_explosion by @a[tag=mg.gro,limit=1]',
                      'scoreboard players operation $gm mg.st = $bk mg.st', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $gm mg.st /= #5 mg.st',
                      'scoreboard players operation @a[tag=mg.gro] mg.gta += $gm mg.st',
                      'tag @a remove mg.gro',
                      'particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~ ~ 1.5 1.2 1.5 0.12 40 force',
                      'particle minecraft:large_smoke ~ ~ ~ 1.6 1.2 1.6 0.06 30 force',
                      'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 5 0.8', 'kill @s'])
