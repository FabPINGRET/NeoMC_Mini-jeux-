summon block_display -10340 92 446 {NoGravity:1b,Silent:1b,Tags:["pretzel_book_shelf"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.5f,1.5f,1.5f]},block_state:{Name:"minecraft:bookshelf"}}
execute as @n[tag=pretzel_book_shelf,distance=0..] at @s run tp @s ~-0.75 ~-0.5 ~-0.75
setblock -10355 61 452 redstone_block
playsound minecraft:block.enchantment_table.use hostile @a[tag=mg.flw] -10340 89 446 2 1
