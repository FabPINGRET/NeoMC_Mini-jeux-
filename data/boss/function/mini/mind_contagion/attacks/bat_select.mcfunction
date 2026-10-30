execute as @e[tag=mind_boss_bat,distance=0..] at @s unless block ~ 173 ~ sculk_sensor run tag @s add viable

execute as @e[tag=mind_boss_bat,tag=viable,limit=1,sort=random,distance=0..] at @s run summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["mind_boss_monster_loc"]}

execute as @e[tag=mind_boss_monster_loc,distance=0..] at @s run fill ~ 173 ~ ~ 173 ~ minecraft:sculk_sensor[sculk_sensor_phase=active] replace air
execute as @e[tag=mind_boss_monster_loc,distance=0..] at @s run fill ~ 173 ~ ~ 173 ~ minecraft:sculk_sensor[sculk_sensor_phase=active] replace sculk_vein

tag @e[tag=mind_boss_bat,distance=0..] remove viable
