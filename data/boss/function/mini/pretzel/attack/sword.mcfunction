setblock -10341 89 445 air
tp @n[tag=pretzel_boss,distance=0..] -10341 89 445 -45 0
execute as @n[tag=pretzel_boss,distance=0..] at @s run playsound minecraft:entity.evoker.cast_spell hostile @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute as @n[tag=pretzel_boss,distance=0..] at @s run particle minecraft:firework ~ ~1 ~ 0.5 0.5 0.5 0 70
