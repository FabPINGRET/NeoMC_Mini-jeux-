execute as @n[tag=wahrog_stand,distance=0..] at @s run playsound minecraft:entity.lightning_bolt.thunder hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @n[tag=wahrog_fork_0,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_1,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_2,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_3,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_1a,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_1b,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_2a,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_2b,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1
execute as @n[tag=wahrog_fork_3a,distance=0..] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~ 0 0 0 0 1


scoreboard players set wahrog_shortray Value 30
execute as @n[tag=wahrog_fork_0,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_0
scoreboard players set wahrog_shortray_1 Value 70
execute as @n[tag=wahrog_fork_1,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_1
scoreboard players set wahrog_shortray_1a Value 60
execute as @n[tag=wahrog_fork_1a,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_1a
scoreboard players set wahrog_shortray_1b Value 40
execute as @n[tag=wahrog_fork_1b,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_1b
scoreboard players set wahrog_shortray_2 Value 70
execute as @n[tag=wahrog_fork_2,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_2
scoreboard players set wahrog_shortray_2a Value 40
execute as @n[tag=wahrog_fork_2a,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_2a
scoreboard players set wahrog_shortray_2b Value 30
execute as @n[tag=wahrog_fork_2b,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_2b
scoreboard players set wahrog_shortray_3 Value 70
execute as @n[tag=wahrog_fork_3,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_3
scoreboard players set wahrog_shortray_3a Value 30
execute as @n[tag=wahrog_fork_3a,distance=0..] at @s run function boss:mini/wahrog/attack/forking/damage/ray_3a
