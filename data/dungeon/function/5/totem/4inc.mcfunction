tag @e[tag=snake_statue_roto,tag=4,tag=target_1,tag=!target_7,distance=0..] add target_22
tag @e[tag=snake_statue_roto,tag=4,tag=target_2,tag=!target_1,distance=0..] add target_33
tag @e[tag=snake_statue_roto,tag=4,tag=target_3,tag=!target_2,distance=0..] add target_55
tag @e[tag=snake_statue_roto,tag=4,tag=target_5,tag=!target_3,distance=0..] add target_66
tag @e[tag=snake_statue_roto,tag=4,tag=target_6,tag=!target_5,distance=0..] add target_77
tag @e[tag=snake_statue_roto,tag=4,tag=target_7,tag=!target_6,distance=0..] add target_11

tag @e[tag=target_11,distance=0..] add target_1
tag @e[tag=target_22,distance=0..] add target_2
tag @e[tag=target_33,distance=0..] add target_3
tag @e[tag=target_55,distance=0..] add target_5
tag @e[tag=target_66,distance=0..] add target_6
tag @e[tag=target_77,distance=0..] add target_7

tag @e[tag=target_11,distance=0..] remove target_7
tag @e[tag=target_22,distance=0..] remove target_1
tag @e[tag=target_33,distance=0..] remove target_2
tag @e[tag=target_55,distance=0..] remove target_3
tag @e[tag=target_66,distance=0..] remove target_5
tag @e[tag=target_77,distance=0..] remove target_6

tag @e[tag=target_11,distance=0..] remove target_11
tag @e[tag=target_22,distance=0..] remove target_22
tag @e[tag=target_33,distance=0..] remove target_33
tag @e[tag=target_55,distance=0..] remove target_55
tag @e[tag=target_66,distance=0..] remove target_66
tag @e[tag=target_77,distance=0..] remove target_77

function dungeon:5/totem/refresh
