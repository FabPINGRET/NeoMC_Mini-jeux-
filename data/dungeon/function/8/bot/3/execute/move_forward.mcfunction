execute as @n[tag=fs_bot,tag=3,distance=0..] at @s if block ^ ^-1 ^3 sea_lantern run tag @s add can_move
execute as @n[tag=fs_bot,tag=3,distance=0..] at @s if block ^ ^-1 ^3 netherite_block run tag @s add can_move
execute as @n[tag=fs_bot,tag=3,distance=0..] at @s if block ^ ^-1 ^3 lapis_ore run tag @s add can_move

execute as @n[tag=fs_bot,tag=3,tag=can_move,distance=0..] at @s run tp @s ^ ^ ^3

tag @e[tag=fs_bot,distance=0..] remove can_move

function dungeon:8/bot/3/redraw
