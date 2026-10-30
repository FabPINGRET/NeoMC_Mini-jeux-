tp @n[tag=morbex_sunray_sword,distance=0..] @n[tag=morbex_sunray_sword_loc,distance=0..]

execute as @n[tag=morbex_sunray_sword,distance=0..] at @s rotated as @n[tag=morbex_sunray_sword_loc,distance=0..] run tp @s ~ ~ ~ ~ ~

execute as @n[tag=morbex_sunray_sword_loc,distance=0..] at @s if block ~ ~-0.01 ~ sculk run scoreboard players set @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] ScreenShake 1
execute as @n[tag=morbex_sunray_sword_loc,distance=0..] at @s if block ~ ~-0.01 ~ sculk run setblock -12359 42 339 redstone_block
