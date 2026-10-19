# Aube sacrée
scoreboard players operation $d mg.st = $pw mg.st
scoreboard players add $d mg.st 20
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
playsound minecraft:ui.toast.challenge_complete player @a ~ ~ ~ 1 0.7
particle minecraft:flash{color:[1.0,0.9,0.5,1.0]} ~ ~1 ~ 0 0 0 0 1 force
particle minecraft:end_rod ~ ~1 ~ 6 2 6 0.1 200 force
effect give @a[tag=mg.olw,distance=..16] minecraft:instant_health 1 2 true
effect give @a[tag=mg.olw,distance=..16] minecraft:regeneration 10 1 true
execute as @e[tag=mg.olm,distance=..10] at @s run function mg:ombre/cl/smite_hit with storage mg:ombre s
function mg:ombre/cl/end
