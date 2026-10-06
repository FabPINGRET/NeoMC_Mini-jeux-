execute unless block ~ ~ ~ #minecraft:air run return 0
execute positioned ~ ~-0.9 ~ as @a[tag=mg.play,distance=..1.0,limit=1] run return run function mg:mobarena/ship/skull_hit
particle minecraft:smoke ~ ~ ~ 0 0 0 0 1
particle minecraft:soul_fire_flame ~ ~ ~ 0 0 0 0 1
scoreboard players remove $rs mg.st 1
execute if score $rs mg.st matches 1.. positioned ^ ^ ^1 run function mg:mobarena/ship/skull_ray
