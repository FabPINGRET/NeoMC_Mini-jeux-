tag @e[tag=st_hand_loc,distance=0..] remove attacking
tag @e[tag=st_hand_loc,distance=0..] remove summon_attacking


execute as @e[tag=st_hand_dest,distance=0..] run function boss:7/target/none
execute if score boss:st BossHealth >= 4 Value as @e[tag=st_hand_loc,tag=meditate,distance=0..] run function boss:7/hand_frame/idle
execute if score boss:st BossHealth < 4 Value as @e[tag=st_hand_loc,tag=meditate,distance=0..] run function boss:7/hand_frame/point_down

execute if score boss:st BossHealth >= 4 Value as @e[tag=st_hand_loc,tag=point_down,distance=0..] run function boss:7/hand_frame/idle
execute if score boss:st BossHealth < 4 Value as @e[tag=st_hand_loc,tag=point_down,distance=0..] run function boss:7/hand_frame/point_down

execute if score boss:st BossHealth >= 4 Value run function boss:7/hand_position/2
execute if score boss:st BossHealth < 4 Value run function boss:7/hand_position/3

tag @a[tag=mg.flw] remove targeted
function boss:7/body_frame/rotate/new_position_chance
schedule function floaty:sched/boss/7/target_check 3s replace
