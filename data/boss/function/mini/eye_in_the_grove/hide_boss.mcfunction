execute as @n[tag=g_eye_boss,distance=0..] at @s run particle dust_color_transition{from_color:[0.678,0.678,0.678],to_color:[1.000,0.569,0.000],scale:2} ~ 117 ~ 1 1 1 0 200 normal
execute as @n[tag=g_eye_boss,distance=0..] at @s run playsound minecraft:block.trial_spawner.ominous_activate hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7

scoreboard players set grove_eye_horse_mode Value 0
tp @n[tag=g_eye_boss,distance=0..] -10059 93 337
