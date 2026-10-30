function boss:7/hand_position/none
setblock -10446 -48 -387 redstone_block
tag @e[tag=st_hand_dest,distance=0..] add hand_pos_5
execute as @e[tag=st_hand_loc,distance=0..] run function boss:7/hand_frame/idle
schedule clear floaty:sched/boss/7/attack/smack_return
