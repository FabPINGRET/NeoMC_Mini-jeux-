# Un pas du jet de peinture (0,5 bloc) : bloc plein → éclaboussure ; adversaire touché → touche ; air → on avance (le marqueur mg.rend suit le jet : la traînée s'arrête dessus)
execute unless loaded ~ ~ ~ run return 0
tp @e[type=minecraft:marker,tag=mg.rend,distance=..1,limit=1] ~ ~ ~
execute unless block ~ ~ ~ #minecraft:air run return run function mg:paintball/splat
execute if score $st mg.st matches 1 positioned ~ ~-0.9 ~ as @a[tag=mg.play,team=mg_blue,tag=!mg.prot,distance=..0.95,limit=1,sort=nearest] run return run function mg:paintball/hit
execute if score $st mg.st matches 2 positioned ~ ~-0.9 ~ as @a[tag=mg.play,team=mg_red,tag=!mg.prot,distance=..0.95,limit=1,sort=nearest] run return run function mg:paintball/hit
scoreboard players remove $rs mg.st 1
execute if score $rs mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:paintball/ray
