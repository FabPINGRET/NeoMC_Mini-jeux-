execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_1,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_1,distance=0..] ^ ^ ^-1.5
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_1,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_1,distance=0..] ^ ^ ^-1.5
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_1,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_1,distance=0..] ^ ^ ^-1.5

execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_2,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_2,distance=0..] ^ ^ ^-1.5
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_2,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_2,distance=0..] ^ ^ ^-1.5
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_2,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_2,distance=0..] ^ ^ ^-1.5

execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_3,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_3,distance=0..] ^ ^ ^-1.5
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_3,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_3,distance=0..] ^ ^ ^-1.5
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_3,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_3,distance=0..] ^ ^ ^-1.5

execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_4,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_4,distance=0..] ^ ^ ^-1.5
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_4,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_4,distance=0..] ^ ^ ^-1.5
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_4,tag=fist,distance=0..] run tp @n[tag=st_hand_dest_4,distance=0..] ^ ^ ^-1.5

execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_1,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_1,distance=0..] add punch_speed
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_1,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_1,distance=0..] add punch_speed
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_1,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_1,distance=0..] add punch_speed

execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_2,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_2,distance=0..] add punch_speed
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_2,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_2,distance=0..] add punch_speed
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_2,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_2,distance=0..] add punch_speed

execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_3,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_3,distance=0..] add punch_speed
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_3,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_3,distance=0..] add punch_speed
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_3,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_3,distance=0..] add punch_speed

execute unless block ^ ^ ^ air if entity @e[tag=st_hand_loc_4,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_4,distance=0..] add punch_speed
execute if block ^0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_4,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_4,distance=0..] add punch_speed
execute if block ^-0.1 ^ ^ lime_stained_glass if entity @e[tag=st_hand_loc_4,tag=fist,distance=0..] run tag @n[tag=st_hand_dest_4,distance=0..] add punch_speed

setblock -10446 -48 -382 redstone_block

execute positioned ~ -20 ~ if block ^ ^ ^ lime_stained_glass run scoreboard players set boss:st_shatter_glass bool 1
execute positioned ~ -20 ~ if block ^0.1 ^ ^ lime_stained_glass run scoreboard players set boss:st_shatter_glass bool 1
execute positioned ~ -20 ~ if block ^-0.1 ^ ^ lime_stained_glass run scoreboard players set boss:st_shatter_glass bool 1


execute if block ^ ^ ^ air unless block ^-0.1 ^ ^ lime_stained_glass unless block ^0.1 ^ ^ lime_stained_glass positioned ^ ^ ^0.1 run function boss:7/utility/punch_check_ray
