summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["wahrog_fork_3a","wahrog_node"]}
execute as @n[tag=wahrog_fork_3a,distance=0..] at @s rotated as @n[tag=wahrog_fork_3,distance=0..] run tp @s ~ ~ ~ ~ ~
execute as @n[tag=wahrog_fork_3a,distance=0..] at @s run function boss:mini/wahrog/attack/forking/reangle
scoreboard players set wahrog_shortray_3a Value 30
execute as @n[tag=wahrog_fork_3a,distance=0..] at @s run function boss:mini/wahrog/attack/forking/ray_3a
