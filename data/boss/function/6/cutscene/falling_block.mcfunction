execute if block ~ ~-30 ~ mud_bricks run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_bricks"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ air run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:barrier"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ ochre_froglight[axis=y] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:ochre_froglight",Properties:{axis:"y"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~-30 ~ mud_brick_stairs[facing=east,half=bottom] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"east",half:"bottom"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ mud_brick_stairs[facing=west,half=bottom] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"west",half:"bottom"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ mud_brick_stairs[facing=north,half=bottom] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"north",half:"bottom"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ mud_brick_stairs[facing=south,half=bottom] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"south",half:"bottom"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~-30 ~ mud_brick_stairs[facing=east,half=top] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"east",half:"top"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ mud_brick_stairs[facing=west,half=top] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"west",half:"top"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ mud_brick_stairs[facing=north,half=top] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"north",half:"top"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~-30 ~ mud_brick_stairs[facing=south,half=top] run summon falling_block ~ ~-30.5 ~ {BlockState:{Name:"minecraft:mud_brick_stairs",Properties:{facing:"south",half:"top"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}


setblock ~ ~-30 ~ air
