# Boîte à objets touchée (@s = boîte) : elle disparaît 3 s, les pilotes sans objet en reçoivent un
tag @s add mg.kboff
scoreboard players set @s mg.t 60
item replace entity @s contents with minecraft:air
execute at @s run playsound minecraft:block.glass.break master @a[tag=mg.play,distance=..16] ~ ~ ~ 0.8 1.4
execute at @s run particle minecraft:wax_on ~ ~0.5 ~ 0.4 0.4 0.4 0 12
execute at @s as @e[type=minecraft:text_display,tag=mg.kboxq,distance=..1.5] run data merge entity @s {text:""}
execute at @s as @a[tag=mg.play,distance=..2.3,scores={mg.kit=0}] run function mg:kart/item_roll
