# ⚽ Terrain de foot souterrain : terrain, buts, vestiaire, tapis d'entrée (généré par tools/lobby/gen_foot.py)
fill -14 46 -41 18 54 -21 minecraft:deepslate_bricks
fill -17 46 -34 -14 51 -28 minecraft:deepslate_bricks
fill 18 46 -34 21 51 -28 minecraft:deepslate_bricks
fill -4 46 -20 4 52 -14 minecraft:deepslate_bricks
fill -13 48 -40 17 53 -22 minecraft:air
fill -16 48 -33 -14 50 -29 minecraft:air
fill 18 48 -33 20 50 -29 minecraft:air
fill -3 48 -19 3 51 -15 minecraft:air
fill -1 48 -21 1 50 -20 minecraft:air
fill -13 47 -40 17 47 -22 minecraft:green_concrete
fill 2 47 -40 2 47 -22 minecraft:white_concrete
fill 0 47 -33 4 47 -33 minecraft:white_concrete
fill 0 47 -29 4 47 -29 minecraft:white_concrete
fill 0 47 -33 0 47 -29 minecraft:white_concrete
fill 4 47 -33 4 47 -29 minecraft:white_concrete
fill -17 48 -33 -17 50 -29 minecraft:red_concrete
fill 21 48 -33 21 50 -29 minecraft:blue_concrete
fill -14 48 -34 -14 50 -34 minecraft:white_concrete
fill -14 48 -28 -14 50 -28 minecraft:white_concrete
fill -14 51 -34 -14 51 -28 minecraft:white_concrete
fill 18 48 -34 18 50 -34 minecraft:white_concrete
fill 18 48 -28 18 50 -28 minecraft:white_concrete
fill 18 51 -34 18 51 -28 minecraft:white_concrete
setblock -11 54 -38 minecraft:sea_lantern
setblock -11 54 -33 minecraft:sea_lantern
setblock -11 54 -28 minecraft:sea_lantern
setblock -11 54 -23 minecraft:sea_lantern
setblock -6 54 -38 minecraft:sea_lantern
setblock -6 54 -33 minecraft:sea_lantern
setblock -6 54 -28 minecraft:sea_lantern
setblock -6 54 -23 minecraft:sea_lantern
setblock -1 54 -38 minecraft:sea_lantern
setblock -1 54 -33 minecraft:sea_lantern
setblock -1 54 -28 minecraft:sea_lantern
setblock -1 54 -23 minecraft:sea_lantern
setblock 4 54 -38 minecraft:sea_lantern
setblock 4 54 -33 minecraft:sea_lantern
setblock 4 54 -28 minecraft:sea_lantern
setblock 4 54 -23 minecraft:sea_lantern
setblock 9 54 -38 minecraft:sea_lantern
setblock 9 54 -33 minecraft:sea_lantern
setblock 9 54 -28 minecraft:sea_lantern
setblock 9 54 -23 minecraft:sea_lantern
setblock 14 54 -38 minecraft:sea_lantern
setblock 14 54 -33 minecraft:sea_lantern
setblock 14 54 -28 minecraft:sea_lantern
setblock 14 54 -23 minecraft:sea_lantern
setblock -16 51 -31 minecraft:sea_lantern
setblock 20 51 -31 minecraft:sea_lantern
fill -3 47 -19 3 47 -15 minecraft:deepslate_tiles
setblock -3 52 -19 minecraft:sea_lantern
setblock 3 52 -19 minecraft:sea_lantern
setblock -3 52 -15 minecraft:sea_lantern
setblock 3 52 -15 minecraft:sea_lantern
fill -3 47 -19 -2 47 -18 minecraft:red_concrete
fill 2 47 -19 3 47 -18 minecraft:blue_concrete
fill -3 47 -16 -2 47 -15 minecraft:white_concrete
fill 2 47 -16 3 47 -15 minecraft:gold_block
# ancien puits : rebouché avec les blocs du spawn (roche, terre, avenue)
fill -2 53 -18 1 53 -15 minecraft:stone
fill -2 54 -18 1 54 -15 minecraft:stone
fill -2 55 -18 1 55 -15 minecraft:stone
fill -2 56 -18 1 56 -15 minecraft:stone
fill -2 57 -18 1 57 -15 minecraft:stone
fill -2 58 -18 1 58 -15 minecraft:stone
fill -2 59 -18 1 59 -15 minecraft:dirt
fill -2 60 -18 1 60 -15 minecraft:dirt
fill -2 61 -18 1 61 -15 minecraft:dirt
fill -2 62 -18 1 62 -15 minecraft:dirt
setblock -2 63 -18 minecraft:stone_bricks
setblock -2 63 -17 minecraft:stone_bricks
setblock -2 63 -16 minecraft:stone_bricks
setblock -2 63 -15 minecraft:stone_bricks
setblock -1 63 -18 minecraft:stone_bricks
setblock -1 63 -17 minecraft:mossy_stone_bricks
setblock -1 63 -16 minecraft:stone_bricks
setblock -1 63 -15 minecraft:stone_bricks
setblock 0 63 -18 minecraft:stone_bricks
setblock 0 63 -17 minecraft:stone_bricks
setblock 0 63 -16 minecraft:stone_bricks
setblock 0 63 -15 minecraft:stone_bricks
setblock 1 63 -18 minecraft:stone_bricks
setblock 1 63 -17 minecraft:stone_bricks
setblock 1 63 -16 minecraft:mossy_stone_bricks
setblock 1 63 -15 minecraft:stone_bricks
execute if block -2 64 -18 minecraft:polished_blackstone_wall run fill -2 64 -18 -2 65 -18 minecraft:air
execute if block -2 64 -15 minecraft:polished_blackstone_wall run fill -2 64 -15 -2 65 -15 minecraft:air
execute if block 1 64 -18 minecraft:polished_blackstone_wall run fill 1 64 -18 1 65 -18 minecraft:air
execute if block 1 64 -15 minecraft:polished_blackstone_wall run fill 1 64 -15 1 65 -15 minecraft:air
# tapis d'avant : rendu à l'herbe
fill -19 63 -19 -17 63 -17 minecraft:grass_block
setblock -19 64 -19 minecraft:short_grass
setblock -19 64 -18 minecraft:air
setblock -19 64 -17 minecraft:air
setblock -18 64 -19 minecraft:dandelion
setblock -18 64 -18 minecraft:air
setblock -18 64 -17 minecraft:air
setblock -17 64 -19 minecraft:air
setblock -17 64 -18 minecraft:air
setblock -17 64 -17 minecraft:air
# ancienne entrée de l'avenue nord : décor du spawn rendu
setblock -8 63 -41 minecraft:grass_block
setblock -8 63 -40 minecraft:grass_block
setblock -8 63 -39 minecraft:grass_block
setblock -8 63 -38 minecraft:grass_block
setblock -8 63 -37 minecraft:grass_block
setblock -7 63 -41 minecraft:grass_block
setblock -7 63 -40 minecraft:grass_block
setblock -7 63 -39 minecraft:grass_block
setblock -7 63 -38 minecraft:grass_block
setblock -7 63 -37 minecraft:grass_block
setblock -6 63 -41 minecraft:grass_block
setblock -6 63 -40 minecraft:grass_block
setblock -6 63 -39 minecraft:grass_block
setblock -6 63 -38 minecraft:grass_block
setblock -6 63 -37 minecraft:grass_block
setblock -5 63 -41 minecraft:grass_block
setblock -5 63 -40 minecraft:grass_block
setblock -5 63 -39 minecraft:grass_block
setblock -5 63 -38 minecraft:grass_block
setblock -5 63 -37 minecraft:grass_block
setblock -4 63 -41 minecraft:grass_block
setblock -4 63 -40 minecraft:grass_block
setblock -4 63 -39 minecraft:grass_block
setblock -4 63 -38 minecraft:grass_block
setblock -4 63 -37 minecraft:grass_block
setblock -8 64 -41 minecraft:air
setblock -8 64 -40 minecraft:bamboo[age=0,leaves=none]
setblock -8 64 -39 minecraft:air
setblock -8 64 -38 minecraft:bamboo[age=0,leaves=none]
setblock -8 64 -37 minecraft:short_grass
setblock -7 64 -41 minecraft:air
setblock -7 64 -40 minecraft:short_grass
setblock -7 64 -39 minecraft:pink_tulip
setblock -7 64 -38 minecraft:air
setblock -7 64 -37 minecraft:air
setblock -6 64 -41 minecraft:azure_bluet
setblock -6 64 -40 minecraft:cornflower
setblock -6 64 -39 minecraft:white_tulip
setblock -6 64 -38 minecraft:orange_tulip
setblock -6 64 -37 minecraft:short_grass
setblock -5 64 -41 minecraft:air
setblock -5 64 -40 minecraft:red_tulip
setblock -5 64 -39 minecraft:allium
setblock -5 64 -38 minecraft:blue_orchid
setblock -5 64 -37 minecraft:oxeye_daisy
setblock -4 64 -41 minecraft:air
setblock -4 64 -40 minecraft:azalea_leaves[persistent=true]
setblock -4 64 -39 minecraft:azalea_leaves[persistent=true]
setblock -4 64 -38 minecraft:azalea_leaves[persistent=true]
setblock -4 64 -37 minecraft:chiseled_polished_blackstone
setblock -8 65 -41 minecraft:air
setblock -8 65 -40 minecraft:bamboo[age=0,leaves=none]
setblock -8 65 -39 minecraft:air
setblock -8 65 -38 minecraft:bamboo[age=0,leaves=none]
setblock -8 65 -37 minecraft:air
setblock -7 65 -41 minecraft:air
setblock -7 65 -40 minecraft:air
setblock -7 65 -39 minecraft:air
setblock -7 65 -38 minecraft:air
setblock -7 65 -37 minecraft:air
setblock -6 65 -41 minecraft:air
setblock -6 65 -40 minecraft:air
setblock -6 65 -39 minecraft:air
setblock -6 65 -38 minecraft:air
setblock -6 65 -37 minecraft:air
setblock -5 65 -41 minecraft:air
setblock -5 65 -40 minecraft:air
setblock -5 65 -39 minecraft:air
setblock -5 65 -38 minecraft:air
setblock -5 65 -37 minecraft:air
setblock -4 65 -41 minecraft:air
setblock -4 65 -40 minecraft:air
setblock -4 65 -39 minecraft:air
setblock -4 65 -38 minecraft:air
setblock -4 65 -37 minecraft:polished_blackstone_wall
setblock -8 66 -41 minecraft:air
setblock -8 66 -40 minecraft:bamboo[age=0,leaves=none]
setblock -8 66 -39 minecraft:air
setblock -8 66 -38 minecraft:bamboo[age=0,leaves=none]
setblock -8 66 -37 minecraft:air
setblock -7 66 -41 minecraft:air
setblock -7 66 -40 minecraft:air
setblock -7 66 -39 minecraft:air
setblock -7 66 -38 minecraft:air
setblock -7 66 -37 minecraft:air
setblock -6 66 -41 minecraft:air
setblock -6 66 -40 minecraft:air
setblock -6 66 -39 minecraft:air
setblock -6 66 -38 minecraft:air
setblock -6 66 -37 minecraft:air
setblock -5 66 -41 minecraft:air
setblock -5 66 -40 minecraft:air
setblock -5 66 -39 minecraft:air
setblock -5 66 -38 minecraft:air
setblock -5 66 -37 minecraft:air
setblock -4 66 -41 minecraft:air
setblock -4 66 -40 minecraft:air
setblock -4 66 -39 minecraft:air
setblock -4 66 -38 minecraft:air
setblock -4 66 -37 minecraft:polished_blackstone_wall
setblock -8 67 -41 minecraft:air
setblock -8 67 -40 minecraft:bamboo[age=0,leaves=none]
setblock -8 67 -39 minecraft:air
setblock -8 67 -38 minecraft:bamboo[age=0,leaves=small]
setblock -8 67 -37 minecraft:air
setblock -7 67 -41 minecraft:air
setblock -7 67 -40 minecraft:air
setblock -7 67 -39 minecraft:air
setblock -7 67 -38 minecraft:air
setblock -7 67 -37 minecraft:air
setblock -6 67 -41 minecraft:air
setblock -6 67 -40 minecraft:air
setblock -6 67 -39 minecraft:air
setblock -6 67 -38 minecraft:air
setblock -6 67 -37 minecraft:air
setblock -5 67 -41 minecraft:air
setblock -5 67 -40 minecraft:air
setblock -5 67 -39 minecraft:air
setblock -5 67 -38 minecraft:air
setblock -5 67 -37 minecraft:air
setblock -4 67 -41 minecraft:air
setblock -4 67 -40 minecraft:air
setblock -4 67 -39 minecraft:air
setblock -4 67 -38 minecraft:air
setblock -4 67 -37 minecraft:polished_blackstone_wall
setblock -8 68 -41 minecraft:air
setblock -8 68 -40 minecraft:bamboo[age=0,leaves=none]
setblock -8 68 -39 minecraft:air
setblock -8 68 -38 minecraft:bamboo[age=0,leaves=large]
setblock -8 68 -37 minecraft:air
setblock -7 68 -41 minecraft:air
setblock -7 68 -40 minecraft:air
setblock -7 68 -39 minecraft:air
setblock -7 68 -38 minecraft:air
setblock -7 68 -37 minecraft:air
setblock -6 68 -41 minecraft:air
setblock -6 68 -40 minecraft:air
setblock -6 68 -39 minecraft:air
setblock -6 68 -38 minecraft:air
setblock -6 68 -37 minecraft:air
setblock -5 68 -41 minecraft:air
setblock -5 68 -40 minecraft:air
setblock -5 68 -39 minecraft:air
setblock -5 68 -38 minecraft:air
setblock -5 68 -37 minecraft:air
setblock -4 68 -41 minecraft:air
setblock -4 68 -40 minecraft:air
setblock -4 68 -39 minecraft:air
setblock -4 68 -38 minecraft:air
setblock -4 68 -37 minecraft:lantern
setblock -8 69 -41 minecraft:air
setblock -8 69 -40 minecraft:bamboo[age=0,leaves=none]
setblock -8 69 -39 minecraft:air
setblock -8 69 -38 minecraft:bamboo[age=0,leaves=large]
setblock -8 69 -37 minecraft:air
setblock -7 69 -41 minecraft:air
setblock -7 69 -40 minecraft:air
setblock -7 69 -39 minecraft:air
setblock -7 69 -38 minecraft:air
setblock -7 69 -37 minecraft:air
setblock -6 69 -41 minecraft:air
setblock -6 69 -40 minecraft:air
setblock -6 69 -39 minecraft:air
setblock -6 69 -38 minecraft:air
setblock -6 69 -37 minecraft:air
setblock -5 69 -41 minecraft:air
setblock -5 69 -40 minecraft:air
setblock -5 69 -39 minecraft:air
setblock -5 69 -38 minecraft:air
setblock -5 69 -37 minecraft:air
setblock -4 69 -41 minecraft:air
setblock -4 69 -40 minecraft:air
setblock -4 69 -39 minecraft:air
setblock -4 69 -38 minecraft:air
setblock -4 69 -37 minecraft:air
setblock -8 70 -41 minecraft:air
setblock -8 70 -40 minecraft:bamboo[age=0,leaves=none]
setblock -8 70 -39 minecraft:air
setblock -8 70 -38 minecraft:air
setblock -8 70 -37 minecraft:air
setblock -7 70 -41 minecraft:air
setblock -7 70 -40 minecraft:air
setblock -7 70 -39 minecraft:air
setblock -7 70 -38 minecraft:air
setblock -7 70 -37 minecraft:air
setblock -6 70 -41 minecraft:air
setblock -6 70 -40 minecraft:air
setblock -6 70 -39 minecraft:air
setblock -6 70 -38 minecraft:air
setblock -6 70 -37 minecraft:air
setblock -5 70 -41 minecraft:air
setblock -5 70 -40 minecraft:air
setblock -5 70 -39 minecraft:air
setblock -5 70 -38 minecraft:air
setblock -5 70 -37 minecraft:air
setblock -4 70 -41 minecraft:air
setblock -4 70 -40 minecraft:air
setblock -4 70 -39 minecraft:air
setblock -4 70 -38 minecraft:air
setblock -4 70 -37 minecraft:air
setblock -8 71 -41 minecraft:air
setblock -8 71 -40 minecraft:bamboo[age=0,leaves=small]
setblock -8 71 -39 minecraft:air
setblock -8 71 -38 minecraft:air
setblock -8 71 -37 minecraft:air
setblock -7 71 -41 minecraft:air
setblock -7 71 -40 minecraft:air
setblock -7 71 -39 minecraft:air
setblock -7 71 -38 minecraft:air
setblock -7 71 -37 minecraft:air
setblock -6 71 -41 minecraft:air
setblock -6 71 -40 minecraft:air
setblock -6 71 -39 minecraft:air
setblock -6 71 -38 minecraft:air
setblock -6 71 -37 minecraft:air
setblock -5 71 -41 minecraft:air
setblock -5 71 -40 minecraft:air
setblock -5 71 -39 minecraft:air
setblock -5 71 -38 minecraft:air
setblock -5 71 -37 minecraft:air
setblock -4 71 -41 minecraft:air
setblock -4 71 -40 minecraft:air
setblock -4 71 -39 minecraft:air
setblock -4 71 -38 minecraft:air
setblock -4 71 -37 minecraft:air
setblock -8 72 -41 minecraft:air
setblock -8 72 -40 minecraft:bamboo[age=0,leaves=large]
setblock -8 72 -39 minecraft:air
setblock -8 72 -38 minecraft:air
setblock -8 72 -37 minecraft:air
setblock -7 72 -41 minecraft:air
setblock -7 72 -40 minecraft:air
setblock -7 72 -39 minecraft:air
setblock -7 72 -38 minecraft:air
setblock -7 72 -37 minecraft:air
setblock -6 72 -41 minecraft:air
setblock -6 72 -40 minecraft:air
setblock -6 72 -39 minecraft:air
setblock -6 72 -38 minecraft:air
setblock -6 72 -37 minecraft:air
setblock -5 72 -41 minecraft:air
setblock -5 72 -40 minecraft:air
setblock -5 72 -39 minecraft:air
setblock -5 72 -38 minecraft:air
setblock -5 72 -37 minecraft:air
setblock -4 72 -41 minecraft:air
setblock -4 72 -40 minecraft:air
setblock -4 72 -39 minecraft:air
setblock -4 72 -38 minecraft:air
setblock -4 72 -37 minecraft:air
setblock -8 73 -41 minecraft:air
setblock -8 73 -40 minecraft:bamboo[age=0,leaves=large]
setblock -8 73 -39 minecraft:air
setblock -8 73 -38 minecraft:air
setblock -8 73 -37 minecraft:air
setblock -7 73 -41 minecraft:air
setblock -7 73 -40 minecraft:air
setblock -7 73 -39 minecraft:air
setblock -7 73 -38 minecraft:air
setblock -7 73 -37 minecraft:air
setblock -6 73 -41 minecraft:air
setblock -6 73 -40 minecraft:air
setblock -6 73 -39 minecraft:air
setblock -6 73 -38 minecraft:air
setblock -6 73 -37 minecraft:air
setblock -5 73 -41 minecraft:air
setblock -5 73 -40 minecraft:air
setblock -5 73 -39 minecraft:air
setblock -5 73 -38 minecraft:air
setblock -5 73 -37 minecraft:air
setblock -4 73 -41 minecraft:air
setblock -4 73 -40 minecraft:air
setblock -4 73 -39 minecraft:air
setblock -4 73 -38 minecraft:air
setblock -4 73 -37 minecraft:air
fill -8 74 -41 -4 74 -37 minecraft:air
fill -8 75 -41 -4 75 -37 minecraft:air
fill -8 76 -41 -4 76 -37 minecraft:air
fill -8 77 -41 -4 77 -37 minecraft:air
fill -8 78 -41 -4 78 -37 minecraft:air
fill -8 79 -41 -4 79 -37 minecraft:air
fill -8 80 -41 -4 80 -37 minecraft:air
setblock 2 46 -30 minecraft:lodestone
function mg:foot/labels
execute if score $ftoff mg.st matches 1 run function mg:foot/entry_close
data modify storage mg:lobby foot2 set value 1b
