tp @e[tag=mg.olb_nyxar] ~ ~ ~
particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1 force
playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 2 0.5
execute as @a[tag=mg.olw,gamemode=adventure,distance=..6] run damage @s 16 minecraft:mob_attack by @e[tag=mg.olb_nyxar,limit=1]
kill @s
