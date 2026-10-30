particle minecraft:explosion ~ ~0.1 ~ 0.2 0.2 0.2 0 5
particle minecraft:copper_fire_flame ~ ~0.1 ~ 0.4 0.4 0.4 0.2 100
playsound minecraft:entity.generic.explode hostile @a[tag=mg.flw] ~ ~ ~ 2 1.2
playsound minecraft:item.lodestone_compass.lock hostile @a[tag=mg.flw] ~ ~ ~ 2 0.1

execute as @a[distance=..1.5,tag=mg.flw] run damage @s 20 minecraft:dragon_breath by @n[tag=knotfire_boss,distance=0..]

kill @e[tag=knotfire_green_fireball,distance=0..]
