execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:red_concrete_powder run function dungeon:8/bot/1/execute/move_forward
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:yellow_concrete_powder run function dungeon:8/bot/1/execute/turn_left
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:lime_concrete_powder run function dungeon:8/bot/1/execute/turn_right
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:purple_concrete_powder run function dungeon:8/bot/1/execute/power_panel

execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:red_concrete_powder run tag @s add read_next
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:yellow_concrete_powder run tag @s add read_next
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:lime_concrete_powder run tag @s add read_next
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:purple_concrete_powder run tag @s add read_next

execute as @n[tag=fs_bot_reader,tag=1,tag=read_next,distance=0..] at @s run tp @s ~ ~ ~-1

tag @e[tag=fs_bot_reader,tag=read_next,distance=0..] remove read_next

execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:red_concrete_powder run schedule function floaty:sched/dungeon/8/bot/1/step 1s replace
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:yellow_concrete_powder run schedule function floaty:sched/dungeon/8/bot/1/step 1s replace
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:lime_concrete_powder run schedule function floaty:sched/dungeon/8/bot/1/step 1s replace
execute as @n[tag=fs_bot_reader,tag=1,distance=0..] at @s if block ~ ~ ~ minecraft:purple_concrete_powder run schedule function floaty:sched/dungeon/8/bot/1/step 1s replace
