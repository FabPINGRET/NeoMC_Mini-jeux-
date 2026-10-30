execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run fill ~-1 ~ ~-1 ~1 ~9 ~1 air
execute as @e[tag=boss_skt_hole_last,limit=1,distance=0..] at @s run clone -10193 72 457 -10191 76 459 ~-1 ~ ~-1

function boss:5/ectobeam/ray_start
