tag @n[tag=st_hand_loc_1,distance=0..] remove attacking
tag @n[tag=st_hand_loc_1,distance=0..] remove crystal_attacking

tag @n[tag=st_hand_loc_3,distance=0..] remove attacking
tag @n[tag=st_hand_loc_3,distance=0..] remove crystal_attacking

execute as @e[tag=st_hand_dest,distance=0..] run function boss:7/target/none
execute if score boss:st BossHealth >= 4 Value as @n[tag=st_hand_loc_1,distance=0..] run function boss:7/hand_frame/idle
execute if score boss:st BossHealth >= 4 Value as @n[tag=st_hand_loc_3,distance=0..] run function boss:7/hand_frame/idle

execute if score boss:st BossHealth < 4 Value as @e[tag=st_hand_loc_1,distance=0..] run function boss:7/hand_frame/point_down
execute if score boss:st BossHealth < 4 Value as @e[tag=st_hand_loc_3,distance=0..] run function boss:7/hand_frame/point_down

tag @a[tag=mg.flw] remove targeted
function boss:7/body_frame/rotate/new_position_chance
schedule function floaty:sched/boss/7/target_check 3s replace

kill @e[tag=st_crystal,distance=0..]
