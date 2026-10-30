tag @n[tag=st_hand_loc_1,distance=0..] add attacking
tag @n[tag=st_hand_loc_3,distance=0..] add attacking
tag @n[tag=st_hand_loc_1,distance=0..] add crystal_attacking
tag @n[tag=st_hand_loc_3,distance=0..] add crystal_attacking

execute as @n[tag=st_hand_loc_1,distance=0..] run scoreboard players set @s Countdown 120
execute as @n[tag=st_hand_loc_3,distance=0..] run scoreboard players set @s Countdown 120

execute as @n[tag=st_hand_loc_1,distance=0..] run function boss:7/hand_frame/gun
execute as @n[tag=st_hand_loc_3,distance=0..] run function boss:7/hand_frame/crystal

execute as @n[tag=st_hand_dest_1,distance=0..] run function boss:7/target/crystal_strafe
execute as @n[tag=st_hand_dest_3,distance=0..] run function boss:7/target/crystal_strafe

function boss:7/rotation_type/crystal_rotation

function boss:7/summon_crystal

playsound minecraft:entity.ravager.attack hostile @a[tag=mg.flw] -10473 -20 -378 2 0.5
