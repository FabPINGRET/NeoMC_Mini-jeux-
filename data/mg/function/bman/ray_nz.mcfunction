# Un pas de l'explosion
execute if block ~ ~ ~ minecraft:stone_bricks run return 0
execute if block ~ ~ ~ minecraft:bricks run return run function mg:bman/brk
execute if entity @e[type=minecraft:marker,tag=mg.yb,tag=!mg.yx,distance=..0.5] run return run function mg:bman/chain
function mg:bman/flame
scoreboard players remove $yk mg.st 1
execute if score $yk mg.st matches 1.. positioned ~ ~ ~-1 run function mg:bman/ray_nz
