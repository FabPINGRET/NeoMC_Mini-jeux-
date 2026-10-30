execute as @n[tag=knotfire_run_dest,distance=0..] at @s rotated as @n[tag=knotfire_statue,tag=active,distance=0..] run tp @s ~ ~ ~ ~ ~

tp @n[tag=knotfire_statue,tag=active,distance=0..] @n[tag=knotfire_run_dest,distance=0..]

kill @e[tag=knotfire_run_dest,distance=0..]

setblock -10696 54 105 redstone_block

#playsound minecraft:entity.bat.takeoff hostile @a -10697 71 89 2 1
playsound minecraft:entity.ender_dragon.flap hostile @a[tag=mg.flw] -10697 71 89 2 1
playsound minecraft:item.lodestone_compass.lock hostile @a[tag=mg.flw] -10697 71 89 3 0.1
playsound minecraft:entity.camel_husk.dash hostile @a[tag=mg.flw] -10697 71 89 3 2
