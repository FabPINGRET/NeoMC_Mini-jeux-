execute as @e[tag=stealth_guard,tag=south,distance=0..] at @s run tp @s ~ ~ ~ 0 0
execute as @e[tag=stealth_guard,tag=west,distance=0..] at @s run tp @s ~ ~ ~ 90 0
execute as @e[tag=stealth_guard,tag=north,distance=0..] at @s run tp @s ~ ~ ~ 180 0
execute as @e[tag=stealth_guard,tag=east,distance=0..] at @s run tp @s ~ ~ ~ 270 0

execute if score stealth_cycle bool matches 1 as @e[tag=stealth_guard,tag=rotating,distance=0..] at @s run tp @s ~ ~ ~ ~180 ~

execute if score @n[tag=stealth_guard,tag=target,distance=0..] bool matches 0 as @n[tag=stealth_guard,tag=target,distance=0..] at @s run tp @s ~ ~ ~ 270 0
execute if score @n[tag=stealth_guard,tag=target,distance=0..] bool matches 1 as @n[tag=stealth_guard,tag=target,distance=0..] at @s run tp @s ~ ~ ~ 180 0
