execute if block ~ ~ ~ chiseled_tuff_bricks run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:chiseled_tuff_bricks"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ chiseled_tuff run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:chiseled_tuff"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ polished_tuff run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:polished_tuff"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~ ~ air run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:barrier"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ structure_void run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:structure_void"},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~ ~ iron_chain[axis=y] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:iron_chain",Properties:{axis:"y"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~ ~ tuff_brick_wall[east=none,north=none,south=none,west=none,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"none",north:"none",south:"none",west:"none",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~ ~ tuff_brick_wall[east=low,north=none,south=none,west=none,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"low",north:"none",south:"none",west:"none",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=none,north=low,south=none,west=none,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"none",north:"low",south:"none",west:"none",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=none,north=none,south=low,west=none,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"none",north:"none",south:"low",west:"none",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=none,north=none,south=none,west=low,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"none",north:"none",south:"none",west:"low",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~ ~ tuff_brick_wall[east=none,north=none,south=low,west=low,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"none",north:"none",south:"low",west:"low",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=none,north=low,south=none,west=low,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"none",north:"low",south:"none",west:"low",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=low,north=none,south=low,west=none,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"low",north:"none",south:"low",west:"none",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=low,north=low,south=none,west=none,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"low",north:"low",south:"none",west:"none",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

execute if block ~ ~ ~ tuff_brick_wall[east=none,north=low,south=low,west=low,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"none",north:"low",south:"low",west:"low",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=low,north=none,south=low,west=low,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"low",north:"none",south:"low",west:"low",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=low,north=low,south=none,west=low,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"low",north:"low",south:"none",west:"low",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}
execute if block ~ ~ ~ tuff_brick_wall[east=low,north=low,south=low,west=none,up=true] run summon falling_block ~ ~-0.5 ~ {BlockState:{Name:"minecraft:tuff_brick_wall",Properties:{east:"low",north:"low",south:"low",west:"none",up:"true"}},Time:1,DropItem:0b,CancelDrop:0b,HurtEntities:0b}

setblock ~ ~ ~ air
