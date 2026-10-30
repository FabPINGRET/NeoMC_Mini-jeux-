execute as @e[tag=st_hand_dest,distance=0..] run function boss:7/target/none
execute if score boss:st BossHealth >= 4 Value as @e[tag=st_hand_loc,tag=smack,distance=0..] run function boss:7/hand_frame/idle
execute if score boss:st BossHealth < 4 Value as @e[tag=st_hand_loc,tag=smack,distance=0..] run function boss:7/hand_frame/point_down
tag @a[tag=mg.flw] remove targeted
execute unless score boss:st BossHealth matches 0 run function boss:7/body_frame/rotate/new_position_chance

setblock -10446 -48 -392 air
schedule function floaty:sched/boss/7/target_check 3s replace
