# @s (soldat) : onde de choc
tag @s add mg.trsrc
effect give @s minecraft:resistance 5 1
playsound minecraft:entity.generic.explode player @a ~ ~ ~ 1 1.4
particle minecraft:explosion ~ ~1 ~ 2 0.4 2 0 10
particle minecraft:sweep_attack ~ ~1 ~ 3 0.3 3 0 20
execute if score $rk mg.st matches ..2 as @e[tag=mg.tvtg,distance=..6] at @s run function mg:terra/rpg/cl/shock
execute if score $rk mg.st matches 3.. as @e[tag=mg.tvtg,distance=..9] at @s run function mg:terra/rpg/cl/shock
tag @s remove mg.trsrc
