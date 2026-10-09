# @s braque la caisse du commerce : 5 s, alarme ; le caissier lève les mains
scoreboard players add @s mg.grob 5
function mg:gta/rob_bar_shop
execute as @e[type=minecraft:villager,tag=mg.gclerk,distance=..5] at @s run particle minecraft:angry_villager ~ ~2.3 ~ 0.2 0.1 0.2 0 1
execute if score @s mg.grob matches 10 as @e[type=minecraft:villager,tag=mg.gclerk,distance=..5] at @s run playsound minecraft:entity.villager.hurt neutral @a ~ ~ ~ 1 1.4
execute if score @s mg.grob matches 5 run playsound minecraft:block.bell.use master @a ~ ~ ~ 2 1.2
execute if score @s mg.grob matches 50 run playsound minecraft:block.bell.use master @a ~ ~ ~ 2 1.2
execute if score @s mg.grob matches 100.. run function mg:gta/rob_shop_ok
