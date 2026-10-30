execute positioned ~ 123 ~ as @e[tag=walking_statue,distance=..3] run tp @s ~ 121 -327
execute positioned ~ 123 ~ as @a[gamemode=!spectator,distance=..3,tag=mg.flw] run tp @s ~ 121 -327

playsound minecraft:block.anvil.place master @a[tag=mg.flw] ~ ~ ~ 5 0.8
fill ~-1 ~ ~-1 ~1 ~1 ~1 air

summon falling_block ~ ~ ~ {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~1 ~ ~ {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~-1 ~ ~ {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~ ~ ~1 {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~ ~ ~-1 {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~1 ~ ~1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~1 ~ ~-1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~-1 ~ ~1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~-1 ~ ~-1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

summon falling_block ~ ~1 ~ {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~1 ~1 ~ {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~-1 ~1 ~ {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~ ~1 ~1 {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~ ~1 ~-1 {BlockState:{Name:"minecraft:chiseled_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~1 ~1 ~1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~1 ~1 ~-1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~-1 ~1 ~1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
summon falling_block ~-1 ~1 ~-1 {BlockState:{Name:"minecraft:polished_deepslate"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block -10174 124 -306 minecraft:lime_stained_glass if block -10187 124 -310 minecraft:lime_stained_glass if block -10196 124 -294 minecraft:lime_stained_glass run playsound minecraft:zelda.secret master @a[tag=mg.flw] -10184 122 -324 1 1 1
execute if block -10174 124 -306 minecraft:lime_stained_glass if block -10187 124 -310 minecraft:lime_stained_glass if block -10196 124 -294 minecraft:lime_stained_glass run setblock -10174 118 -335 minecraft:redstone_block
