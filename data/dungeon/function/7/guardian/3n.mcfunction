execute as @e[tag=st_guardian,tag=3,distance=0..] at @s run tp @s ~ ~ ~ 180 0

execute as @e[tag=st_guardian,tag=3,distance=0..] at @s unless block ~ ~-1 ~-1 minecraft:chiseled_deepslate if block ~ ~ ~-1 air run tag @s add move_clear_block
execute as @e[tag=st_guardian,tag=3,distance=0..] at @s positioned ~ ~ ~-1 unless entity @e[tag=st_guardian,distance=..0.5] run tag @s add move_clear_statue

execute as @e[tag=st_guardian,tag=3,distance=0..] at @s positioned ~ ~ ~-1 if entity @e[tag=st_guardian,distance=..0.5,tag=move_clear_block,tag=move_clear_statue] run tag @s add move_clear_statue
execute as @e[tag=st_guardian,tag=3,distance=0..] at @s positioned ~ ~ ~-1 if entity @e[tag=st_guardian,distance=..0.5,tag=move_clear_block,tag=move_clear_statue] run tag @s add move_clear_statue

execute as @e[tag=st_guardian,tag=3,tag=move_clear_block,tag=move_clear_statue,distance=0..] at @s run tp @s ~ ~ ~-1
execute as @e[tag=st_guardian,tag=3,tag=move_clear_block,tag=move_clear_statue,distance=0..] at @s run playsound minecraft:block.grindstone.use master @a[tag=mg.flw] ~ ~ ~ 1 2

tag @e[tag=st_guardian,distance=0..] remove move_clear_block
tag @e[tag=st_guardian,distance=0..] remove move_clear_statue
