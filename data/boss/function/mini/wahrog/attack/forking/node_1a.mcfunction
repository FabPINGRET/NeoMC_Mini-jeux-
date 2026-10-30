summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["wahrog_fork_1a","wahrog_node"]}
execute as @n[tag=wahrog_fork_1a,distance=0..] at @s rotated as @n[tag=wahrog_fork_1,distance=0..] run tp @s ~ ~ ~ ~ ~
execute as @n[tag=wahrog_fork_1a,distance=0..] at @s run function boss:mini/wahrog/attack/forking/reangle
scoreboard players set wahrog_shortray_1a Value 60
execute as @n[tag=wahrog_fork_1a,distance=0..] at @s run function boss:mini/wahrog/attack/forking/ray_1a
