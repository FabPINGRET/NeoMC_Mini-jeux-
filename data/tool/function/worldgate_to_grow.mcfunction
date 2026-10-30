execute as @n[tag=worldgate_to_marker,distance=0..] at @s run data merge entity @n[type=item_display,tag=worldgate_to,distance=0..] {start_interpolation:0,interpolation_duration:10,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[3f,3f,3f]}}
schedule function floaty:sched/tool/worldgate_to_end 10t replace
