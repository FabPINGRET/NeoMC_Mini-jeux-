particle minecraft:end_rod ~ ~ ~ 0 0 0 0 1
scoreboard players remove $rs mg.st 1
execute if score $rs mg.st matches 1.. positioned ^ ^ ^1 run function mg:mobarena/temple/beam_ray
