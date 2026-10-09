# Chaque seconde : véhicules détruits, passants, police, sirènes, valises, ménage
execute unless score $gsu mg.st matches 1.. run return 0
execute if score $gsu mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.gvb,tag=!mg.gok] at @s run function mg:gta/wreck
execute if score $gsu mg.st matches 1 run kill @e[type=minecraft:block_display,tag=mg.gvd,tag=!mg.gok]
execute if score $gsu mg.st matches 1 run kill @e[type=minecraft:interaction,tag=mg.gcint,tag=!mg.gok]
tag @e[tag=mg.gok] remove mg.gok
scoreboard players set $gsu mg.st 1
execute store result score $gpn mg.st if entity @e[type=minecraft:villager,tag=mg.gped]
execute if score $gpn mg.st matches ..39 as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/ped_spawn
execute if score $gpn mg.st matches ..30 as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/ped_spawn
team join mg_gciv @a[tag=mg.gtw,scores={mg.gwl=0}]
team leave @a[tag=mg.gtw,scores={mg.gwl=1..}]
scoreboard players operation $gq3 mg.st = $gtt mg.st
scoreboard players set #40 mg.st 40
scoreboard players operation $gq3 mg.st %= #40 mg.st
execute store result score $gca mg.st if entity @e[tag=mg.gcop]
execute if score $gq3 mg.st matches 0 if score $gca mg.st matches ..44 as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/police_call
execute if score $gq3 mg.st matches 0 as @e[tag=mg.gcop,tag=!mg.gphel] at @s unless entity @a[tag=mg.gtw,scores={mg.gwl=1..},distance=..60] run function mg:gta/cop_leave
execute if score $gq3 mg.st matches 0 as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/police_plus
function mg:gta/police_clean
function mg:gta/traffic/second
scoreboard players operation $gq10 mg.st = $gtt mg.st
scoreboard players set #200 mg.st 200
scoreboard players operation $gq10 mg.st %= #200 mg.st
execute if score $gq10 mg.st matches 0 in mg:gta run kill @e[type=minecraft:item,x=-90,y=40,z=32310,dx=180,dy=140,dz=180]
execute if score $gq10 mg.st matches 0 in mg:gta run kill @e[type=minecraft:item,x=-46,y=50,z=32222,dx=102,dy=60,dz=96]
execute as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s if entity @e[tag=mg.gcop,distance=..22] run scoreboard players set @s mg.gwt 400
execute as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/siren
function mg:gta/bars_tick
scoreboard players enable @a[tag=mg.gtw] mg.gmis
execute as @e[type=minecraft:marker,tag=mg.gshop,scores={mg.gpc=1..20}] run function mg:gta/shop_reopen
scoreboard players remove @e[type=minecraft:marker,tag=mg.gshop,scores={mg.gpc=1..}] mg.gpc 20
execute as @e[type=minecraft:marker,tag=mg.gbank,scores={mg.gpc=1..20}] run function mg:gta/bank_reopen
scoreboard players remove @e[type=minecraft:marker,tag=mg.gbank,scores={mg.gpc=1..}] mg.gpc 20
scoreboard players operation $gq5 mg.st = $gtt mg.st
scoreboard players set #300 mg.st 300
scoreboard players operation $gq5 mg.st %= #300 mg.st
execute store result score $gcn mg.st if entity @e[type=minecraft:item_display,tag=mg.gcash]
execute if score $gq5 mg.st matches 0 if score $gcn mg.st matches ..3 at @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] run function mg:gta/cash_spawn
execute store result score $gvc mg.st if entity @e[type=minecraft:horse,tag=mg.gcarh]
execute if score $gq5 mg.st matches 100 if score $gvc mg.st matches ..15 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..20] run function mg:gta/car_random
execute if score $gq5 mg.st matches 200 if score $gvc mg.st matches ..15 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..20] run function mg:gta/car_random
execute store result score $ghc mg.st if entity @e[type=minecraft:happy_ghast,tag=mg.ghel]
execute if score $gq5 mg.st matches 0 if score $ghc mg.st matches ..3 run function mg:gta/heli_random
execute as @a[tag=mg.gtw] at @s if entity @s[y=0,dy=60] run function mg:gta/place
execute in mg:gta run kill @e[type=#minecraft:arrows,x=-90,y=40,z=32310,dx=180,dy=140,dz=180,nbt={inGround:1b}]
