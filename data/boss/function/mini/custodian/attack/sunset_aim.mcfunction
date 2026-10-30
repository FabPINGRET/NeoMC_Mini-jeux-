#CENTER AIM
#execute as @n[tag=custodian_sunset_moon] at @s facing -10441 83 439 run tp @s ~ ~ ~ ~ 0
#PLAYER AIM
execute as @n[tag=custodian_sunset_moon,distance=0..] at @s facing entity @r[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ 0

execute store result score custodian_sunset_moon_delta Value run random value -40..40
execute store result score custodian_sunset_moon_angle Value run data get entity @n[tag=custodian_sunset_moon,distance=0..] Rotation[0] 1
scoreboard players operation custodian_sunset_moon_angle Value += custodian_sunset_moon_delta Value
execute store result entity @n[tag=custodian_sunset_moon,distance=0..] Rotation[0] float 1 run scoreboard players get custodian_sunset_moon_angle Value
