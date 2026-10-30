fill -10470 -22 -375 -10476 -17 -381 lime_stained_glass replace light[level=0]
scoreboard players set boss:st_glass bool 1
execute as @n[tag=st_boss_statue,distance=0..] at @s run tag @a[distance=..3.5,gamemode=!spectator,tag=mg.flw] add st_inside_glass
execute as @n[tag=st_boss_statue,distance=0..] at @s run tag @e[distance=..3.5,tag=knucklehead] add st_inside_glass
execute as @n[tag=st_boss_statue,distance=0..] at @s positioned ^ ^ ^6 positioned ~ -21 ~ run tp @e[tag=st_inside_glass,distance=0..] ~ ~ ~
tag @a[tag=mg.flw] remove st_inside_glass
