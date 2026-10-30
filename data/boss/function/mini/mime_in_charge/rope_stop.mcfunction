setblock -11665 150 -337 air
fill -11641 149 -341 -11639 149 -339 glass replace stone
execute as @n[tag=mime_stand,distance=0..] at @s run particle minecraft:squid_ink ~ ~1 ~ 0.6 0.6 0.6 0.15 10
execute as @n[tag=mime_stand,distance=0..] at @s run playsound minecraft:entity.squid.squirt hostile @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @n[tag=mime_stand,distance=0..] at @s run tp @s ~ 161 ~

kill @n[tag=mime_cloud,distance=0..]

schedule function floaty:sched/boss/mini/mime_in_charge/appear 1s replace
