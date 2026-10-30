summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["bobo_place"]}

spreadplayers ~ ~ 2 30 false @e[tag=bobo_place,distance=0..]

execute as @e[tag=bobo_place,distance=0..] at @s positioned ~1 ~ ~ if entity @e[tag=bobo_place,distance=..0.5] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s positioned ~ ~ ~1 if entity @e[tag=bobo_place,distance=..0.5] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s positioned ~-1 ~ ~ if entity @e[tag=bobo_place,distance=..0.5] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s positioned ~ ~ ~-1 if entity @e[tag=bobo_place,distance=..0.5] run kill @s

execute as @e[tag=bobo_place,distance=0..] at @s if block ~1 ~ ~ minecraft:dead_tube_coral[waterlogged=false] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s if block ~ ~ ~1 minecraft:dead_tube_coral[waterlogged=false] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s if block ~-1 ~ ~ minecraft:dead_tube_coral[waterlogged=false] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s if block ~ ~ ~-1 minecraft:dead_tube_coral[waterlogged=false] run kill @s


execute as @e[tag=bobo_place,distance=0..] at @s if block ~ ~-1 ~ cobblestone run fill ~ ~ ~ ~ ~ ~ minecraft:dead_tube_coral[waterlogged=false] replace air

kill @e[tag=bobo_place,distance=0..]

#schedule function tool:bobograss_finish 5t replace
