kill @e[tag=wm_drone_pos,tag=1,distance=0..]
kill @e[tag=wm_drone_pivot,tag=1,distance=0..]

tag @e[tag=wm_drone_draw,tag=3,distance=0..] add 1
tag @e[tag=wm_drone_pos,tag=3,distance=0..] add 1
tag @e[tag=wm_drone_pivot,tag=3,distance=0..] add 1
tag @e[tag=wm_drone_part,tag=3,distance=0..] add 1

tag @e[tag=wm_drone_draw,tag=1,distance=0..] remove 3
tag @e[tag=wm_drone_pos,tag=1,distance=0..] remove 3
tag @e[tag=wm_drone_pivot,tag=1,distance=0..] remove 3
tag @e[tag=wm_drone_part,tag=1,distance=0..] remove 3
