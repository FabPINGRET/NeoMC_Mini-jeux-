# @s ramasse sa caisse : il la porte (ralenti), une meute flaire l'odeur
execute as @e[tag=mg.tvcrate] if score @s mg.tvo = $own mg.st run kill @s
tag @s add mg.tvcar
scoreboard players set @s mg.tvmp 0
effect give @s minecraft:slowness infinite 0 true
summon minecraft:item_display ~ ~2.2 ~ {Tags:["mg.tv","mg.tvcarry","mg.tvn"],teleport_duration:1,item:{id:"minecraft:barrel",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st
tag @e[tag=mg.tvn] remove mg.tvn
function mg:terra/save_pos
function mg:terra/loc {x:0,y:65,z:0}
title @s title {"text":"📦 Caisse récupérée","color":"yellow","bold":true}
title @s subtitle {"text":"Rapporte-la à la colonie !","color":"gray"}
playsound minecraft:block.barrel.open player @s ~ ~ ~ 1 0.8
execute as @e[type=minecraft:marker,tag=mg.tvsp,distance=16..48,sort=nearest,limit=1] at @s run function mg:terra/pack
tellraw @s {"text":"⚠ Des slashers ont flairé la caisse !","color":"red"}
