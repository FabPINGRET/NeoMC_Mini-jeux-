execute as @n[tag=st_hand_loc_1,tag=fist,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_1,tag=fist,distance=0..] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_1,distance=0..] run function boss:7/target/stationary
#execute as @n[tag=st_hand_loc_1,tag=fist] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_1] run tag @s add punch_speed

execute as @n[tag=st_hand_loc_2,tag=fist,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_2,tag=fist,distance=0..] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_2,distance=0..] run function boss:7/target/stationary
#execute as @n[tag=st_hand_loc_2,tag=fist] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_2] run tag @s add punch_speed

execute as @n[tag=st_hand_loc_3,tag=fist,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_3,tag=fist,distance=0..] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_3,distance=0..] run function boss:7/target/stationary
#execute as @n[tag=st_hand_loc_3,tag=fist] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_3] run tag @s add punch_speed

execute as @n[tag=st_hand_loc_4,tag=fist,distance=0..] at @s if score @s Countdown matches 20 run function boss:7/rotation_type/locked
execute as @n[tag=st_hand_loc_4,tag=fist,distance=0..] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_4,distance=0..] run function boss:7/target/stationary
#execute as @n[tag=st_hand_loc_4,tag=fist] at @s if score @s Countdown matches 30 as @n[tag=st_hand_dest_4] run tag @s add punch_speed
