# @s (pilier) : éteint 30 s par un clic
execute if score @s mg.olst matches 1.. run return run data remove entity @s interaction
scoreboard players set @s mg.olst 30
execute at @s run setblock ~ ~4 ~ minecraft:black_stained_glass
execute at @s run playsound minecraft:block.beacon.deactivate master @a ~ ~ ~ 1 1
execute at @s run particle minecraft:electric_spark ~ ~4 ~ 0.4 0.4 0.4 0.2 30
data remove entity @s interaction
