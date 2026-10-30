execute as @e[tag=boss_skt_hole_1,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/1
execute as @e[tag=boss_skt_hole_2,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/2
execute as @e[tag=boss_skt_hole_3,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/3
execute as @e[tag=boss_skt_hole_4,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/4
execute as @e[tag=boss_skt_hole_5,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/5
execute as @e[tag=boss_skt_hole_6,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/6
execute as @e[tag=boss_skt_hole_7,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/7
execute as @e[tag=boss_skt_hole_8,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/8
execute as @e[tag=boss_skt_hole_9,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/9
execute as @e[tag=boss_skt_hole_10,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/10
execute as @e[tag=boss_skt_hole_11,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/11
execute as @e[tag=boss_skt_hole_12,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite/12

function boss:5/tail_to_last

schedule function floaty:sched/boss/5/neutral_anim 1s replace
