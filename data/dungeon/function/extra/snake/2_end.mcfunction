execute as @e[tag=sc_snake_ride_2,distance=0..] at @s run particle block{block_state:"minecraft:purple_wool"} ~ ~ ~ 0.5 0.5 0.5 0 5 force
execute as @e[tag=sc_snake_ride_2,distance=0..] at @s run fill ~ ~ ~ ~ ~ ~ air replace purple_wool strict
kill @e[tag=sc_snake_ride_2,distance=0..]
tag @a[tag=mg.flw] remove sc_snake_captain_2
