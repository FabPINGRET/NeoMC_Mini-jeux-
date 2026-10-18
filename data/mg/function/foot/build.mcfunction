# ⚽ Terrain de foot souterrain : terrain, buts, vestiaire, puits (généré par tools/lobby/gen_foot.py)
fill -14 46 -41 18 54 -21 minecraft:deepslate_bricks
fill -17 46 -34 -14 51 -28 minecraft:deepslate_bricks
fill 18 46 -34 21 51 -28 minecraft:deepslate_bricks
fill -4 46 -20 4 52 -14 minecraft:deepslate_bricks
fill -2 52 -18 1 62 -15 minecraft:deepslate_bricks
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
setblock -2 57 -17 minecraft:sea_lantern
setblock 1 57 -16 minecraft:sea_lantern
setblock -2 61 -16 minecraft:sea_lantern
setblock 1 61 -17 minecraft:sea_lantern
fill -3 47 -19 -2 47 -18 minecraft:red_concrete
fill 2 47 -19 3 47 -18 minecraft:blue_concrete
fill -3 47 -16 -2 47 -15 minecraft:white_concrete
fill 2 47 -16 3 47 -15 minecraft:gold_block
fill -1 47 -17 0 47 -16 minecraft:hay_block
fill -2 63 -18 1 63 -15 minecraft:polished_blackstone_bricks
fill -1 52 -17 0 63 -16 minecraft:air
fill -1 64 -17 0 66 -16 minecraft:air
setblock -2 64 -18 minecraft:polished_blackstone_wall
setblock -2 65 -18 minecraft:lantern
setblock 1 64 -18 minecraft:polished_blackstone_wall
setblock 1 65 -18 minecraft:lantern
setblock -2 64 -15 minecraft:polished_blackstone_wall
setblock -2 65 -15 minecraft:lantern
setblock 1 64 -15 minecraft:polished_blackstone_wall
setblock 1 65 -15 minecraft:lantern
setblock 2 46 -31 minecraft:lodestone
function mg:foot/labels
execute if score $ftoff mg.st matches 1 run function mg:foot/hole_close
data modify storage mg:lobby foot1 set value 1b
