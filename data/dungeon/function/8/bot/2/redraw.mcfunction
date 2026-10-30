fill -10780 50 410 -10769 48 399 air

execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ~ ~1 ~ minecraft:sea_lantern
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ~ ~2 ~ minecraft:iron_bars
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ^1 ^0.5 ^ minecraft:diorite_wall
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ^-1 ^0.5 ^ minecraft:diorite_wall
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ^1 ^0.5 ^-1 minecraft:diorite_wall
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ^-1 ^0.5 ^-1 minecraft:diorite_wall
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ^1 ^1 ^-1 minecraft:diorite_wall
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ^-1 ^1 ^-1 minecraft:diorite_wall
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run setblock ^ ^1 ^-1 minecraft:diorite_wall

execute as @n[tag=fs_bot,tag=2,distance=0..] at @s if entity @s[y_rotation=90] run setblock ^ ^1 ^1 minecraft:player_wall_head[facing=west,powered=false]{components:{"minecraft:lore":['{"color":"gray","italic":false,"text":"Custom Head ID: 112395"}','{"color":"blue","italic":false,"text":"www.minecraft-heads.com"}']},custom_name:'{"text":"Diamond Gem","bold":true,"italic":false,"underlined":true,"color":"gold"}',profile:{id:[I;-1581063518,-468492328,-1598945027,1244511198],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTBhMTA2ZmU5MDQxYTg1OGNjZjQxNDBiYmI5ZGI2YzJhZjNiNTI1OTI2MTNhNzRkMDhhZmM2ZWQ2YmFhNDExYSJ9fX0="}]}}

execute as @n[tag=fs_bot,tag=2,distance=0..] at @s if entity @s[y_rotation=-180] run setblock ^ ^1 ^1 minecraft:player_wall_head[facing=north,powered=false]{components:{"minecraft:lore":['{"color":"gray","italic":false,"text":"Custom Head ID: 112395"}','{"color":"blue","italic":false,"text":"www.minecraft-heads.com"}']},custom_name:'{"text":"Diamond Gem","bold":true,"italic":false,"underlined":true,"color":"gold"}',profile:{id:[I;-1581063518,-468492328,-1598945027,1244511198],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTBhMTA2ZmU5MDQxYTg1OGNjZjQxNDBiYmI5ZGI2YzJhZjNiNTI1OTI2MTNhNzRkMDhhZmM2ZWQ2YmFhNDExYSJ9fX0="}]}}

execute as @n[tag=fs_bot,tag=2,distance=0..] at @s if entity @s[y_rotation=-90] run setblock ^ ^1 ^1 minecraft:player_wall_head[facing=east,powered=false]{components:{"minecraft:lore":['{"color":"gray","italic":false,"text":"Custom Head ID: 112395"}','{"color":"blue","italic":false,"text":"www.minecraft-heads.com"}']},custom_name:'{"text":"Diamond Gem","bold":true,"italic":false,"underlined":true,"color":"gold"}',profile:{id:[I;-1581063518,-468492328,-1598945027,1244511198],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTBhMTA2ZmU5MDQxYTg1OGNjZjQxNDBiYmI5ZGI2YzJhZjNiNTI1OTI2MTNhNzRkMDhhZmM2ZWQ2YmFhNDExYSJ9fX0="}]}}

execute as @n[tag=fs_bot,tag=2,distance=0..] at @s if entity @s[y_rotation=0] run setblock ^ ^1 ^1 minecraft:player_wall_head[facing=south,powered=false]{components:{"minecraft:lore":['{"color":"gray","italic":false,"text":"Custom Head ID: 112395"}','{"color":"blue","italic":false,"text":"www.minecraft-heads.com"}']},custom_name:'{"text":"Diamond Gem","bold":true,"italic":false,"underlined":true,"color":"gold"}',profile:{id:[I;-1581063518,-468492328,-1598945027,1244511198],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTBhMTA2ZmU5MDQxYTg1OGNjZjQxNDBiYmI5ZGI2YzJhZjNiNTI1OTI2MTNhNzRkMDhhZmM2ZWQ2YmFhNDExYSJ9fX0="}]}}
