tag @e[tag=snake_statue_roto,tag=5,tag=target_6,tag=!target_4,distance=0..] add target_11
tag @e[tag=snake_statue_roto,tag=5,tag=target_1,tag=!target_6,distance=0..] add target_22
tag @e[tag=snake_statue_roto,tag=5,tag=target_2,tag=!target_1,distance=0..] add target_44
tag @e[tag=snake_statue_roto,tag=5,tag=target_4,tag=!target_2,distance=0..] add target_66

tag @e[tag=target_11,distance=0..] add target_1
tag @e[tag=target_22,distance=0..] add target_2
tag @e[tag=target_44,distance=0..] add target_4
tag @e[tag=target_66,distance=0..] add target_6

tag @e[tag=target_11,distance=0..] remove target_6
tag @e[tag=target_22,distance=0..] remove target_1
tag @e[tag=target_44,distance=0..] remove target_2
tag @e[tag=target_66,distance=0..] remove target_4

tag @e[tag=target_11,distance=0..] remove target_11
tag @e[tag=target_22,distance=0..] remove target_22
tag @e[tag=target_44,distance=0..] remove target_44
tag @e[tag=target_66,distance=0..] remove target_66

function dungeon:5/totem/refresh
