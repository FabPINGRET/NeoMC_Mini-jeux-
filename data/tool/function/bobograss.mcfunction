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

spreadplayers ~ ~ 2 10 false @e[tag=bobo_place,distance=0..]

execute as @e[tag=bobo_place,distance=0..] at @s positioned ~1 ~ ~ if entity @e[tag=bobo_place,distance=..0.5] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s positioned ~ ~ ~1 if entity @e[tag=bobo_place,distance=..0.5] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s positioned ~-1 ~ ~ if entity @e[tag=bobo_place,distance=..0.5] run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s positioned ~ ~ ~-1 if entity @e[tag=bobo_place,distance=..0.5] run kill @s

execute as @e[tag=bobo_place,distance=0..] at @s if block ~1 ~ ~ warped_roots run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s if block ~ ~ ~1 warped_roots run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s if block ~-1 ~ ~ warped_roots run kill @s
execute as @e[tag=bobo_place,distance=0..] at @s if block ~ ~ ~-1 warped_roots run kill @s


execute as @e[tag=bobo_place,distance=0..] at @s if block ~ ~-1 ~ netherrack run fill ~ ~ ~ ~ ~ ~ warped_roots replace air

kill @e[tag=bobo_place,distance=0..]

#schedule function tool:bobograss_finish 5t replace
