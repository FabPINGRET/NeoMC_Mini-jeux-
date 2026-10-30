fill 9900 59 -137 9898 64 -126 air
fill 9898 65 -136 9900 65 -127 air
fill 9900 66 -135 9898 66 -128 air

#EMPTY
execute if score firelight_set Value matches 0 run fill 9899 63 -136 9899 65 -136 minecraft:spruce_fence strict
execute if score firelight_set Value matches 0 run fill 9900 62 -127 9900 65 -127 minecraft:spruce_fence strict

#THRONE ROOM
execute if score firelight_set Value matches 1 run fill 9900 59 -135 9900 63 -129 stone_bricks
execute if score firelight_set Value matches 1 run setblock 9900 64 -135 minecraft:stone_bricks
execute if score firelight_set Value matches 1 run setblock 9900 64 -133 minecraft:stone_bricks
execute if score firelight_set Value matches 1 run setblock 9900 64 -131 minecraft:stone_bricks
execute if score firelight_set Value matches 1 run setblock 9900 64 -129 minecraft:stone_bricks
execute if score firelight_set Value matches 1 run fill 9899 59 -133 9899 59 -131 minecraft:polished_andesite
execute if score firelight_set Value matches 1 run fill 9900 59 -131 9900 62 -133 minecraft:polished_andesite
execute if score firelight_set Value matches 1 run fill 9900 61 -132 9899 59 -132 minecraft:purple_wool replace minecraft:polished_andesite
execute if score firelight_set Value matches 1 run setblock 9899 60 -133 minecraft:polished_andesite_stairs[facing=north,half=bottom,shape=straight,waterlogged=false]
execute if score firelight_set Value matches 1 run setblock 9899 60 -131 minecraft:polished_andesite_stairs[facing=south,half=bottom,shape=straight,waterlogged=false]

#ROAD
execute if score firelight_set Value matches 2 run fill 9900 59 -136 9900 64 -127 minecraft:light_blue_wool
execute if score firelight_set Value matches 2 run fill 9898 59 -136 9899 59 -127 minecraft:moss_carpet
execute if score firelight_set Value matches 2 run fill 9900 60 -136 9900 59 -135 minecraft:moss_block
execute if score firelight_set Value matches 2 run fill 9900 59 -134 9900 59 -130 minecraft:moss_block
execute if score firelight_set Value matches 2 run fill 9900 60 -131 9900 60 -130 minecraft:moss_block
execute if score firelight_set Value matches 2 run setblock 9900 61 -130 minecraft:moss_block
execute if score firelight_set Value matches 2 run fill 9900 62 -129 9900 62 -127 minecraft:moss_block
execute if score firelight_set Value matches 2 run fill 9900 61 -129 9900 59 -127 minecraft:dripstone_block
execute if score firelight_set Value matches 2 run fill 9900 59 -128 9900 60 -128 air
execute if score firelight_set Value matches 2 run setblock 9900 62 -136 minecraft:white_wool
execute if score firelight_set Value matches 2 run fill 9900 64 -135 9900 64 -134 minecraft:white_wool
execute if score firelight_set Value matches 2 run fill 9900 63 -134 9900 63 -133 minecraft:white_wool
execute if score firelight_set Value matches 2 run fill 9900 64 -130 9900 64 -128 minecraft:white_wool
execute if score firelight_set Value matches 2 run setblock 9900 63 -129 minecraft:white_wool
execute if score firelight_set Value matches 2 run setblock 9899 59 -129 minecraft:pointed_dripstone[thickness=tip,vertical_direction=up,waterlogged=false]
execute if score firelight_set Value matches 2 run setblock 9899 59 -127 minecraft:pointed_dripstone[thickness=tip,vertical_direction=up,waterlogged=false]

#TUNNEL
execute if score firelight_set Value matches 3 run fill 9900 64 -127 9900 59 -136 stone
execute if score firelight_set Value matches 3 run fill 9898 59 -136 9899 59 -127 stone
execute if score firelight_set Value matches 3 run fill 9898 64 -136 9899 64 -127 stone
execute if score firelight_set Value matches 3 run fill 9899 60 -136 9898 60 -132 stone
execute if score firelight_set Value matches 3 run fill 9898 63 -127 9899 63 -131 stone
execute if score firelight_set Value matches 3 run setblock 9898 60 -132 air
execute if score firelight_set Value matches 3 run setblock 9898 63 -131 air
execute if score firelight_set Value matches 3 run setblock 9899 60 -131 minecraft:stone
execute if score firelight_set Value matches 3 run setblock 9899 63 -136 minecraft:pointed_dripstone[thickness=tip,vertical_direction=down,waterlogged=false]
execute if score firelight_set Value matches 3 run setblock 9898 61 -135 minecraft:pointed_dripstone[thickness=tip,vertical_direction=up,waterlogged=false]
execute if score firelight_set Value matches 3 run setblock 9898 63 -133 minecraft:pointed_dripstone[thickness=tip,vertical_direction=down,waterlogged=false]
execute if score firelight_set Value matches 3 run setblock 9898 60 -131 minecraft:pointed_dripstone[thickness=tip,vertical_direction=up,waterlogged=false]
execute if score firelight_set Value matches 3 run setblock 9898 62 -130 minecraft:pointed_dripstone[thickness=tip,vertical_direction=down,waterlogged=false]
execute if score firelight_set Value matches 3 run setblock 9899 62 -128 minecraft:pointed_dripstone[thickness=tip,vertical_direction=down,waterlogged=false]
execute if score firelight_set Value matches 3 run fill 9898 63 -136 9898 61 -136 minecraft:andesite_wall
execute if score firelight_set Value matches 3 run fill 9898 60 -132 9898 63 -132 andesite_wall
execute if score firelight_set Value matches 3 run fill 9898 60 -129 9898 62 -129 minecraft:andesite_wall
execute if score firelight_set Value matches 3 run setblock 9899 61 -128 minecraft:soul_wall_torch[facing=west]

#BAZAAR
execute if score firelight_set Value matches 4 run fill 9900 59 -136 9900 64 -127 minecraft:deepslate
execute if score firelight_set Value matches 4 run fill 9900 59 -127 9900 61 -131 blue_wool
execute if score firelight_set Value matches 4 run fill 9898 59 -130 9898 59 -128 minecraft:pale_oak_planks
execute if score firelight_set Value matches 4 run setblock 9898 59 -129 minecraft:pale_oak_slab[type=top,waterlogged=false]
execute if score firelight_set Value matches 4 run fill 9899 59 -131 9899 60 -131 minecraft:pale_oak_fence
execute if score firelight_set Value matches 4 run fill 9899 59 -127 9899 60 -127 minecraft:pale_oak_fence
execute if score firelight_set Value matches 4 run fill 9899 62 -130 9899 62 -128 minecraft:blue_wool
execute if score firelight_set Value matches 4 run setblock 9899 61 -131 minecraft:blue_wool
execute if score firelight_set Value matches 4 run setblock 9899 61 -127 minecraft:blue_wool
execute if score firelight_set Value matches 4 run setblock 9900 59 -132 minecraft:deepslate_diamond_ore
execute if score firelight_set Value matches 4 run setblock 9900 60 -136 minecraft:deepslate_diamond_ore
execute if score firelight_set Value matches 4 run setblock 9900 61 -135 minecraft:deepslate_diamond_ore
execute if score firelight_set Value matches 4 run setblock 9900 62 -132 minecraft:deepslate_diamond_ore
execute if score firelight_set Value matches 4 run setblock 9900 64 -133 minecraft:deepslate_diamond_ore
execute if score firelight_set Value matches 4 run setblock 9900 63 -129 minecraft:deepslate_diamond_ore
execute if score firelight_set Value matches 4 run setblock 9899 61 -130 minecraft:player_wall_head[facing=west,powered=false]{components:{"minecraft:lore":[{color:"gray",italic:0b,text:"Custom Head ID: 39534"},{color:"blue",italic:0b,text:"www.minecraft-heads.com"}]},custom_name:{bold:1b,color:"gold",italic:0b,text:"Comedy Mask",underlined:1b},profile:{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTljOTEwYTFlMmRhMmI3MzdkNGMwYmUwZWY5OTRlMTAzZTFlZGU0YjA1OTkyODA3NjNiMjg1N2E3OTM5NmNhZiJ9fX0="}]}}
execute if score firelight_set Value matches 4 run setblock 9899 61 -129 minecraft:player_wall_head[facing=west,powered=false]{components:{"minecraft:lore":[{color:"gray",italic:0b,text:"Custom Head ID: 39535"},{color:"blue",italic:0b,text:"www.minecraft-heads.com"}]},custom_name:{bold:1b,color:"gold",italic:0b,text:"Horror Mask",underlined:1b},profile:{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmY4ZWFlYTc1MDYzM2E0MjY5MjU1MzM1NTgzMWJkNzM3ODUxOTMyYTNmNzgxN2I4MDdkNmM3NDRhODUyOWVmYSJ9fX0="}]}}
execute if score firelight_set Value matches 4 run setblock 9899 61 -128 minecraft:player_wall_head[facing=west,powered=false]{components:{"minecraft:lore":[{color:"gray",italic:0b,text:"Custom Head ID: 39532"},{color:"blue",italic:0b,text:"www.minecraft-heads.com"}]},custom_name:{bold:1b,color:"gold",italic:0b,text:"Tragedy Mask",underlined:1b},profile:{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzRjZTNkMTAwZGQ5NTNiODk2ZTFjOTQ0MGExMjI5N2YzMDExMGEzODg5YzQ5Y2UxOWNmOGI4YzA2MDRmY2M5ZSJ9fX0="}]}}
