execute as @e[tag=boss_skt_hole_1,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/1
execute as @e[tag=boss_skt_hole_2,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/2
execute as @e[tag=boss_skt_hole_3,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/3
execute as @e[tag=boss_skt_hole_4,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/4
execute as @e[tag=boss_skt_hole_5,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/5
execute as @e[tag=boss_skt_hole_6,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/6
execute as @e[tag=boss_skt_hole_7,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/7
execute as @e[tag=boss_skt_hole_8,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/8
execute as @e[tag=boss_skt_hole_9,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/9
execute as @e[tag=boss_skt_hole_10,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/10
execute as @e[tag=boss_skt_hole_11,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/11
execute as @e[tag=boss_skt_hole_12,distance=0..] at @s if block ~ ~ ~ minecraft:white_stained_glass run function boss:5/bite_slow/12

function boss:5/tail_to_last

schedule function floaty:sched/boss/5/neutral_anim 1s replace
