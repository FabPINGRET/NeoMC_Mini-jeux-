execute at @s if entity @s[y=47,dy=6] if block ~ 47 ~ lime_wool run tag @a[distance=..5,tag=mg.flw] add caught
execute at @s if entity @s[y=47,dy=6] if block ~ 47 ~ blue_wool if score stealth_cycle bool matches 0 run tag @a[distance=..5,tag=mg.flw] add caught
execute at @s if entity @s[y=47,dy=6] if block ~ 47 ~ red_wool if score stealth_cycle bool matches 1 run tag @a[distance=..5,tag=mg.flw] add caught
execute at @s if entity @s[y=47,dy=6] if block ~ 47 ~ white_wool if score @n[tag=stealth_guard,tag=target,distance=0..] bool matches 0 run tag @a[distance=..5,tag=mg.flw] add caught
execute at @s if entity @s[y=47,dy=6] if block ~ 47 ~ black_wool if score @n[tag=stealth_guard,tag=target,distance=0..] bool matches 1 run tag @a[distance=..5,tag=mg.flw] add caught
execute at @s if entity @s[y=47,dy=6] if block ~ 47 ~ purple_wool if score @n[tag=stealth_guard,tag=water,distance=0..] bool matches 0 run tag @a[distance=..5,tag=mg.flw] add caught
execute at @s if entity @s[y=47,dy=6] if entity @n[tag=stealth_guard,tag=water,distance=..0.5] run tag @a[distance=..5,tag=mg.flw] add caught

execute at @s if entity @s[tag=caught] run tellraw @a[tag=caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> HEY, WHERE DO YOU THINK YOU'RE GOING??","color":"white"}]
execute at @s if entity @s[tag=caught] run effect give @a[tag=caught,tag=mg.flw] slowness 2 50 true
execute at @s if entity @s[tag=caught] as @a[tag=caught,tag=mg.flw] at @s facing entity @n[tag=stealth_guard,distance=0..] eyes run tp @s ~ ~ ~ ~ 0
execute at @s if entity @s[tag=caught] as @a[tag=caught,tag=mg.flw] at @s run playsound minecraft:entity.squid.death neutral @s ~ ~ ~ 1 2
execute at @s if entity @s[tag=caught] as @a[tag=caught,tag=mg.flw] run scoreboard players set @s stealth_caught_timer 40
