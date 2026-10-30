execute as @a[gamemode=!spectator,tag=mg.flw] at @s run particle minecraft:dust_color_transition{from_color:[0.000,0.000,0.000],to_color:[0.529,0.000,0.529],scale:3} ~ ~ ~ 0.4 6 0.4 1 100
execute as @a[gamemode=!spectator,tag=mg.flw] at @s run playsound minecraft:block.trial_spawner.ambient_ominous hostile @s ~ ~ ~ 1 2
execute as @a[gamemode=!spectator,tag=mg.flw] at @s run playsound minecraft:block.trial_spawner.detect_player hostile @s ~ ~ ~ 1 2
