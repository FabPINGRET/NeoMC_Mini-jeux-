spreadplayers -10340 446 3 12 false @e[tag=pretzel_rand,distance=0..]
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~ ~ ~ {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~1 ~ ~ {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~-1 ~ ~ {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~1 ~ ~1 {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~-1 ~ ~1 {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~ ~ ~1 {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~ ~ ~-1 {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~-1 ~ ~-1 {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}
execute as @e[tag=pretzel_rand,distance=0..] at @s unless block ~ 87 ~ air positioned ~ 108 ~ run summon falling_block ~1 ~ ~-1 {BlockState:{Name:"minecraft:bricks"},Silent:1b,Time:1,DropItem:0b,CancelDrop:1b,HurtEntities:1b,FallHurtAmount:0.75f,Tags:["pretzel_brick"]}

playsound minecraft:block.anvil.place master @a[tag=mg.flw] -10340 89 446 2 0.1

schedule function floaty:sched/boss/mini/pretzel/schedule_attack 3s
