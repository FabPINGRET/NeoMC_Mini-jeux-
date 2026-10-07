execute if score @s mg.t matches 1.. run return run scoreboard players remove @s mg.t 1
tag @s add mg.kcur
execute as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5,limit=1,sort=nearest] run function mg:kart/shell_hit
tag @s remove mg.kcur
