playsound minecraft:block.trial_spawner.ambient_ominous hostile @a[tag=mg.flw] ~ ~ ~ 3 1

execute store result entity @n[tag=boss_ta_scorn_laser,distance=0..] Rotation[1] float 1 run scoreboard players get boss_ta_scorn_angle Value

execute as @n[tag=boss_ta_scorn_laser,distance=0..] at @s facing ^ ^ ^1 positioned ~ 222 ~ run function boss:10/attack/scorn_beam

execute as @n[tag=boss_ta_scorn_laser,distance=0..] at @s facing ^-0.3 ^ ^1 positioned ~ 222 ~ run function boss:10/attack/scorn_beam
execute as @n[tag=boss_ta_scorn_laser,distance=0..] at @s facing ^0.3 ^ ^1 positioned ~ 222 ~ run function boss:10/attack/scorn_beam


scoreboard players remove boss_ta_scorn_angle Value 5
