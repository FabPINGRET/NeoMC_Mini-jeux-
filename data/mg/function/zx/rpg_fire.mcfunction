# @s tire une roquette
scoreboard players reset @s mg.qs
execute if score @s mg.gcd matches 1.. run return 0
scoreboard players set @s mg.gcd 30
execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.zent","mg.zrk","mg.zrkn"],item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}
execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.zrkn] ~ ~ ~ ~ ~
scoreboard players operation @e[type=minecraft:item_display,tag=mg.zrkn] mg.zmo = @s mg.zid
scoreboard players set @e[type=minecraft:item_display,tag=mg.zrkn] mg.zmc 0
tag @e[tag=mg.zrkn] remove mg.zrkn
playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6
playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5
