execute as @n[tag=s_t_locator,distance=0..] if entity @s[tag=1] run scoreboard players set s_t_locator_1 bool 0
execute as @n[tag=s_t_locator,distance=0..] if entity @s[tag=2] run scoreboard players set s_t_locator_2 bool 0
execute as @n[tag=s_t_locator,distance=0..] if entity @s[tag=3] run scoreboard players set s_t_locator_3 bool 0
execute as @n[tag=s_t_locator,distance=0..] if entity @s[tag=4] run scoreboard players set s_t_locator_4 bool 0
execute as @n[tag=s_t_locator,distance=0..] if entity @s[tag=5] run scoreboard players set s_t_locator_5 bool 0
execute as @n[tag=s_t_locator,distance=0..] if entity @s[tag=6] run scoreboard players set s_t_locator_6 bool 0

execute as @n[tag=s_t_locator,distance=0..] at @s run tp @s ~ ~ ~ ~45 ~
execute as @n[tag=s_t_locator,distance=0..] at @s run playsound minecraft:block.grindstone.use master @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute as @n[tag=s_t_locator,distance=0..] at @s if entity @s[tag=1] if block ^ ^ ^1 structure_void run scoreboard players set s_t_locator_1 bool 1
execute as @n[tag=s_t_locator,distance=0..] at @s if entity @s[tag=2] if block ^ ^ ^1 structure_void run scoreboard players set s_t_locator_2 bool 1
execute as @n[tag=s_t_locator,distance=0..] at @s if entity @s[tag=3] if block ^ ^ ^1 structure_void run scoreboard players set s_t_locator_3 bool 1
execute as @n[tag=s_t_locator,distance=0..] at @s if entity @s[tag=4] if block ^ ^ ^1 structure_void run scoreboard players set s_t_locator_4 bool 1
execute as @n[tag=s_t_locator,distance=0..] at @s if entity @s[tag=5] if block ^ ^ ^1 structure_void run scoreboard players set s_t_locator_5 bool 1
execute as @n[tag=s_t_locator,distance=0..] at @s if entity @s[tag=6] if block ^ ^ ^1 structure_void run scoreboard players set s_t_locator_6 bool 1

execute if score s_t_locator_1 bool matches 1 if score s_t_locator_2 bool matches 1 if score s_t_locator_3 bool matches 1 if score s_t_locator_4 bool matches 1 if score s_t_locator_5 bool matches 1 if score s_t_locator_6 bool matches 1 run setblock -9773 252 418 minecraft:redstone_block

execute if score s_t_locator_1 bool matches 1 if score s_t_locator_2 bool matches 1 if score s_t_locator_3 bool matches 1 if score s_t_locator_4 bool matches 1 if score s_t_locator_5 bool matches 1 if score s_t_locator_6 bool matches 1 as @n[tag=s_t_locator,distance=0..] at @s run playsound minecraft:entity.enderman.ambient master @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score s_t_locator_1 bool matches 1 if score s_t_locator_2 bool matches 1 if score s_t_locator_3 bool matches 1 if score s_t_locator_4 bool matches 1 if score s_t_locator_5 bool matches 1 if score s_t_locator_6 bool matches 1 as @n[tag=s_t_locator,distance=0..] at @s run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"?","color":"gray"},{"text":"> ","color":"white"},{"text":"The way... we see it.. the stolen temple's hiding place opens now under our gaze...","color":"gray","italic":true}]
