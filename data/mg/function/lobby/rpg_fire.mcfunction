# @s tire une roquette inoffensive (recharge 1 s)
scoreboard players reset @s mg.qs
execute if score @s mg.lrc matches 1.. run return 0
scoreboard players set @s mg.lrc 20
execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.lrkt","mg.lrkn"],item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}
execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.lrkn] ~ ~ ~ ~ ~
scoreboard players set @e[type=minecraft:item_display,tag=mg.lrkn] mg.gpc 0
tag @e[tag=mg.lrkn] remove mg.lrkn
playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6
playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5
particle minecraft:cloud ~ ~1.4 ~ 0.2 0.2 0.2 0.05 10
