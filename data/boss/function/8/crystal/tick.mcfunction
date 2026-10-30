execute as @n[tag=frostbyte_crystal_pos,tag=1,distance=0..] at @s run tp @n[tag=frostbyte_crystal,tag=floating,tag=1,distance=0..] ~ ~ ~
execute as @n[tag=frostbyte_crystal_pos,tag=2,distance=0..] at @s run tp @n[tag=frostbyte_crystal,tag=floating,tag=2,distance=0..] ~ ~ ~
execute as @n[tag=frostbyte_crystal_pos,tag=3,distance=0..] at @s run tp @n[tag=frostbyte_crystal,tag=floating,tag=3,distance=0..] ~ ~ ~
execute as @n[tag=frostbyte_crystal_pos,tag=4,distance=0..] at @s run tp @n[tag=frostbyte_crystal,tag=floating,tag=4,distance=0..] ~ ~ ~

execute as @n[tag=frostbyte_crystal_pos,tag=1,distance=0..] at @s facing entity @n[tag=frostbyte_crystal_loc,tag=1,distance=0..] eyes run tp @s ^ ^ ^0.5
execute as @n[tag=frostbyte_crystal_pos,tag=2,distance=0..] at @s facing entity @n[tag=frostbyte_crystal_loc,tag=2,distance=0..] eyes run tp @s ^ ^ ^0.5
execute as @n[tag=frostbyte_crystal_pos,tag=3,distance=0..] at @s facing entity @n[tag=frostbyte_crystal_loc,tag=3,distance=0..] eyes run tp @s ^ ^ ^0.5
execute as @n[tag=frostbyte_crystal_pos,tag=4,distance=0..] at @s facing entity @n[tag=frostbyte_crystal_loc,tag=4,distance=0..] eyes run tp @s ^ ^ ^0.5

execute as @n[tag=frostbyte_crystal_pos,tag=1,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=1,distance=..0.6] run tag @n[tag=frostbyte_crystal,tag=1,distance=0..] remove floating
execute as @n[tag=frostbyte_crystal_pos,tag=1,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=1,distance=..0.6] run kill @s

execute as @n[tag=frostbyte_crystal_pos,tag=2,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=2,distance=..0.6] run tag @n[tag=frostbyte_crystal,tag=2,distance=0..] remove floating
execute as @n[tag=frostbyte_crystal_pos,tag=2,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=2,distance=..0.6] run kill @s

execute as @n[tag=frostbyte_crystal_pos,tag=3,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=3,distance=..0.6] run tag @n[tag=frostbyte_crystal,tag=3,distance=0..] remove floating
execute as @n[tag=frostbyte_crystal_pos,tag=3,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=3,distance=..0.6] run kill @s

execute as @n[tag=frostbyte_crystal_pos,tag=4,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=4,distance=..0.6] run tag @n[tag=frostbyte_crystal,tag=4,distance=0..] remove floating
execute as @n[tag=frostbyte_crystal_pos,tag=4,distance=0..] at @s if entity @n[tag=frostbyte_crystal_loc,tag=4,distance=..0.6] run kill @s

execute as @n[tag=frostbyte_crystal,tag=1,distance=0..] at @s unless block ~ ~ ~ air unless block ~ ~ ~ light run function boss:8/crystal/strike_1
execute as @n[tag=frostbyte_crystal,tag=2,distance=0..] at @s unless block ~ ~ ~ air unless block ~ ~ ~ light run function boss:8/crystal/strike_2
execute as @n[tag=frostbyte_crystal,tag=3,distance=0..] at @s unless block ~ ~ ~ air unless block ~ ~ ~ light run function boss:8/crystal/strike_3
execute as @n[tag=frostbyte_crystal,tag=4,distance=0..] at @s unless block ~ ~ ~ air unless block ~ ~ ~ light run function boss:8/crystal/strike_4

execute as @e[tag=frostbyte_crystal,tag=main,distance=0..] at @s run particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:1,to_color:[0.039,1.000,0.969]} ~ ~ ~ 0.5 1 0.5 0 2 force
execute as @e[tag=frostbyte_crystal,tag=main,distance=0..] at @s run particle block_crumble{block_state:"ice"} ~ ~ ~ 0.5 1 0.5 0 3 force

execute as @n[tag=frostbyte_crystal,tag=!floating,distance=0..] at @s run tp @s ~ ~-2 ~

execute as @e[tag=frostbyte_crystal,tag=main,distance=0..] at @s run tp @s ~ ~ ~ ~10 ~
