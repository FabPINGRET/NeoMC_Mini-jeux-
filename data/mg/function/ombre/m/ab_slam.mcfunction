# Coup au sol : onde autour du monstre
particle minecraft:explosion ~ ~0.5 ~ 1.5 0.2 1.5 0 6
playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 0.8 0.7
execute as @a[tag=mg.olw,gamemode=adventure,distance=..4] run damage @s 6 minecraft:mob_attack by @e[tag=mg.olm,limit=1,sort=nearest]
effect give @a[tag=mg.olw,gamemode=adventure,distance=..4] minecraft:slowness 2 1
