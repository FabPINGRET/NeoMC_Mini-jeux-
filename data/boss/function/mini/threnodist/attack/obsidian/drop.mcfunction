spreadplayers -11144 430 7 18 false @e[tag=thren_rand,distance=0..]
execute as @e[tag=thren_rand,distance=0..] at @s if block ~ 124 ~ glass run tag @s add viable

tag @e[tag=thren_rand,sort=random,limit=3,tag=viable,distance=0..] add big
tag @e[tag=thren_rand,sort=random,limit=3,tag=viable,tag=!big,distance=0..] add medium
tag @e[tag=thren_rand,tag=viable,tag=!big,tag=!medium,distance=0..] add small

execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~ ~ ~ {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~1 ~ ~ {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~-1 ~ ~ {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~ ~ ~1 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~ ~ ~-1 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~1 ~ ~1 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~1 ~ ~-1 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~-1 ~ ~1 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=big,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~-1 ~ ~-1 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}

execute as @e[tag=thren_rand,tag=medium,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~-0.5 ~ ~-0.5 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=medium,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~0.5 ~ ~0.5 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=medium,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~-0.5 ~ ~0.5 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}
execute as @e[tag=thren_rand,tag=medium,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~0.5 ~ ~-0.5 {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}

execute as @e[tag=thren_rand,tag=small,distance=0..] at @s positioned ~ 85 ~ run summon falling_block ~ ~ ~ {BlockState:{Name:"minecraft:crying_obsidian"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["thren_drop_block"]}

tag @e[tag=thren_rand,distance=0..] remove viable
tag @e[tag=thren_rand,distance=0..] remove big
tag @e[tag=thren_rand,distance=0..] remove medium
tag @e[tag=thren_rand,distance=0..] remove small

