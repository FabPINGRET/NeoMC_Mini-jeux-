# Hall des scores v15 (sud-ouest de la place) : construction + restauration des top 3 (généré par tools/hall/gen_hall.py)
# Chunks du hall pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus
execute store success score #hl mg.st unless block -58 300 18 minecraft:bedrock
execute if score #hl mg.st matches 1 store success score #hl mg.st unless block -14 300 33 minecraft:bedrock
execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0
execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t
scoreboard players set #hlr mg.st 0
kill @e[tag=mg.hall]
execute unless data storage mg:hall v15 run function mg:hall/clear_old

# gros œuvre : terrain dégagé (arbres, ancienne fontaine), dalle, murs, étage, toit
fill -60 64 15 -12 84 36 minecraft:air
fill -60 62 15 -12 62 36 minecraft:stone
fill -60 63 15 -12 63 36 minecraft:polished_andesite
fill -60 64 15 -12 72 15 minecraft:stone_bricks
fill -60 64 36 -12 72 36 minecraft:stone_bricks
fill -60 64 15 -60 72 36 minecraft:stone_bricks
fill -12 64 15 -12 72 36 minecraft:stone_bricks
fill -60 73 15 -12 73 36 minecraft:dark_oak_planks
fill -61 73 14 -11 73 14 minecraft:dark_oak_slab[type=bottom]
fill -61 73 37 -11 73 37 minecraft:dark_oak_slab[type=bottom]
fill -61 73 15 -61 73 36 minecraft:dark_oak_slab[type=bottom]
fill -11 73 15 -11 73 36 minecraft:dark_oak_slab[type=bottom]
fill -60 64 15 -12 64 15 minecraft:mossy_stone_bricks
fill -60 64 36 -12 64 36 minecraft:mossy_stone_bricks
fill -60 64 15 -60 64 36 minecraft:mossy_stone_bricks
fill -12 64 15 -12 64 36 minecraft:mossy_stone_bricks
fill -60 68 15 -12 68 15 minecraft:chiseled_stone_bricks
fill -60 68 36 -12 68 36 minecraft:chiseled_stone_bricks
fill -60 68 15 -60 68 36 minecraft:chiseled_stone_bricks
fill -12 68 15 -12 68 36 minecraft:chiseled_stone_bricks
fill -59 68 16 -13 68 35 minecraft:dark_oak_planks
fill -59 68 25 -13 68 26 minecraft:air
fill -15 68 22 -13 68 29 minecraft:air
fill -51 69 24 -16 69 24 minecraft:dark_oak_fence
fill -51 69 27 -16 69 27 minecraft:dark_oak_fence
fill -16 69 22 -16 69 29 minecraft:dark_oak_fence
fill -16 69 25 -16 69 26 minecraft:air
fill -51 64 25 -51 64 26 minecraft:dark_oak_stairs[facing=west]
fill -52 65 25 -52 65 26 minecraft:dark_oak_stairs[facing=west]
fill -52 64 25 -52 64 26 minecraft:dark_oak_planks
fill -53 66 25 -53 66 26 minecraft:dark_oak_stairs[facing=west]
fill -53 64 25 -53 65 26 minecraft:dark_oak_planks
fill -54 67 25 -54 67 26 minecraft:dark_oak_stairs[facing=west]
fill -54 64 25 -54 66 26 minecraft:dark_oak_planks
fill -59 68 22 -55 68 29 minecraft:dark_oak_planks
fill -50 63 25 -13 63 26 minecraft:red_wool
fill -12 64 23 -12 67 28 minecraft:air
fill -12 68 23 -12 68 28 minecraft:chiseled_stone_bricks
fill -11 63 23 -6 63 28 minecraft:polished_andesite
fill -11 64 23 -6 70 28 minecraft:air
fill -57 70 15 -56 71 15 minecraft:glass_pane
fill -57 70 36 -56 71 36 minecraft:glass_pane
fill -53 70 15 -52 71 15 minecraft:glass_pane
fill -53 70 36 -52 71 36 minecraft:glass_pane
fill -49 70 15 -48 71 15 minecraft:glass_pane
fill -49 70 36 -48 71 36 minecraft:glass_pane
fill -45 70 15 -44 71 15 minecraft:glass_pane
fill -45 70 36 -44 71 36 minecraft:glass_pane
fill -41 70 15 -40 71 15 minecraft:glass_pane
fill -41 70 36 -40 71 36 minecraft:glass_pane
fill -37 70 15 -36 71 15 minecraft:glass_pane
fill -37 70 36 -36 71 36 minecraft:glass_pane
fill -33 70 15 -32 71 15 minecraft:glass_pane
fill -33 70 36 -32 71 36 minecraft:glass_pane
fill -29 70 15 -28 71 15 minecraft:glass_pane
fill -29 70 36 -28 71 36 minecraft:glass_pane
fill -25 70 15 -24 71 15 minecraft:glass_pane
fill -25 70 36 -24 71 36 minecraft:glass_pane
fill -21 70 15 -20 71 15 minecraft:glass_pane
fill -21 70 36 -20 71 36 minecraft:glass_pane
fill -17 70 15 -16 71 15 minecraft:glass_pane
fill -17 70 36 -16 71 36 minecraft:glass_pane
setblock -50 72 25 minecraft:lantern[hanging=true]
setblock -50 72 26 minecraft:lantern[hanging=true]
setblock -44 72 25 minecraft:lantern[hanging=true]
setblock -44 72 26 minecraft:lantern[hanging=true]
setblock -38 72 25 minecraft:lantern[hanging=true]
setblock -38 72 26 minecraft:lantern[hanging=true]
setblock -32 72 25 minecraft:lantern[hanging=true]
setblock -32 72 26 minecraft:lantern[hanging=true]
setblock -26 72 25 minecraft:lantern[hanging=true]
setblock -26 72 26 minecraft:lantern[hanging=true]
setblock -20 72 25 minecraft:lantern[hanging=true]
setblock -20 72 26 minecraft:lantern[hanging=true]
setblock -57 72 18 minecraft:sea_lantern
setblock -57 72 33 minecraft:sea_lantern
setblock -53 72 18 minecraft:sea_lantern
setblock -53 72 33 minecraft:sea_lantern
setblock -49 72 18 minecraft:sea_lantern
setblock -49 72 33 minecraft:sea_lantern
setblock -45 72 18 minecraft:sea_lantern
setblock -45 72 33 minecraft:sea_lantern
setblock -41 72 18 minecraft:sea_lantern
setblock -41 72 33 minecraft:sea_lantern
setblock -37 72 18 minecraft:sea_lantern
setblock -37 72 33 minecraft:sea_lantern
setblock -33 72 18 minecraft:sea_lantern
setblock -33 72 33 minecraft:sea_lantern
setblock -29 72 18 minecraft:sea_lantern
setblock -29 72 33 minecraft:sea_lantern
setblock -25 72 18 minecraft:sea_lantern
setblock -25 72 33 minecraft:sea_lantern
setblock -21 72 18 minecraft:sea_lantern
setblock -21 72 33 minecraft:sea_lantern
setblock -17 72 18 minecraft:sea_lantern
setblock -17 72 33 minecraft:sea_lantern
fill -56 64 16 -56 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -59 63 16 -57 63 21 minecraft:light_blue_concrete
fill -59 64 16 -57 64 16 minecraft:polished_andesite
setblock -58 64 17 minecraft:gold_block
setblock -58 65 16 minecraft:gold_block
setblock -59 64 17 minecraft:iron_block
setblock -57 64 17 minecraft:copper_block
setblock -58 67 18 minecraft:light[level=15]
setblock -58 67 20 minecraft:light[level=12]
fill -52 64 16 -52 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -55 63 16 -53 63 21 minecraft:red_concrete
fill -55 64 16 -53 64 16 minecraft:polished_andesite
setblock -54 64 17 minecraft:gold_block
setblock -54 65 16 minecraft:gold_block
setblock -55 64 17 minecraft:iron_block
setblock -53 64 17 minecraft:copper_block
setblock -54 67 18 minecraft:light[level=15]
setblock -54 67 20 minecraft:light[level=12]
fill -48 64 16 -48 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -51 63 16 -49 63 21 minecraft:yellow_concrete
fill -51 64 16 -49 64 16 minecraft:polished_andesite
setblock -50 64 17 minecraft:gold_block
setblock -50 65 16 minecraft:gold_block
setblock -51 64 17 minecraft:iron_block
setblock -49 64 17 minecraft:copper_block
setblock -50 67 18 minecraft:light[level=15]
setblock -50 67 20 minecraft:light[level=12]
fill -44 64 16 -44 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -47 63 16 -45 63 21 minecraft:red_concrete
fill -47 64 16 -45 64 16 minecraft:polished_andesite
setblock -46 64 17 minecraft:gold_block
setblock -46 65 16 minecraft:gold_block
setblock -47 64 17 minecraft:iron_block
setblock -45 64 17 minecraft:copper_block
setblock -46 67 18 minecraft:light[level=15]
setblock -46 67 20 minecraft:light[level=12]
fill -40 64 16 -40 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -43 63 16 -41 63 21 minecraft:white_concrete
fill -43 64 16 -41 64 16 minecraft:polished_andesite
setblock -42 64 17 minecraft:gold_block
setblock -42 65 16 minecraft:gold_block
setblock -43 64 17 minecraft:iron_block
setblock -41 64 17 minecraft:copper_block
setblock -42 67 18 minecraft:light[level=15]
setblock -42 67 20 minecraft:light[level=12]
fill -36 64 16 -36 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -39 63 16 -37 63 21 minecraft:green_concrete
fill -39 64 16 -37 64 16 minecraft:polished_andesite
setblock -38 64 17 minecraft:gold_block
setblock -38 65 16 minecraft:gold_block
setblock -39 64 17 minecraft:iron_block
setblock -37 64 17 minecraft:copper_block
setblock -38 67 18 minecraft:light[level=15]
setblock -38 67 20 minecraft:light[level=12]
fill -32 64 16 -32 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -35 63 16 -33 63 21 minecraft:yellow_concrete
fill -35 64 16 -33 64 16 minecraft:polished_andesite
setblock -34 64 17 minecraft:gold_block
setblock -34 65 16 minecraft:gold_block
setblock -35 64 17 minecraft:iron_block
setblock -33 64 17 minecraft:copper_block
setblock -34 67 18 minecraft:light[level=15]
setblock -34 67 20 minecraft:light[level=12]
fill -28 64 16 -28 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -31 63 16 -29 63 21 minecraft:yellow_concrete
fill -31 64 16 -29 64 16 minecraft:polished_andesite
setblock -30 64 17 minecraft:gold_block
setblock -30 65 16 minecraft:gold_block
setblock -31 64 17 minecraft:iron_block
setblock -29 64 17 minecraft:copper_block
setblock -30 67 18 minecraft:light[level=15]
setblock -30 67 20 minecraft:light[level=12]
fill -24 64 16 -24 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -27 63 16 -25 63 21 minecraft:light_blue_concrete
fill -27 64 16 -25 64 16 minecraft:polished_andesite
setblock -26 64 17 minecraft:gold_block
setblock -26 65 16 minecraft:gold_block
setblock -27 64 17 minecraft:iron_block
setblock -25 64 17 minecraft:copper_block
setblock -26 67 18 minecraft:light[level=15]
setblock -26 67 20 minecraft:light[level=12]
fill -20 64 16 -20 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -23 63 16 -21 63 21 minecraft:yellow_concrete
fill -23 64 16 -21 64 16 minecraft:polished_andesite
setblock -22 64 17 minecraft:gold_block
setblock -22 65 16 minecraft:gold_block
setblock -23 64 17 minecraft:iron_block
setblock -21 64 17 minecraft:copper_block
setblock -22 67 18 minecraft:light[level=15]
setblock -22 67 20 minecraft:light[level=12]
fill -16 64 16 -16 67 21 minecraft:stripped_dark_oak_log[axis=y]
fill -19 63 16 -17 63 21 minecraft:red_concrete
fill -19 64 16 -17 64 16 minecraft:polished_andesite
setblock -18 64 17 minecraft:gold_block
setblock -18 65 16 minecraft:gold_block
setblock -19 64 17 minecraft:iron_block
setblock -17 64 17 minecraft:copper_block
setblock -18 67 18 minecraft:light[level=15]
setblock -18 67 20 minecraft:light[level=12]
fill -56 64 30 -56 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -59 63 30 -57 63 35 minecraft:magenta_concrete
fill -59 64 35 -57 64 35 minecraft:polished_andesite
setblock -58 64 34 minecraft:gold_block
setblock -58 65 35 minecraft:gold_block
setblock -59 64 34 minecraft:iron_block
setblock -57 64 34 minecraft:copper_block
setblock -58 67 32 minecraft:light[level=15]
setblock -58 67 34 minecraft:light[level=12]
fill -52 64 30 -52 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -55 63 30 -53 63 35 minecraft:gray_concrete
fill -55 64 35 -53 64 35 minecraft:polished_andesite
setblock -54 64 34 minecraft:gold_block
setblock -54 65 35 minecraft:gold_block
setblock -55 64 34 minecraft:iron_block
setblock -53 64 34 minecraft:copper_block
setblock -54 67 32 minecraft:light[level=15]
setblock -54 67 34 minecraft:light[level=12]
fill -48 64 30 -48 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -51 63 30 -49 63 35 minecraft:yellow_concrete
fill -51 64 35 -49 64 35 minecraft:polished_andesite
setblock -50 64 34 minecraft:gold_block
setblock -50 65 35 minecraft:gold_block
setblock -51 64 34 minecraft:iron_block
setblock -49 64 34 minecraft:copper_block
setblock -50 67 32 minecraft:light[level=15]
setblock -50 67 34 minecraft:light[level=12]
fill -44 64 30 -44 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -47 63 30 -45 63 35 minecraft:light_blue_concrete
fill -47 64 35 -45 64 35 minecraft:polished_andesite
setblock -46 64 34 minecraft:gold_block
setblock -46 65 35 minecraft:gold_block
setblock -47 64 34 minecraft:iron_block
setblock -45 64 34 minecraft:copper_block
setblock -46 67 32 minecraft:light[level=15]
setblock -46 67 34 minecraft:light[level=12]
fill -40 64 30 -40 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -43 63 30 -41 63 35 minecraft:yellow_concrete
fill -43 64 35 -41 64 35 minecraft:polished_andesite
setblock -42 64 34 minecraft:gold_block
setblock -42 65 35 minecraft:gold_block
setblock -43 64 34 minecraft:iron_block
setblock -41 64 34 minecraft:copper_block
setblock -42 67 32 minecraft:light[level=15]
setblock -42 67 34 minecraft:light[level=12]
fill -36 64 30 -36 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -39 63 30 -37 63 35 minecraft:light_blue_concrete
fill -39 64 35 -37 64 35 minecraft:polished_andesite
setblock -38 64 34 minecraft:gold_block
setblock -38 65 35 minecraft:gold_block
setblock -39 64 34 minecraft:iron_block
setblock -37 64 34 minecraft:copper_block
setblock -38 67 32 minecraft:light[level=15]
setblock -38 67 34 minecraft:light[level=12]
fill -32 64 30 -32 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -35 63 30 -33 63 35 minecraft:lime_concrete
fill -35 64 35 -33 64 35 minecraft:polished_andesite
setblock -34 64 34 minecraft:gold_block
setblock -34 65 35 minecraft:gold_block
setblock -35 64 34 minecraft:iron_block
setblock -33 64 34 minecraft:copper_block
setblock -34 67 32 minecraft:light[level=15]
setblock -34 67 34 minecraft:light[level=12]
fill -28 64 30 -28 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -31 63 30 -29 63 35 minecraft:yellow_concrete
fill -31 64 35 -29 64 35 minecraft:polished_andesite
setblock -30 64 34 minecraft:gold_block
setblock -30 65 35 minecraft:gold_block
setblock -31 64 34 minecraft:iron_block
setblock -29 64 34 minecraft:copper_block
setblock -30 67 32 minecraft:light[level=15]
setblock -30 67 34 minecraft:light[level=12]
fill -24 64 30 -24 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -27 63 30 -25 63 35 minecraft:red_concrete
fill -27 64 35 -25 64 35 minecraft:polished_andesite
setblock -26 64 34 minecraft:gold_block
setblock -26 65 35 minecraft:gold_block
setblock -27 64 34 minecraft:iron_block
setblock -25 64 34 minecraft:copper_block
setblock -26 67 32 minecraft:light[level=15]
setblock -26 67 34 minecraft:light[level=12]
fill -20 64 30 -20 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -23 63 30 -21 63 35 minecraft:light_blue_concrete
fill -23 64 35 -21 64 35 minecraft:polished_andesite
setblock -22 64 34 minecraft:gold_block
setblock -22 65 35 minecraft:gold_block
setblock -23 64 34 minecraft:iron_block
setblock -21 64 34 minecraft:copper_block
setblock -22 67 32 minecraft:light[level=15]
setblock -22 67 34 minecraft:light[level=12]
fill -16 64 30 -16 67 35 minecraft:stripped_dark_oak_log[axis=y]
fill -19 63 30 -17 63 35 minecraft:light_blue_concrete
fill -19 64 35 -17 64 35 minecraft:polished_andesite
setblock -18 64 34 minecraft:gold_block
setblock -18 65 35 minecraft:gold_block
setblock -19 64 34 minecraft:iron_block
setblock -17 64 34 minecraft:copper_block
setblock -18 67 32 minecraft:light[level=15]
setblock -18 67 34 minecraft:light[level=12]
fill -56 69 16 -56 72 21 minecraft:stripped_spruce_log[axis=y]
fill -59 68 16 -57 68 21 minecraft:yellow_concrete
fill -59 69 16 -57 69 16 minecraft:polished_andesite
setblock -58 69 17 minecraft:gold_block
setblock -58 70 16 minecraft:gold_block
setblock -59 69 17 minecraft:iron_block
setblock -57 69 17 minecraft:copper_block
setblock -58 72 18 minecraft:light[level=15]
setblock -58 72 20 minecraft:light[level=12]
fill -52 69 16 -52 72 21 minecraft:stripped_spruce_log[axis=y]
fill -55 68 16 -53 68 21 minecraft:light_blue_concrete
fill -55 69 16 -53 69 16 minecraft:polished_andesite
setblock -54 69 17 minecraft:gold_block
setblock -54 70 16 minecraft:gold_block
setblock -55 69 17 minecraft:iron_block
setblock -53 69 17 minecraft:copper_block
setblock -54 72 18 minecraft:light[level=15]
setblock -54 72 20 minecraft:light[level=12]
fill -48 69 16 -48 72 21 minecraft:stripped_spruce_log[axis=y]
fill -51 68 16 -49 68 21 minecraft:yellow_concrete
fill -51 69 16 -49 69 16 minecraft:polished_andesite
setblock -50 69 17 minecraft:gold_block
setblock -50 70 16 minecraft:gold_block
setblock -51 69 17 minecraft:iron_block
setblock -49 69 17 minecraft:copper_block
setblock -50 72 18 minecraft:light[level=15]
setblock -50 72 20 minecraft:light[level=12]
fill -44 69 16 -44 72 21 minecraft:stripped_spruce_log[axis=y]
fill -47 68 16 -45 68 21 minecraft:yellow_concrete
fill -47 69 16 -45 69 16 minecraft:polished_andesite
setblock -46 69 17 minecraft:gold_block
setblock -46 70 16 minecraft:gold_block
setblock -47 69 17 minecraft:iron_block
setblock -45 69 17 minecraft:copper_block
setblock -46 72 18 minecraft:light[level=15]
setblock -46 72 20 minecraft:light[level=12]
fill -40 69 16 -40 72 21 minecraft:stripped_spruce_log[axis=y]
fill -43 68 16 -41 68 21 minecraft:yellow_concrete
fill -43 69 16 -41 69 16 minecraft:polished_andesite
setblock -42 69 17 minecraft:gold_block
setblock -42 70 16 minecraft:gold_block
setblock -43 69 17 minecraft:iron_block
setblock -41 69 17 minecraft:copper_block
setblock -42 72 18 minecraft:light[level=15]
setblock -42 72 20 minecraft:light[level=12]
fill -36 69 16 -36 72 21 minecraft:stripped_spruce_log[axis=y]
fill -39 68 16 -37 68 21 minecraft:red_concrete
fill -39 69 16 -37 69 16 minecraft:polished_andesite
setblock -38 69 17 minecraft:gold_block
setblock -38 70 16 minecraft:gold_block
setblock -39 69 17 minecraft:iron_block
setblock -37 69 17 minecraft:copper_block
setblock -38 72 18 minecraft:light[level=15]
setblock -38 72 20 minecraft:light[level=12]
fill -32 69 16 -32 72 21 minecraft:stripped_spruce_log[axis=y]
fill -35 68 16 -33 68 21 minecraft:yellow_concrete
fill -35 69 16 -33 69 16 minecraft:polished_andesite
setblock -34 69 17 minecraft:gold_block
setblock -34 70 16 minecraft:gold_block
setblock -35 69 17 minecraft:iron_block
setblock -33 69 17 minecraft:copper_block
setblock -34 72 18 minecraft:light[level=15]
setblock -34 72 20 minecraft:light[level=12]
fill -28 69 16 -28 72 21 minecraft:stripped_spruce_log[axis=y]
fill -31 68 16 -29 68 21 minecraft:yellow_concrete
fill -31 69 16 -29 69 16 minecraft:polished_andesite
setblock -30 69 17 minecraft:gold_block
setblock -30 70 16 minecraft:gold_block
setblock -31 69 17 minecraft:iron_block
setblock -29 69 17 minecraft:copper_block
setblock -30 72 18 minecraft:light[level=15]
setblock -30 72 20 minecraft:light[level=12]
fill -24 69 16 -24 72 21 minecraft:stripped_spruce_log[axis=y]
fill -27 68 16 -25 68 21 minecraft:yellow_concrete
fill -27 69 16 -25 69 16 minecraft:polished_andesite
setblock -26 69 17 minecraft:gold_block
setblock -26 70 16 minecraft:gold_block
setblock -27 69 17 minecraft:iron_block
setblock -25 69 17 minecraft:copper_block
setblock -26 72 18 minecraft:light[level=15]
setblock -26 72 20 minecraft:light[level=12]
fill -20 69 16 -20 72 21 minecraft:stripped_spruce_log[axis=y]
fill -23 68 16 -21 68 21 minecraft:green_concrete
fill -23 69 16 -21 69 16 minecraft:polished_andesite
setblock -22 69 17 minecraft:gold_block
setblock -22 70 16 minecraft:gold_block
setblock -23 69 17 minecraft:iron_block
setblock -21 69 17 minecraft:copper_block
setblock -22 72 18 minecraft:light[level=15]
setblock -22 72 20 minecraft:light[level=12]
fill -16 69 16 -16 72 21 minecraft:stripped_spruce_log[axis=y]
fill -19 68 16 -17 68 21 minecraft:lime_concrete
fill -19 69 16 -17 69 16 minecraft:polished_andesite
setblock -18 69 17 minecraft:gold_block
setblock -18 70 16 minecraft:gold_block
setblock -19 69 17 minecraft:iron_block
setblock -17 69 17 minecraft:copper_block
setblock -18 72 18 minecraft:light[level=15]
setblock -18 72 20 minecraft:light[level=12]
fill -56 69 30 -56 72 35 minecraft:stripped_spruce_log[axis=y]
fill -59 68 30 -57 68 35 minecraft:red_concrete
fill -59 69 35 -57 69 35 minecraft:polished_andesite
setblock -58 69 34 minecraft:gold_block
setblock -58 70 35 minecraft:gold_block
setblock -59 69 34 minecraft:iron_block
setblock -57 69 34 minecraft:copper_block
setblock -58 72 32 minecraft:light[level=15]
setblock -58 72 34 minecraft:light[level=12]
fill -52 69 30 -52 72 35 minecraft:stripped_spruce_log[axis=y]
fill -55 68 30 -53 68 35 minecraft:lime_concrete
fill -55 69 35 -53 69 35 minecraft:polished_andesite
setblock -54 69 34 minecraft:gold_block
setblock -54 70 35 minecraft:gold_block
setblock -55 69 34 minecraft:iron_block
setblock -53 69 34 minecraft:copper_block
setblock -54 72 32 minecraft:light[level=15]
setblock -54 72 34 minecraft:light[level=12]
fill -48 69 30 -48 72 35 minecraft:stripped_spruce_log[axis=y]
fill -51 68 30 -49 68 35 minecraft:light_blue_concrete
fill -51 69 35 -49 69 35 minecraft:polished_andesite
setblock -50 69 34 minecraft:gold_block
setblock -50 70 35 minecraft:gold_block
setblock -51 69 34 minecraft:iron_block
setblock -49 69 34 minecraft:copper_block
setblock -50 72 32 minecraft:light[level=15]
setblock -50 72 34 minecraft:light[level=12]
fill -44 69 30 -44 72 35 minecraft:stripped_spruce_log[axis=y]
fill -47 68 30 -45 68 35 minecraft:red_concrete
fill -47 69 35 -45 69 35 minecraft:polished_andesite
setblock -46 69 34 minecraft:gold_block
setblock -46 70 35 minecraft:gold_block
setblock -47 69 34 minecraft:iron_block
setblock -45 69 34 minecraft:copper_block
setblock -46 72 32 minecraft:light[level=15]
setblock -46 72 34 minecraft:light[level=12]
fill -40 69 30 -40 72 35 minecraft:stripped_spruce_log[axis=y]
fill -43 68 30 -41 68 35 minecraft:light_blue_concrete
fill -43 69 35 -41 69 35 minecraft:polished_andesite
setblock -42 69 34 minecraft:gold_block
setblock -42 70 35 minecraft:gold_block
setblock -43 69 34 minecraft:iron_block
setblock -41 69 34 minecraft:copper_block
setblock -42 72 32 minecraft:light[level=15]
setblock -42 72 34 minecraft:light[level=12]
fill -36 69 30 -36 72 35 minecraft:stripped_spruce_log[axis=y]
fill -39 68 30 -37 68 35 minecraft:lime_concrete
fill -39 69 35 -37 69 35 minecraft:polished_andesite
setblock -38 69 34 minecraft:gold_block
setblock -38 70 35 minecraft:gold_block
setblock -39 69 34 minecraft:iron_block
setblock -37 69 34 minecraft:copper_block
setblock -38 72 32 minecraft:light[level=15]
setblock -38 72 34 minecraft:light[level=12]
fill -32 69 30 -32 72 35 minecraft:stripped_spruce_log[axis=y]
fill -35 68 30 -33 68 35 minecraft:magenta_concrete
fill -35 69 35 -33 69 35 minecraft:polished_andesite
setblock -34 69 34 minecraft:gold_block
setblock -34 70 35 minecraft:gold_block
setblock -35 69 34 minecraft:iron_block
setblock -33 69 34 minecraft:copper_block
setblock -34 72 32 minecraft:light[level=15]
setblock -34 72 34 minecraft:light[level=12]
fill -28 69 30 -28 72 35 minecraft:stripped_spruce_log[axis=y]
fill -31 68 30 -29 68 35 minecraft:yellow_concrete
fill -31 69 35 -29 69 35 minecraft:polished_andesite
setblock -30 69 34 minecraft:gold_block
setblock -30 70 35 minecraft:gold_block
setblock -31 69 34 minecraft:iron_block
setblock -29 69 34 minecraft:copper_block
setblock -30 72 32 minecraft:light[level=15]
setblock -30 72 34 minecraft:light[level=12]
fill -24 69 30 -24 72 35 minecraft:stripped_spruce_log[axis=y]
fill -27 68 30 -25 68 35 minecraft:red_concrete
fill -27 69 35 -25 69 35 minecraft:polished_andesite
setblock -26 69 34 minecraft:gold_block
setblock -26 70 35 minecraft:gold_block
setblock -27 69 34 minecraft:iron_block
setblock -25 69 34 minecraft:copper_block
setblock -26 72 32 minecraft:light[level=15]
setblock -26 72 34 minecraft:light[level=12]
fill -20 69 30 -20 72 35 minecraft:stripped_spruce_log[axis=y]
fill -23 68 30 -21 68 35 minecraft:red_concrete
fill -23 69 35 -21 69 35 minecraft:polished_andesite
setblock -22 69 34 minecraft:gold_block
setblock -22 70 35 minecraft:gold_block
setblock -23 69 34 minecraft:iron_block
setblock -21 69 34 minecraft:copper_block
setblock -22 72 32 minecraft:light[level=15]
setblock -22 72 34 minecraft:light[level=12]
fill -16 69 30 -16 72 35 minecraft:stripped_spruce_log[axis=y]
fill -19 68 30 -17 68 35 minecraft:magenta_concrete
fill -19 69 35 -17 69 35 minecraft:polished_andesite
setblock -18 69 34 minecraft:gold_block
setblock -18 70 35 minecraft:gold_block
setblock -19 69 34 minecraft:iron_block
setblock -17 69 34 minecraft:copper_block
setblock -18 72 32 minecraft:light[level=15]
setblock -18 72 34 minecraft:light[level=12]

# salle d'honneur (sous le palier ouest) et ses piédestaux
fill -58 63 22 -56 63 29 minecraft:smooth_quartz
setblock -58 64 23 minecraft:emerald_block
setblock -58 64 26 minecraft:gold_block
setblock -58 64 29 minecraft:lapis_block
fill -59 67 22 -59 67 29 minecraft:sea_lantern

# Tampon de résolution des noms (invisible)
summon minecraft:item_display -57.5 64.5 26.5 {Tags:["mg.hall","mg.hallbuf"],item:{id:"minecraft:paper"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.001f,0.001f,0.001f]}}
summon minecraft:text_display -11.4 69.6 26.0 {Tags:["mg.hall"],billboard:"vertical",background:0,text:[{"text":"🏆 Hall des scores","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -35 72.2 26.0 {Tags:["mg.hall"],billboard:"vertical",background:0,text:[{"text":"🏆 Hall des scores","color":"gold","bold":true},{"text":"\n🥇 🥈 🥉 le top 3 de chaque jeu — étage par l'escalier du fond","color":"gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}

# Piédestaux : objet qui tourne + plaque
summon minecraft:item_display -57.5 65.8 23.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:clock"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -57.5 65.8 26.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:totem_of_undying"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -57.5 65.8 29.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}

# Plaques d'honneur : texte par défaut, puis meneur enregistré s'il existe
summon minecraft:text_display -57.5 66.6 23.5 {Tags:["mg.hall","mg.h_stp"],billboard:"vertical",line_width:115,text:[{"text":"▶ Le plus assidu","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.stp run data modify entity @e[type=minecraft:text_display,tag=mg.h_stp,limit=1] text set from storage mg:hall e.stp
summon minecraft:text_display -57.5 66.6 26.5 {Tags:["mg.hall","mg.h_wins"],billboard:"vertical",line_width:115,text:[{"text":"👑 Champion des mini-jeux","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.wins run data modify entity @e[type=minecraft:text_display,tag=mg.h_wins,limit=1] text set from storage mg:hall e.wins
summon minecraft:text_display -57.5 66.6 29.5 {Tags:["mg.hall","mg.h_ely"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record petit parcours d'élytra","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely,limit=1] text set from storage mg:hall e.ely
summon minecraft:text_display -58.6 70.4 23.5 {Tags:["mg.hall","mg.h_ely2"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record grand parcours d'élytra","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely2 run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely2,limit=1] text set from storage mg:hall e.ely2
summon minecraft:text_display -58.6 70.4 29.5 {Tags:["mg.hall","mg.h_elyg"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record Élytra : course","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.elyg run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyg,limit=1] text set from storage mg:hall e.elyg
summon minecraft:text_display -58.6 71.4 26.5 {Tags:["mg.hall","mg.h_gen"],billboard:"vertical",line_width:200,text:[{"text":"🏅 Meilleur niveau général","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.1f,1.1f,1.1f]}}
execute if data storage mg:hall e.gen run data modify entity @e[type=minecraft:text_display,tag=mg.h_gen,limit=1] text set from storage mg:hall e.gen

# Stands : top 3 de chaque jeu (texte par défaut, puis top 3 enregistré)
summon minecraft:text_display -57.5 66.0 16.6 {Tags:["mg.hall","mg.h3_spleef"],billboard:"vertical",line_width:110,text:[{"text":"❄ Spleef","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.spleef run data modify entity @e[type=minecraft:text_display,tag=mg.h3_spleef,limit=1] text set from storage mg:hall t3x.spleef
summon minecraft:text_display -53.5 66.0 16.6 {Tags:["mg.hall","mg.h3_tntrun"],billboard:"vertical",line_width:110,text:[{"text":"✷ TNT Run","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.tntrun run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tntrun,limit=1] text set from storage mg:hall t3x.tntrun
summon minecraft:text_display -49.5 66.0 16.6 {Tags:["mg.hall","mg.h3_pvp"],billboard:"vertical",line_width:110,text:[{"text":"⚔ PvP","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.pvp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_pvp,limit=1] text set from storage mg:hall t3x.pvp
summon minecraft:text_display -45.5 66.0 16.6 {Tags:["mg.hall","mg.h3_bedwars"],billboard:"vertical",line_width:110,text:[{"text":"🛏 Bedwars","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.bedwars run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bedwars,limit=1] text set from storage mg:hall t3x.bedwars
summon minecraft:text_display -41.5 66.0 16.6 {Tags:["mg.hall","mg.h3_sheepwar"],billboard:"vertical",line_width:110,text:[{"text":"🐑 Sheep War","color":"white","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.sheepwar run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sheepwar,limit=1] text set from storage mg:hall t3x.sheepwar
summon minecraft:text_display -37.5 66.0 16.6 {Tags:["mg.hall","mg.h3_mobarena"],billboard:"vertical",line_width:110,text:[{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.mobarena run data modify entity @e[type=minecraft:text_display,tag=mg.h3_mobarena,limit=1] text set from storage mg:hall t3x.mobarena
summon minecraft:text_display -33.5 66.0 16.6 {Tags:["mg.hall","mg.h3_splegg"],billboard:"vertical",line_width:110,text:[{"text":"❍ Splegg","color":"yellow","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.splegg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_splegg,limit=1] text set from storage mg:hall t3x.splegg
summon minecraft:text_display -29.5 66.0 16.6 {Tags:["mg.hall","mg.h3_sumo"],billboard:"vertical",line_width:110,text:[{"text":"✊ Sumo","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.sumo run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sumo,limit=1] text set from storage mg:hall t3x.sumo
summon minecraft:text_display -25.5 66.0 16.6 {Tags:["mg.hall","mg.h3_dropper"],billboard:"vertical",line_width:110,text:[{"text":"⬇ Dropper","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.dropper run data modify entity @e[type=minecraft:text_display,tag=mg.h3_dropper,limit=1] text set from storage mg:hall t3x.dropper
summon minecraft:text_display -21.5 66.0 16.6 {Tags:["mg.hall","mg.h3_oitc"],billboard:"vertical",line_width:110,text:[{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.oitc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_oitc,limit=1] text set from storage mg:hall t3x.oitc
summon minecraft:text_display -17.5 66.0 16.6 {Tags:["mg.hall","mg.h3_tnttag"],billboard:"vertical",line_width:110,text:[{"text":"✹ TNT Tag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.tnttag run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tnttag,limit=1] text set from storage mg:hall t3x.tnttag
summon minecraft:text_display -57.5 66.0 35.4 {Tags:["mg.hall","mg.h3_blockparty"],billboard:"vertical",line_width:110,text:[{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.blockparty run data modify entity @e[type=minecraft:text_display,tag=mg.h3_blockparty,limit=1] text set from storage mg:hall t3x.blockparty
summon minecraft:text_display -53.5 66.0 35.4 {Tags:["mg.hall","mg.h3_anvil"],billboard:"vertical",line_width:110,text:[{"text":"⚓ Pluie d'enclumes","color":"gray","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.anvil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_anvil,limit=1] text set from storage mg:hall t3x.anvil
summon minecraft:text_display -49.5 66.0 35.4 {Tags:["mg.hall","mg.h3_turf"],billboard:"vertical",line_width:110,text:[{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.turf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_turf,limit=1] text set from storage mg:hall t3x.turf
summon minecraft:text_display -45.5 66.0 35.4 {Tags:["mg.hall","mg.h3_quake"],billboard:"vertical",line_width:110,text:[{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.quake run data modify entity @e[type=minecraft:text_display,tag=mg.h3_quake,limit=1] text set from storage mg:hall t3x.quake
summon minecraft:text_display -41.5 66.0 35.4 {Tags:["mg.hall","mg.h3_paintball"],billboard:"vertical",line_width:110,text:[{"text":"▓ Paintball","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.paintball run data modify entity @e[type=minecraft:text_display,tag=mg.h3_paintball,limit=1] text set from storage mg:hall t3x.paintball
summon minecraft:text_display -37.5 66.0 35.4 {Tags:["mg.hall","mg.h3_icerace"],billboard:"vertical",line_width:110,text:[{"text":"⛵ Course de bateaux","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.icerace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_icerace,limit=1] text set from storage mg:hall t3x.icerace
summon minecraft:text_display -33.5 66.0 35.4 {Tags:["mg.hall","mg.h3_bb"],billboard:"vertical",line_width:110,text:[{"text":"✎ Build Battle","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.bb run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bb,limit=1] text set from storage mg:hall t3x.bb
summon minecraft:text_display -29.5 66.0 35.4 {Tags:["mg.hall","mg.h3_party"],billboard:"vertical",line_width:110,text:[{"text":"★ Mini Party","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.party run data modify entity @e[type=minecraft:text_display,tag=mg.h3_party,limit=1] text set from storage mg:hall t3x.party
summon minecraft:text_display -25.5 66.0 35.4 {Tags:["mg.hall","mg.h3_kart"],billboard:"vertical",line_width:110,text:[{"text":"🏎 Kart","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.kart run data modify entity @e[type=minecraft:text_display,tag=mg.h3_kart,limit=1] text set from storage mg:hall t3x.kart
summon minecraft:text_display -21.5 66.0 35.4 {Tags:["mg.hall","mg.h3_elyrace"],billboard:"vertical",line_width:110,text:[{"text":"🪽 Course d'élytres","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.elyrace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elyrace,limit=1] text set from storage mg:hall t3x.elyrace
summon minecraft:text_display -17.5 66.0 35.4 {Tags:["mg.hall","mg.h3_elytra"],billboard:"vertical",line_width:110,text:[{"text":"🪽 Élytra (3 modes)","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.elytra run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elytra,limit=1] text set from storage mg:hall t3x.elytra
summon minecraft:text_display -57.5 71.0 16.6 {Tags:["mg.hall","mg.h3_telephone"],billboard:"vertical",line_width:110,text:[{"text":"📞 Téléphone","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.telephone run data modify entity @e[type=minecraft:text_display,tag=mg.h3_telephone,limit=1] text set from storage mg:hall t3x.telephone
summon minecraft:text_display -53.5 71.0 16.6 {Tags:["mg.hall","mg.h3_tron"],billboard:"vertical",line_width:110,text:[{"text":"⚡ Tron","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.tron run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tron,limit=1] text set from storage mg:hall t3x.tron
summon minecraft:text_display -49.5 71.0 16.6 {Tags:["mg.hall","mg.h3_koth"],billboard:"vertical",line_width:110,text:[{"text":"👑 King of the Hill","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.koth run data modify entity @e[type=minecraft:text_display,tag=mg.h3_koth,limit=1] text set from storage mg:hall t3x.koth
summon minecraft:text_display -45.5 71.0 16.6 {Tags:["mg.hall","mg.h3_tower"],billboard:"vertical",line_width:110,text:[{"text":"🏰 The Towers","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.tower run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tower,limit=1] text set from storage mg:hall t3x.tower
summon minecraft:text_display -41.5 71.0 16.6 {Tags:["mg.hall","mg.h3_convoy"],billboard:"vertical",line_width:110,text:[{"text":"🚚 Convoi","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.convoy run data modify entity @e[type=minecraft:text_display,tag=mg.h3_convoy,limit=1] text set from storage mg:hall t3x.convoy
summon minecraft:text_display -37.5 71.0 16.6 {Tags:["mg.hall","mg.h3_ctf"],billboard:"vertical",line_width:110,text:[{"text":"🚩 Capture the Flag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.ctf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_ctf,limit=1] text set from storage mg:hall t3x.ctf
summon minecraft:text_display -33.5 71.0 16.6 {Tags:["mg.hall","mg.h3_uhc"],billboard:"vertical",line_width:110,text:[{"text":"⛏ Mini UHC Run","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.uhc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_uhc,limit=1] text set from storage mg:hall t3x.uhc
summon minecraft:text_display -29.5 71.0 16.6 {Tags:["mg.hall","mg.h3_hg"],billboard:"vertical",line_width:110,text:[{"text":"🏹 Mini Hunger Games","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.hg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_hg,limit=1] text set from storage mg:hall t3x.hg
summon minecraft:text_display -25.5 71.0 16.6 {Tags:["mg.hall","mg.h3_prophunt"],billboard:"vertical",line_width:110,text:[{"text":"🎭 Prop Hunt","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.prophunt run data modify entity @e[type=minecraft:text_display,tag=mg.h3_prophunt,limit=1] text set from storage mg:hall t3x.prophunt
summon minecraft:text_display -21.5 71.0 16.6 {Tags:["mg.hall","mg.h3_zombies"],billboard:"vertical",line_width:110,text:[{"text":"🧟 Zombies","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.zombies run data modify entity @e[type=minecraft:text_display,tag=mg.h3_zombies,limit=1] text set from storage mg:hall t3x.zombies
summon minecraft:text_display -17.5 71.0 16.6 {Tags:["mg.hall","mg.h3_infection"],billboard:"vertical",line_width:110,text:[{"text":"🧪 Infection","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.infection run data modify entity @e[type=minecraft:text_display,tag=mg.h3_infection,limit=1] text set from storage mg:hall t3x.infection
summon minecraft:text_display -57.5 71.0 35.4 {Tags:["mg.hall","mg.h3_bomber"],billboard:"vertical",line_width:110,text:[{"text":"💣 Bombardier","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.bomber run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bomber,limit=1] text set from storage mg:hall t3x.bomber
summon minecraft:text_display -53.5 71.0 35.4 {Tags:["mg.hall","mg.h3_chameleon"],billboard:"vertical",line_width:110,text:[{"text":"🦎 Meccha Chameleon","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.chameleon run data modify entity @e[type=minecraft:text_display,tag=mg.h3_chameleon,limit=1] text set from storage mg:hall t3x.chameleon
summon minecraft:text_display -49.5 71.0 35.4 {Tags:["mg.hall","mg.h3_wii"],billboard:"vertical",line_width:110,text:[{"text":"🎾 Wii Sports","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.wii run data modify entity @e[type=minecraft:text_display,tag=mg.h3_wii,limit=1] text set from storage mg:hall t3x.wii
summon minecraft:text_display -45.5 71.0 35.4 {Tags:["mg.hall","mg.h3_soleil"],billboard:"vertical",line_width:110,text:[{"text":"🔴 1, 2, 3 Soleil","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.soleil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_soleil,limit=1] text set from storage mg:hall t3x.soleil
summon minecraft:text_display -41.5 71.0 35.4 {Tags:["mg.hall","mg.h3_autotamp"],billboard:"vertical",line_width:110,text:[{"text":"🚗 Autos tamponneuses","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.autotamp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_autotamp,limit=1] text set from storage mg:hall t3x.autotamp
summon minecraft:text_display -37.5 71.0 35.4 {Tags:["mg.hall","mg.h3_slimejump"],billboard:"vertical",line_width:110,text:[{"text":"🟩 Slime Jump","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.slimejump run data modify entity @e[type=minecraft:text_display,tag=mg.h3_slimejump,limit=1] text set from storage mg:hall t3x.slimejump
summon minecraft:text_display -33.5 71.0 35.4 {Tags:["mg.hall","mg.h3_lab"],billboard:"vertical",line_width:110,text:[{"text":"🙈 Labyrinthe aveugle","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.lab run data modify entity @e[type=minecraft:text_display,tag=mg.h3_lab,limit=1] text set from storage mg:hall t3x.lab
summon minecraft:text_display -29.5 71.0 35.4 {Tags:["mg.hall","mg.h3_master"],billboard:"vertical",line_width:110,text:[{"text":"👑 Master dit","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.master run data modify entity @e[type=minecraft:text_display,tag=mg.h3_master,limit=1] text set from storage mg:hall t3x.master
summon minecraft:text_display -25.5 71.0 35.4 {Tags:["mg.hall","mg.h3_murder"],billboard:"vertical",line_width:110,text:[{"text":"🔪 Murder Mystery","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.murder run data modify entity @e[type=minecraft:text_display,tag=mg.h3_murder,limit=1] text set from storage mg:hall t3x.murder
summon minecraft:text_display -21.5 71.0 35.4 {Tags:["mg.hall","mg.h3_bman"],billboard:"vertical",line_width:110,text:[{"text":"💣 Bomberman","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.bman run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bman,limit=1] text set from storage mg:hall t3x.bman
summon minecraft:text_display -17.5 71.0 35.4 {Tags:["mg.hall","mg.h3_maze"],billboard:"vertical",line_width:110,text:[{"text":"🌀 Labyrinthe géant","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall t3x.maze run data modify entity @e[type=minecraft:text_display,tag=mg.h3_maze,limit=1] text set from storage mg:hall t3x.maze
data modify storage mg:hall v2 set value 1b
data modify storage mg:hall v3 set value 1b
data modify storage mg:hall v4 set value 1b
data modify storage mg:hall v5 set value 1b
data modify storage mg:hall v6 set value 1b
data modify storage mg:hall v7 set value 1b
data modify storage mg:hall v8 set value 1b
data modify storage mg:hall v9 set value 1b
data modify storage mg:hall v10 set value 1b
data modify storage mg:hall v11 set value 1b
data modify storage mg:hall v12 set value 1b
data modify storage mg:hall v13 set value 1b
data modify storage mg:hall v14 set value 1b
data modify storage mg:hall v15 set value 1b
