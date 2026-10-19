# Chaîne d'éclairs : les 4 ennemis les plus proches (12 blocs)
scoreboard players operation $d mg.st = $pw mg.st
scoreboard players add $d mg.st 12
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
playsound minecraft:item.trident.thunder player @a ~ ~ ~ 0.8 1.6
execute as @e[tag=mg.olm,distance=..12,sort=nearest,limit=4] at @s run function mg:ombre/cl/chain_hit with storage mg:ombre s
function mg:ombre/cl/end
