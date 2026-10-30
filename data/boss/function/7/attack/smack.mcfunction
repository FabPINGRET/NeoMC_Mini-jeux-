tag @s add attacking
tag @s add smack_attacking
scoreboard players set @s Countdown 100
function boss:7/hand_frame/smack

execute if entity @s[tag=st_hand_loc_1] as @n[tag=st_hand_dest_1,distance=0..] run function boss:7/target/hover_over
execute if entity @s[tag=st_hand_loc_2] as @n[tag=st_hand_dest_2,distance=0..] run function boss:7/target/hover_over
execute if entity @s[tag=st_hand_loc_3] as @n[tag=st_hand_dest_3,distance=0..] run function boss:7/target/hover_over
execute if entity @s[tag=st_hand_loc_4] as @n[tag=st_hand_dest_4,distance=0..] run function boss:7/target/hover_over

playsound minecraft:entity.ravager.attack hostile @a[tag=mg.flw] -10473 -20 -378 2 0.5
