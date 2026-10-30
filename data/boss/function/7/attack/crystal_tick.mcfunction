execute as @n[tag=st_hand_loc_3,distance=0..] at @s positioned ~ ~-1 ~ run tp @n[tag=st_crystal,distance=0..] ~ ~ ~
execute as @n[tag=st_crystal,distance=0..] at @s run tp @s ~ ~ ~ ~-6 ~

execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 80 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 80 as @n[tag=st_hand_dest_1,distance=0..] run function boss:7/target/stationary

execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 80 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 80 as @n[tag=st_hand_dest_3,distance=0..] run function boss:7/target/stationary

execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 70 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 65 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 60 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 55 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 50 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 45 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 40 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 35 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 30 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 25 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 20 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray
execute as @n[tag=st_hand_loc_1,distance=0..] at @s if score @s Countdown matches 15 rotated as @n[tag=st_hand_draw_1,distance=0..] facing ^ ^ ^-1 positioned ~ ~-1 ~ positioned ^ ^ ^2.5 run function boss:7/utility/crystal_pilot_ray

execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 70 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 65 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 60 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 55 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 50 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 45 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 40 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 35 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 30 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 25 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 20 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=st_hand_loc_3,distance=0..] if score @s Countdown matches 15 at @n[tag=st_crystal,distance=0..] run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 2



execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 70 run scoreboard players set boss:st_prism_color Value 1
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 70 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 70 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 70 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 65 run scoreboard players set boss:st_prism_color Value 2
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 65 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 65 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 65 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 60 run scoreboard players set boss:st_prism_color Value 3
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 60 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 60 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 60 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 55 run scoreboard players set boss:st_prism_color Value 4
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 55 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 55 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 55 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 50 run scoreboard players set boss:st_prism_color Value 5
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 50 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 50 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 50 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 45 run scoreboard players set boss:st_prism_color Value 6
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 45 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 45 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 45 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 40 run scoreboard players set boss:st_prism_color Value 7
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 40 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 40 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 40 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 35 run scoreboard players set boss:st_prism_color Value 8
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 35 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 35 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 35 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 30 run scoreboard players set boss:st_prism_color Value 9
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 30 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 30 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 30 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 25 run scoreboard players set boss:st_prism_color Value 10
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 25 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 25 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 25 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 20 run scoreboard players set boss:st_prism_color Value 11
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 20 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 20 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 20 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray


execute as @n[tag=st_hand_loc_3,distance=0..] at @s if score @s Countdown matches 15 run scoreboard players set boss:st_prism_color Value 12
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 15 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^2 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 15 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^6 run function boss:7/utility/crystal_ray
execute as @n[tag=st_hand_loc_1,distance=0..] if score @s Countdown matches 15 as @n[tag=st_crystal,distance=0..] at @s facing ^ ^-10 ^10 run function boss:7/utility/crystal_ray

