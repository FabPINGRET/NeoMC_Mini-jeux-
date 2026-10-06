# Un pas du rayon (0,5 bloc) : bloc plein → fin ; joueur touché → kill ; air → on avance
execute unless block ~ ~ ~ #minecraft:air run return run particle minecraft:electric_spark ~ ~ ~ 0.1 0.1 0.1 0.1 4
execute positioned ~ ~-0.9 ~ as @a[tag=mg.play,tag=!mg.qsh,tag=!mg.prot,tag=!mg.qdd,distance=..0.95,limit=1,sort=nearest] run return run function mg:quake/hit
particle minecraft:end_rod ~ ~ ~ 0 0 0 0 1
scoreboard players remove $rs mg.st 1
execute if score $rs mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:quake/ray
