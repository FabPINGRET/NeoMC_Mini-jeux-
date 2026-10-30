clone -10448 -10 -337 -10440 -4 -329 -10477 -21 -382
execute if score boss:st_glass bool matches 0 run fill -10477 -21 -382 -10469 -15 -374 light[level=0] replace minecraft:lime_stained_glass
execute as @n[tag=st_boss_statue,distance=0..] at @s run tp @s ~ ~ ~ 202.5 0

tag @e[tag=st_boss_face_ref,distance=0..] remove adj
tag @n[tag=st_boss_face_ref,tag=12,distance=0..] add adj
tag @n[tag=st_boss_face_ref,tag=14,distance=0..] add adj
scoreboard players set boss:st_facing_dir Value 13
