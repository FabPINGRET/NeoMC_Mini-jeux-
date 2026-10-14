# @s : canon sonique, onde en cône (sphère de 4,5 blocs centrée 4 blocs devant)
execute if score @s mg.tvsc matches 1.. run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.4
scoreboard players set @s mg.tvsc 80
playsound minecraft:entity.warden.sonic_boom player @a ~ ~ ~ 1 1.3
execute anchored eyes positioned ^ ^ ^1.5 run particle minecraft:sonic_boom ~ ~ ~ 0 0 0 0 1 force
execute anchored eyes positioned ^ ^ ^3.5 run particle minecraft:sonic_boom ~ ~ ~ 0.4 0.3 0.4 0 2 force
execute anchored eyes positioned ^ ^ ^6 run particle minecraft:sonic_boom ~ ~ ~ 0.9 0.5 0.9 0 3 force
tag @s add mg.tvsrc
execute anchored eyes positioned ^ ^ ^4 as @e[tag=mg.tvd,distance=..4.5] at @s run function mg:terra/sonic_hit
tag @s remove mg.tvsrc
