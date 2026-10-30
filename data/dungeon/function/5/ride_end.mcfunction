execute as @e[tag=skt_snake_ride,distance=0..] at @s run particle block{block_state:"minecraft:moss_block"} ~ ~ ~ 0.5 0.5 0.5 0 5 force
execute as @e[tag=skt_snake_ride,distance=0..] at @s run fill ~ ~ ~ ~ ~ ~ air replace moss_block
kill @e[tag=skt_snake_ride,distance=0..]
tag @a[tag=mg.flw] remove skt_snake_captain
