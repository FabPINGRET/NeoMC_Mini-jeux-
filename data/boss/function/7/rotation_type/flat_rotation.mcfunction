function boss:7/rotation_type/none

execute if entity @s[tag=st_hand_loc_1] run tag @e[tag=st_hand_draw_1,distance=0..] add flat_rotation
execute if entity @s[tag=st_hand_loc_2] run tag @e[tag=st_hand_draw_2,distance=0..] add flat_rotation
execute if entity @s[tag=st_hand_loc_3] run tag @e[tag=st_hand_draw_3,distance=0..] add flat_rotation
execute if entity @s[tag=st_hand_loc_4] run tag @e[tag=st_hand_draw_4,distance=0..] add flat_rotation
