# Frappe du bouclier : cône devant soi
scoreboard players operation $d mg.st = $pf mg.st
scoreboard players add $d mg.st 6
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
playsound minecraft:item.shield.block player @a ~ ~ ~ 1 0.7
execute anchored eyes positioned ^ ^ ^1.8 run particle minecraft:sweep_attack ~ ~-0.3 ~ 0.6 0.2 0.6 0 4
execute positioned ^ ^ ^2 as @e[tag=mg.olm,distance=..2.6] at @s run function mg:ombre/cl/k_bash with storage mg:ombre s
function mg:ombre/cl/end
