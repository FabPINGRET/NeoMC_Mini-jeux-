execute as @n[type=arrow,distance=..2] on origin if entity @s[type=minecraft:player] as @n[tag=st_hand_loc,distance=0..] run tag @s add throwing_arrow
execute as @n[type=arrow,distance=..2] on origin if entity @s[type=minecraft:player] as @n[tag=st_hand_loc,distance=0..] run scoreboard players set @s Countdown 30
execute as @n[type=arrow,distance=..2] on origin if entity @s[type=minecraft:player] as @n[tag=st_hand_loc,distance=0..] run function boss:7/hand_frame/closed
execute as @n[type=arrow,distance=..2] on origin if entity @s[type=minecraft:player] run kill @n[type=arrow,distance=..2]
