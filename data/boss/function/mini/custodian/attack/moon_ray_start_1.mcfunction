summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}
summon marker -10441 90.5 439 {NoGravity:1b,Silent:1b,Tags:["custodian_moon_ray_1"]}


#playsound minecraft:block.enchantment_table.use hostile @a -10441 90.5 439 3 1.6

scoreboard players set custodian_midnight_moon_angle_1 Value -8000
scoreboard players set custodian_midnight_moon_angle_2 Value -8000
scoreboard players set custodian_midnight_moon_angle_3 Value -8000

execute as @e[tag=custodian_moon_ray_1,distance=0..] store result entity @s Rotation[0] double 1 run random value -180..180
execute as @e[tag=custodian_moon_ray_1,distance=0..] store result entity @s Rotation[1] double 0.01 run scoreboard players get custodian_midnight_moon_angle_1 Value


setblock -10449 67 433 minecraft:redstone_block
setblock -10456 67 433 minecraft:redstone_block

schedule function floaty:sched/boss/mini/custodian/attack/moon_ray_start_2 30t
