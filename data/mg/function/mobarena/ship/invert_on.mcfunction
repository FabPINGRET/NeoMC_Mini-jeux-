title @a[tag=mg.play] title [{"text":"GRAVITÉ INVERSÉE","color":"light_purple","bold":true}]
title @a[tag=mg.play] subtitle [{"text":"Les shulkers tirent !","color":"gray"}]
effect give @a[tag=mg.play] minecraft:levitation 5 9 true
execute as @a at @s run playsound minecraft:block.beacon.deactivate master @s ~ ~ ~ 1 0.5
execute store result score $sc mg.st if entity @e[type=minecraft:shulker,tag=mg.mob]
execute if score $sc mg.st matches ..9 run function mg:mobarena/ship/shulkers
