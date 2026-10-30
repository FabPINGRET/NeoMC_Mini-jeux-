# DRAW is anchor for drawing boss and faces target, POS is current position of body and faces DEST, DEST is the location POS is trying to move to

summon marker -11223 24 -109 {NoGravity:1b,Silent:1b,Tags:["wm_drone_pos","3"]}

summon marker -11223 24 -109 {NoGravity:1b,Silent:1b,Tags:["wm_drone_dest","3"]}

summon marker -11223 -7 -109 {NoGravity:1b,Silent:1b,Tags:["wm_drone_pivot","3"]}

scoreboard players set @e[tag=wm_drone_pos,distance=0..] Value 0
