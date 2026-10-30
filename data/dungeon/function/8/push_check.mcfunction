execute as @a[sort=arbitrary,scores={sneak_last=1},tag=mg.flw] at @s positioned ~ ~0.5 ~ positioned ^ ^ ^1 if entity @e[tag=fs_slide_block,tag=still,distance=..0.6] run tag @n[tag=fs_slide_block,distance=..0.6] add fs_push_check

execute as @e[tag=fs_push_check,distance=0..] at @s if block ~1 ~-1 ~ packed_ice if block ~1 ~ ~ air at @s positioned ~-1 ~ ~ if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_pushing_east
execute as @e[tag=fs_push_check,distance=0..] at @s if block ~1 ~-1 ~ packed_ice if block ~1 ~ ~ air at @s positioned ~-1 ~ ~ if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_push_success

execute as @e[tag=fs_push_check,distance=0..] at @s if block ~-1 ~-1 ~ packed_ice if block ~-1 ~ ~ air at @s positioned ~1 ~ ~ if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_pushing_west
execute as @e[tag=fs_push_check,distance=0..] at @s if block ~-1 ~-1 ~ packed_ice if block ~-1 ~ ~ air at @s positioned ~1 ~ ~ if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_push_success

execute as @e[tag=fs_push_check,distance=0..] at @s if block ~ ~-1 ~1 packed_ice if block ~ ~ ~1 air at @s positioned ~ ~ ~-1 if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_pushing_south
execute as @e[tag=fs_push_check,distance=0..] at @s if block ~ ~-1 ~1 packed_ice if block ~ ~ ~1 air at @s positioned ~ ~ ~-1 if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_push_success

execute as @e[tag=fs_push_check,distance=0..] at @s if block ~ ~-1 ~-1 packed_ice if block ~ ~ ~-1 air at @s positioned ~ ~ ~1 if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_pushing_north
execute as @e[tag=fs_push_check,distance=0..] at @s if block ~ ~-1 ~-1 packed_ice if block ~ ~ ~-1 air at @s positioned ~ ~ ~1 if entity @a[distance=..0.5,scores={sneak_last=1},tag=mg.flw] run tag @s add fs_push_success


execute as @n[tag=fs_push_check,tag=still,tag=fs_push_success,distance=0..] at @s run setblock ~ ~ ~ air
execute as @n[tag=fs_push_check,tag=still,tag=fs_push_success,distance=0..] at @s run summon block_display ~-0.5 ~ ~-0.5 {NoGravity:1b,Silent:1b,Tags:["fs_block_slide_display"],block_state:{Name:"minecraft:diamond_block"}}
execute as @n[tag=fs_push_check,tag=still,tag=fs_push_success,distance=0..] at @s run playsound minecraft:item.axe.scrape block @a[tag=mg.flw] ~ ~ ~ 1 0.7

tag @e[tag=fs_push_check,tag=fs_push_success,distance=0..] remove still

tag @e[tag=fs_pushing_east,distance=0..] remove fs_pushing_west
tag @e[tag=fs_pushing_east,distance=0..] remove fs_pushing_south
tag @e[tag=fs_pushing_east,distance=0..] remove fs_pushing_north

tag @e[tag=fs_pushing_west,distance=0..] remove fs_pushing_south
tag @e[tag=fs_pushing_west,distance=0..] remove fs_pushing_north

tag @e[tag=fs_pushing_south,distance=0..] remove fs_pushing_north

tag @e[distance=0..] remove fs_push_check
tag @e[distance=0..] remove fs_push_success
