#FOR TOTAL RESET
#scoreboard players set fs_puzzle3_level Value 3

fill -10760 48 434 -10740 62 454 air replace minecraft:diamond_block
execute positioned -10750 55 444 run kill @e[tag=fs_slide_block,distance=..25,limit=3]
execute positioned -10750 55 444 run kill @e[tag=fs_block_slide_display,distance=..25,limit=3]

# REPLACE BLOCKS LEVEL 3
execute if score fs_puzzle3_level Value matches 3 run setblock -10744 62 438 minecraft:diamond_block
execute if score fs_puzzle3_level Value matches 3 run summon armor_stand -10744 62 438 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["fs_slide_block","still"]}

execute if score fs_puzzle3_level Value matches 2 run setblock -10750 55 440 minecraft:diamond_block
execute if score fs_puzzle3_level Value matches 2 run summon armor_stand -10750 55 440 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["fs_slide_block","still"]}

execute if score fs_puzzle3_level Value matches 1 run setblock -10750 48 448 minecraft:diamond_block
execute if score fs_puzzle3_level Value matches 1 run summon armor_stand -10750 48 448 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["fs_slide_block","still"]}


# REPLACE BLOCKS LEVEL 2

execute if score fs_puzzle3_level Value matches 2..3 run setblock -10744 55 438 minecraft:diamond_block
execute if score fs_puzzle3_level Value matches 2..3 run summon armor_stand -10744 55 438 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["fs_slide_block","still"]}

execute if score fs_puzzle3_level Value matches 1 run setblock -10743 48 444 minecraft:diamond_block
execute if score fs_puzzle3_level Value matches 1 run summon armor_stand -10743 48 444 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["fs_slide_block","still"]}

# REPLACE BLOCKS LEVEL 1

setblock -10744 48 438 minecraft:diamond_block
summon armor_stand -10744 48 438 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["fs_slide_block","still"]}

setblock -10762 47 442 minecraft:structure_void
setblock -10762 47 444 minecraft:structure_void
setblock -10762 47 446 minecraft:structure_void

fill -10762 25 446 -10762 25 442 air
fill -10750 25 440 -10743 25 448 air replace minecraft:redstone_block
