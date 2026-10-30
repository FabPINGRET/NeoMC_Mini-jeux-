execute if score grove_eye_health Value matches 21..60 run scoreboard players set grove_eye_horse_mode Value 1
execute if score grove_eye_health Value matches 1..20 run scoreboard players set grove_eye_horse_mode Value 2

execute as @n[tag=grove_eye_pivot,distance=0..] at @s run tp @s ~ ~ ~ ~ 0

function boss:mini/eye_in_the_grove/eye_ride

execute as @n[tag=grove_eye_pivot,distance=0..] at @s positioned ^ ^ ^8 run particle dust_color_transition{from_color:[0.678,0.678,0.678],to_color:[1.000,0.569,0.000],scale:2} ~ 117 ~ 1 1 1 0 200 normal
execute as @n[tag=grove_eye_pivot,distance=0..] at @s positioned ^ ^ ^8 run playsound minecraft:block.trial_spawner.ominous_activate hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7
