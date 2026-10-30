execute as @n[tag=st_hand_loc_1,tag=smack_attacking,distance=0..] run function boss:7/rotation_type/freefall
execute as @n[tag=st_hand_loc_2,tag=smack_attacking,distance=0..] run function boss:7/rotation_type/freefall
execute as @n[tag=st_hand_loc_3,tag=smack_attacking,distance=0..] run function boss:7/rotation_type/freefall
execute as @n[tag=st_hand_loc_4,tag=smack_attacking,distance=0..] run function boss:7/rotation_type/freefall

tag @s remove smack_attacking
tag @s remove attacking
setblock -10446 -48 -392 redstone_block
schedule function floaty:sched/boss/7/attack/smack_return 40t replace

execute as @e[tag=st_hand_draw_1,tag=freefall,distance=0..] run data merge entity @s {brightness:{sky:15,block:15}}
execute as @e[tag=st_hand_draw_2,tag=freefall,distance=0..] run data merge entity @s {brightness:{sky:15,block:15}}
execute as @e[tag=st_hand_draw_3,tag=freefall,distance=0..] run data merge entity @s {brightness:{sky:15,block:15}}
execute as @e[tag=st_hand_draw_4,tag=freefall,distance=0..] run data merge entity @s {brightness:{sky:15,block:15}}
