# Un pas du jet de peinture (0,5 bloc) : bloc plein → éclaboussure ; adversaire touché → touche ; air → on avance
execute unless block ~ ~ ~ #minecraft:air run return run function mg:paintball/splat
execute if score $st mg.st matches 1 positioned ~ ~-0.9 ~ as @a[tag=mg.play,team=mg_blue,tag=!mg.prot,distance=..0.95,limit=1,sort=nearest] run return run function mg:paintball/hit
execute if score $st mg.st matches 2 positioned ~ ~-0.9 ~ as @a[tag=mg.play,team=mg_red,tag=!mg.prot,distance=..0.95,limit=1,sort=nearest] run return run function mg:paintball/hit
execute if score $st mg.st matches 1 run particle minecraft:flame ~ ~ ~ 0 0 0 0 1
execute if score $st mg.st matches 2 run particle minecraft:soul_fire_flame ~ ~ ~ 0 0 0 0 1
scoreboard players remove $rs mg.st 1
execute if score $rs mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:paintball/ray
