summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["wahrog_fork_3","wahrog_node"]}
execute as @n[tag=wahrog_fork_3,distance=0..] at @s facing entity @n[tag=targeted,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=wahrog_fork_3,distance=0..] at @s run function boss:mini/wahrog/attack/forking/reangle
scoreboard players set wahrog_shortray_3 Value 70
execute as @n[tag=wahrog_fork_3,distance=0..] at @s run function boss:mini/wahrog/attack/forking/ray_3
