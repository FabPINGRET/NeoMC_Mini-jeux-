# Boîte touchée (@s = boîte) : elle disparaît 3 s ; les pilotes sans objet dont le kart est tout près en reçoivent un
tag @s add mg.kboff
scoreboard players set @s mg.t 60
item replace entity @s contents with minecraft:air
playsound minecraft:block.glass.break master @a[tag=mg.play,distance=..16] ~ ~ ~ 0.8 1.4
particle minecraft:wax_on ~ ~0.5 ~ 0.4 0.4 0.4 0 12
execute as @e[type=minecraft:text_display,tag=mg.kboxq,distance=..1.5] run data merge entity @s {text:""}
execute as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/owner_roll
