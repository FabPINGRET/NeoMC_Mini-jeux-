# @s tire une roquette (cadence 1,25 s)
scoreboard players reset @s mg.gqs
execute if score @s mg.gcd matches 1.. run return 0
execute unless score @s mg.grk matches 1.. run return run title @s actionbar {"text":"🚀 Plus de roquettes : trouve un point 🚀","color":"red"}
scoreboard players remove @s mg.grk 1
scoreboard players set @s mg.gcd 25
execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.grkt","mg.grkn"],item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}
execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.grkn] ~ ~ ~ ~ ~
scoreboard players operation @e[type=minecraft:item_display,tag=mg.grkn] mg.bid = @s mg.bid
scoreboard players set @e[type=minecraft:item_display,tag=mg.grkn] mg.gpc 0
tag @e[tag=mg.grkn] remove mg.grkn
playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6
playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5
particle minecraft:cloud ~ ~1.4 ~ 0.2 0.2 0.2 0.05 10
scoreboard players set @s mg.gal 0
