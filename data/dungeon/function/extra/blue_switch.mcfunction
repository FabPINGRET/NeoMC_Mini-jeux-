execute as @e[type=snowball,tag=sc_red_block,distance=0..] at @s run setblock ~ ~ ~ air
execute as @e[type=snowball,tag=sc_blue_block,distance=0..] at @s run setblock ~ ~ ~ blue_concrete
execute as @e[type=snowball,tag=sc_red_block_invis,distance=0..] at @s run setblock ~ ~ ~ air
execute as @e[type=snowball,tag=sc_blue_block_invis,distance=0..] at @s run setblock ~ ~ ~ barrier

scoreboard players set sc_color bool 1
