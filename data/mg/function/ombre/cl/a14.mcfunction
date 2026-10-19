# Jugement de l'Aube
scoreboard players operation $d mg.st = $pf mg.st
scoreboard players operation $d mg.st *= #2 mg.st
scoreboard players add $d mg.st 24
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
playsound minecraft:item.trident.thunder player @a ~ ~ ~ 1 0.8
playsound minecraft:entity.generic.explode player @a ~ ~ ~ 1 1.2
particle minecraft:flash{color:[1.0,0.85,0.3,1.0]} ~ ~1 ~ 0 0 0 0 1 force
particle minecraft:end_rod ~ ~0.5 ~ 4 0.3 4 0.1 120 force
particle minecraft:totem_of_undying ~ ~1 ~ 2 1 2 0.3 60 force
execute as @e[tag=mg.olm,distance=..7] at @s run function mg:ombre/cl/k_judg with storage mg:ombre s
function mg:ombre/cl/end
