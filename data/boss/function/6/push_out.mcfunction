execute as @n[tag=boss_sh_loc,distance=0..] at @s as @a[gamemode=!spectator,distance=..4,tag=mg.flw] at @s unless block ~ 64 ~ air run tag @s add sh_push_out
execute as @n[tag=boss_sh_loc,distance=0..] at @s as @e[tag=fungloom,distance=..4] at @s unless block ~ 64 ~ air run tag @s add sh_push_out
execute as @n[tag=boss_sh_loc,distance=0..] at @s run tp @e[tag=sh_push_out,distance=0..] ^2 ^0.5 ^
tag @e[tag=sh_push_out,distance=0..] remove sh_push_out
