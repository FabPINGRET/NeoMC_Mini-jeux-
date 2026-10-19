# Tourbillon
scoreboard players operation $d mg.st = $pf mg.st
scoreboard players add $d mg.st 10
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
playsound minecraft:entity.player.attack.sweep player @a ~ ~ ~ 1 0.6
particle minecraft:sweep_attack ~ ~1 ~ 2 0.3 2 0 16
execute as @e[tag=mg.olm,distance=..4.5] at @s run function mg:ombre/cl/k_bash with storage mg:ombre s
function mg:ombre/cl/end
