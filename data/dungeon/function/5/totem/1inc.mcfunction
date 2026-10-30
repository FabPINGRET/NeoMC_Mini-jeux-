tag @e[tag=snake_statue_roto,tag=1,tag=target_2,tag=!target_7,distance=0..] add target_44
tag @e[tag=snake_statue_roto,tag=1,tag=target_4,tag=!target_2,distance=0..] add target_55
tag @e[tag=snake_statue_roto,tag=1,tag=target_5,tag=!target_4,distance=0..] add target_66
tag @e[tag=snake_statue_roto,tag=1,tag=target_6,tag=!target_5,distance=0..] add target_77
tag @e[tag=snake_statue_roto,tag=1,tag=target_7,tag=!target_6,distance=0..] add target_22

tag @e[tag=target_22,distance=0..] add target_2
tag @e[tag=target_44,distance=0..] add target_4
tag @e[tag=target_55,distance=0..] add target_5
tag @e[tag=target_66,distance=0..] add target_6
tag @e[tag=target_77,distance=0..] add target_7

tag @e[tag=target_22,distance=0..] remove target_7
tag @e[tag=target_44,distance=0..] remove target_2
tag @e[tag=target_55,distance=0..] remove target_4
tag @e[tag=target_66,distance=0..] remove target_5
tag @e[tag=target_77,distance=0..] remove target_6

tag @e[tag=target_22,distance=0..] remove target_22
tag @e[tag=target_44,distance=0..] remove target_44
tag @e[tag=target_55,distance=0..] remove target_55
tag @e[tag=target_66,distance=0..] remove target_66
tag @e[tag=target_77,distance=0..] remove target_77

function dungeon:5/totem/refresh
