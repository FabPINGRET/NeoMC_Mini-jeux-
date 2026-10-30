execute as @e[tag=st_hand_loc,tag=gun,distance=0..] at @s if score @s Countdown matches 60 run playsound minecraft:entity.illusioner.prepare_blindness hostile @a[tag=mg.flw] ~ ~ ~ 1 0.7

execute as @n[tag=st_hand_loc_1,tag=gun,distance=0..] at @s if score @s Countdown matches 51..60 rotated as @n[tag=st_hand_draw_1,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0,1,0]} ~ ~ ~ 0.3 0.3 0.3 0 2 force
execute as @n[tag=st_hand_loc_1,tag=gun,distance=0..] at @s if score @s Countdown matches 41..50 rotated as @n[tag=st_hand_draw_1,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0.5,1.0,0.5]} ~ ~ ~ 0.2 0.2 0.2 0 2 force
execute as @n[tag=st_hand_loc_1,tag=gun,distance=0..] at @s if score @s Countdown matches 21..40 rotated as @n[tag=st_hand_draw_1,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0.8,1.0,0.8]} ~ ~ ~ 0.1 0.1 0.1 0 1 force
execute as @n[tag=st_hand_loc_1,tag=gun,distance=0..] at @s if score @s Countdown matches 1..20 rotated as @n[tag=st_hand_draw_1,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0.95,1.00,0.95]} ~ ~ ~ 0 0 0 0 1 force
execute as @n[tag=st_hand_loc_1,tag=gun,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_1,tag=gun,distance=0..] at @s if score @s Countdown matches 20 as @n[tag=st_hand_dest_1,distance=0..] run function boss:7/target/stationary

execute as @n[tag=st_hand_loc_2,tag=gun,distance=0..] at @s if score @s Countdown matches 51..60 rotated as @n[tag=st_hand_draw_2,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0,1,0]} ~ ~ ~ 0.3 0.3 0.3 0 2 force
execute as @n[tag=st_hand_loc_2,tag=gun,distance=0..] at @s if score @s Countdown matches 41..50 rotated as @n[tag=st_hand_draw_2,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0.5,1.0,0.5]} ~ ~ ~ 0.2 0.2 0.2 0 2 force
execute as @n[tag=st_hand_loc_2,tag=gun,distance=0..] at @s if score @s Countdown matches 21..40 rotated as @n[tag=st_hand_draw_2,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0.8,1.0,0.8]} ~ ~ ~ 0.1 0.1 0.1 0 1 force
execute as @n[tag=st_hand_loc_2,tag=gun,distance=0..] at @s if score @s Countdown matches 1..20 rotated as @n[tag=st_hand_draw_2,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 run particle dust{scale:1,color:[0.95,1.00,0.95]} ~ ~ ~ 0 0 0 0 1 force
execute as @n[tag=st_hand_loc_2,tag=gun,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_2,tag=gun,distance=0..] at @s if score @s Countdown matches 20 as @n[tag=st_hand_dest_2,distance=0..] run function boss:7/target/stationary


execute as @n[tag=st_hand_loc_3,tag=gun,distance=0..] at @s if score @s Countdown matches 51..60 rotated as @n[tag=st_hand_draw_3,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0,1,0]} ~ ~ ~ 0.3 0.3 0.3 0 2 force
execute as @n[tag=st_hand_loc_3,tag=gun,distance=0..] at @s if score @s Countdown matches 41..50 rotated as @n[tag=st_hand_draw_3,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0.5,1.0,0.5]} ~ ~ ~ 0.2 0.2 0.2 0 2 force
execute as @n[tag=st_hand_loc_3,tag=gun,distance=0..] at @s if score @s Countdown matches 21..40 rotated as @n[tag=st_hand_draw_3,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0.8,1.0,0.8]} ~ ~ ~ 0.1 0.1 0.1 0 1 force
execute as @n[tag=st_hand_loc_3,tag=gun,distance=0..] at @s if score @s Countdown matches 1..20 rotated as @n[tag=st_hand_draw_3,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0.95,1.00,0.95]} ~ ~ ~ 0 0 0 0 1 force
execute as @n[tag=st_hand_loc_3,tag=gun,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_3,tag=gun,distance=0..] at @s if score @s Countdown matches 20 as @n[tag=st_hand_dest_3,distance=0..] run function boss:7/target/stationary

execute as @n[tag=st_hand_loc_4,tag=gun,distance=0..] at @s if score @s Countdown matches 51..60 rotated as @n[tag=st_hand_draw_4,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0,1,0]} ~ ~ ~ 0.3 0.3 0.3 0 2 force
execute as @n[tag=st_hand_loc_4,tag=gun,distance=0..] at @s if score @s Countdown matches 41..50 rotated as @n[tag=st_hand_draw_4,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0.5,1.0,0.5]} ~ ~ ~ 0.2 0.2 0.2 0 2 force
execute as @n[tag=st_hand_loc_4,tag=gun,distance=0..] at @s if score @s Countdown matches 21..40 rotated as @n[tag=st_hand_draw_4,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0.8,1.0,0.8]} ~ ~ ~ 0.1 0.1 0.1 0 1 force
execute as @n[tag=st_hand_loc_4,tag=gun,distance=0..] at @s if score @s Countdown matches 1..20 rotated as @n[tag=st_hand_draw_4,distance=0..] positioned ^ ^0.25 ^-3.9 run particle dust{scale:1,color:[0.95,1.00,0.95]} ~ ~ ~ 0 0 0 0 1 force
execute as @n[tag=st_hand_loc_4,tag=gun,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_4,tag=gun,distance=0..] at @s if score @s Countdown matches 20 as @n[tag=st_hand_dest_4,distance=0..] run function boss:7/target/stationary
