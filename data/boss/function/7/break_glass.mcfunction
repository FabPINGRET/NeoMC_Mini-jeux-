fill -10470 -22 -375 -10476 -17 -381 light[level=0] replace minecraft:lime_stained_glass
scoreboard players set boss:st_glass bool 0
execute as @n[tag=st_boss_statue,distance=0..] at @s positioned ^ ^ ^3 run particle block{block_state:"lime_stained_glass"} ~ ~0.5 ~ 0.5 0.75 0.5 0 100 force
execute as @n[tag=st_boss_statue,distance=0..] at @s positioned ^ ^ ^3 run playsound minecraft:block.glass.break block @a[tag=mg.flw] ~ ~ ~ 1 1
