tag @e[tag=boss_skt_hole,distance=0..] remove boss_skt_tail
execute as @e[tag=boss_skt_hole_last,limit=1,distance=0..] at @s run clone -10193 72 457 -10191 76 459 ~-1 ~ ~-1
tag @e[tag=boss_skt_hole_last,limit=1,distance=0..] add boss_skt_tail
