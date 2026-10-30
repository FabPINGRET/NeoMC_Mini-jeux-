execute as @n[tag=mime_stand,distance=0..] at @s run tp @s ~ 164 ~
execute as @n[tag=mime_stand,distance=0..] at @s facing entity @r[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ 0
execute as @n[tag=mime_stand,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 1 1
execute as @n[tag=mime_stand,distance=0..] at @s run particle minecraft:squid_ink ~ ~1 ~ 0.6 0.6 0.6 0.15 10

schedule function floaty:sched/boss/mini/mime_in_charge/chase_lunge_check 15t
