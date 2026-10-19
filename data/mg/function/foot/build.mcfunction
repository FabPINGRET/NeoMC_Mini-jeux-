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
fill -19 63 -19 -17 63 -17 minecraft:green_glazed_terracotta
setblock -18 63 -18 minecraft:gold_block
fill -19 64 -19 -17 66 -17 minecraft:air
setblock 2 46 -30 minecraft:lodestone
function mg:foot/labels
execute if score $ftoff mg.st matches 1 run function mg:foot/entry_close
data modify storage mg:lobby foot1 set value 1b
