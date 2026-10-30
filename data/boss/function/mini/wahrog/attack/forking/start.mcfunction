execute as @n[tag=wahrog_stand,distance=0..] at @s run playsound minecraft:entity.illusioner.prepare_mirror hostile @a[tag=mg.flw] ~ ~ ~ 3 1.5

execute as @n[tag=wahrog_stand,distance=0..] at @s run summon marker ~ ~1 ~ {NoGravity:1b,Silent:1b,Tags:["wahrog_fork_0","wahrog_node"]}
execute as @n[tag=wahrog_fork_0,distance=0..] at @s facing entity @n[tag=targeted,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=wahrog_fork_0,distance=0..] at @s run function boss:mini/wahrog/attack/forking/reangle
scoreboard players set wahrog_shortray Value 30
execute as @n[tag=wahrog_fork_0,distance=0..] at @s run function boss:mini/wahrog/attack/forking/ray_0
