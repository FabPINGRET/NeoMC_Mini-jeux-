summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["fern_place"]}

spreadplayers ~ ~ 3 10 false @e[tag=fern_place,distance=0..]

execute as @e[tag=fern_place,distance=0..] at @s positioned ~1 ~ ~ if entity @e[tag=fern_place,distance=..0.5] run kill @s
execute as @e[tag=fern_place,distance=0..] at @s positioned ~ ~ ~1 if entity @e[tag=fern_place,distance=..0.5] run kill @s
execute as @e[tag=fern_place,distance=0..] at @s positioned ~-1 ~ ~ if entity @e[tag=fern_place,distance=..0.5] run kill @s
execute as @e[tag=fern_place,distance=0..] at @s positioned ~ ~ ~-1 if entity @e[tag=fern_place,distance=..0.5] run kill @s

execute as @e[tag=fern_place,distance=0..] at @s if block ~1 ~ ~ fern run kill @s
execute as @e[tag=fern_place,distance=0..] at @s if block ~ ~ ~1 fern run kill @s
execute as @e[tag=fern_place,distance=0..] at @s if block ~-1 ~ ~ fern run kill @s
execute as @e[tag=fern_place,distance=0..] at @s if block ~ ~ ~-1 fern run kill @s


execute as @e[tag=fern_place,distance=0..] at @s if block ~ ~-1 ~ grass_block run fill ~ ~ ~ ~ ~ ~ fern replace air

kill @e[tag=fern_place,distance=0..]

#schedule function tool:bobograss_finish 5t replace
