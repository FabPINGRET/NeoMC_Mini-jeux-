execute as @e[tag=fs_slide_block,tag=fs_pushing_east,distance=0..] at @s unless block ~0.5 ~ ~ air run tag @s add become_still
execute as @e[tag=fs_slide_block,tag=fs_pushing_east,distance=0..] at @s unless block ~0.5 ~-1 ~ packed_ice unless block ~0.5 ~-1 ~ structure_void run tag @s add become_still

execute as @e[tag=fs_slide_block,tag=fs_pushing_west,distance=0..] at @s unless block ~-0.5 ~ ~ air run tag @s add become_still
execute as @e[tag=fs_slide_block,tag=fs_pushing_west,distance=0..] at @s unless block ~-0.5 ~-1 ~ packed_ice unless block ~-0.5 ~-1 ~ structure_void run tag @s add become_still

execute as @e[tag=fs_slide_block,tag=fs_pushing_south,distance=0..] at @s unless block ~ ~ ~0.5 air run tag @s add become_still
execute as @e[tag=fs_slide_block,tag=fs_pushing_south,distance=0..] at @s unless block ~ ~-1 ~0.5 packed_ice unless block ~ ~-1 ~0.5 structure_void run tag @s add become_still

execute as @e[tag=fs_slide_block,tag=fs_pushing_north,distance=0..] at @s unless block ~ ~ ~-0.5 air run tag @s add become_still
execute as @e[tag=fs_slide_block,tag=fs_pushing_north,distance=0..] at @s unless block ~ ~-1 ~-0.5 packed_ice unless block ~ ~-1 ~-0.5 structure_void run tag @s add become_still

tag @e[tag=fs_slide_block,tag=!still,tag=!fs_pushing_east,tag=!fs_pushing_west,tag=!fs_pushing_north,tag=!fs_pushing_south,distance=0..] add become_still

execute as @e[tag=fs_slide_block,tag=become_still,distance=0..] at @s run kill @e[tag=fs_block_slide_display,distance=..1]
execute as @e[tag=fs_slide_block,tag=become_still,distance=0..] at @s align xz run tp @s ~0.5 ~ ~0.5
execute as @e[tag=fs_slide_block,tag=become_still,distance=0..] at @s run setblock ~ ~ ~ diamond_block
tag @e[tag=fs_slide_block,tag=become_still,distance=0..] remove fs_pushing_east
tag @e[tag=fs_slide_block,tag=become_still,distance=0..] remove fs_pushing_west
tag @e[tag=fs_slide_block,tag=become_still,distance=0..] remove fs_pushing_north
tag @e[tag=fs_slide_block,tag=become_still,distance=0..] remove fs_pushing_south
tag @e[tag=fs_slide_block,tag=become_still,distance=0..] add still
tag @e[tag=fs_slide_block,tag=become_still,distance=0..] remove become_still


execute as @e[tag=fs_slide_block,tag=fs_pushing_east,distance=0..] at @s run tp @s ~0.25 ~ ~
execute as @e[tag=fs_slide_block,tag=fs_pushing_west,distance=0..] at @s run tp @s ~-0.25 ~ ~
execute as @e[tag=fs_slide_block,tag=fs_pushing_south,distance=0..] at @s run tp @s ~ ~ ~0.25
execute as @e[tag=fs_slide_block,tag=fs_pushing_north,distance=0..] at @s run tp @s ~ ~ ~-0.25

execute as @e[tag=fs_block_slide_display,distance=0..] at @s positioned ~-0.5 ~ ~-0.5 at @n[tag=fs_slide_block,tag=!still,distance=0..] run tp @s ~-0.5 ~ ~-0.5

function dungeon:8/push_check

execute as @e[tag=fs_slide_block,tag=still,distance=0..] at @s if block ~ ~-1 ~ structure_void run tag @s add fs_block_over_hole
execute as @e[tag=fs_block_over_hole,distance=0..] at @s run setblock ~ ~ ~ air
execute as @e[tag=fs_block_over_hole,distance=0..] at @s run setblock ~ 25 ~ redstone_block
execute as @e[tag=fs_block_over_hole,distance=0..] at @s run summon falling_block ~ ~ ~ {BlockState:{Name:"minecraft:diamond_block"},Time:1,DropItem:0b}
execute as @e[tag=fs_block_over_hole,distance=0..] at @s run playsound minecraft:item.bottle.fill_dragonbreath block @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute as @e[tag=fs_block_over_hole,distance=0..] at @s if block ~ ~-8 ~ packed_ice run summon armor_stand ~ ~-7 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["fs_slide_block","still"]}
kill @n[tag=fs_block_over_hole,distance=0..]
