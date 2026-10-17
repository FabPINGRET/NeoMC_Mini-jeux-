# Allée des champions (Hall des scores v18, à ciel ouvert, sud-ouest de la place) : construction + top 3 (généré par tools/hall/gen_hall.py)
# Chunks pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus
execute store success score #hl mg.st unless block -58 300 22 minecraft:bedrock
execute if score #hl mg.st matches 1 store success score #hl mg.st unless block -14 300 28 minecraft:bedrock
execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0
execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t
scoreboard players set #hlr mg.st 0
kill @e[tag=mg.hall]
execute unless data storage mg:hall v15 run function mg:hall/clear_old

# terrain des versions précédentes rendu à la pelouse, puis l'allée et ses deux rangées de stands
fill -60 64 15 -6 84 36 minecraft:air
fill -61 73 14 -11 73 14 minecraft:air replace minecraft:dark_oak_slab
fill -61 73 37 -11 73 37 minecraft:air replace minecraft:dark_oak_slab
fill -61 73 14 -61 73 37 minecraft:air replace minecraft:dark_oak_slab
fill -11 73 14 -11 73 37 minecraft:air replace minecraft:dark_oak_slab
fill -60 62 15 -6 62 36 minecraft:dirt
fill -60 63 15 -6 63 36 minecraft:grass_block
fill -59 63 23 -6 63 27 minecraft:dirt_path
fill -13 63 19 -6 63 31 minecraft:polished_andesite
fill -5 64 15 -4 65 36 minecraft:air
fill -5 63 15 -4 63 36 minecraft:grass_block
fill -5 63 19 -4 63 31 minecraft:polished_andesite
fill -60 64 19 -12 64 19 minecraft:moss_block
fill -60 64 31 -12 64 31 minecraft:moss_block
fill -60 64 19 -60 64 31 minecraft:moss_block
fill -12 64 19 -12 64 31 minecraft:moss_block
fill -12 64 23 -12 64 27 minecraft:air
fill -60 64 23 -60 64 27 minecraft:air
fill -60 63 23 -60 63 27 minecraft:dirt_path
fill -63 63 23 -61 63 27 minecraft:dirt_path replace minecraft:grass_block
fill -63 64 23 -61 65 27 minecraft:air replace #minecraft:replaceable
setblock -60 65 19 minecraft:lantern
setblock -60 65 31 minecraft:lantern
setblock -54 65 19 minecraft:lantern
setblock -54 65 31 minecraft:lantern
setblock -48 65 19 minecraft:lantern
setblock -48 65 31 minecraft:lantern
setblock -42 65 19 minecraft:lantern
setblock -42 65 31 minecraft:lantern
setblock -36 65 19 minecraft:lantern
setblock -36 65 31 minecraft:lantern
setblock -30 65 19 minecraft:lantern
setblock -30 65 31 minecraft:lantern
setblock -24 65 19 minecraft:lantern
setblock -24 65 31 minecraft:lantern
setblock -18 65 19 minecraft:lantern
setblock -18 65 31 minecraft:lantern
setblock -12 65 19 minecraft:lantern
setblock -12 65 31 minecraft:lantern
fill -59 63 20 -58 63 22 minecraft:spruce_planks
fill -59 64 20 -58 66 20 minecraft:stripped_spruce_wood
setblock -59 64 22 minecraft:spruce_planks
setblock -58 64 22 minecraft:snow_block
fill -59 65 22 -59 66 22 minecraft:spruce_fence
fill -59 67 20 -58 67 22 minecraft:red_wool
setblock -58 66 21 minecraft:light[level=13]
fill -57 63 20 -56 63 22 minecraft:spruce_planks
fill -57 64 20 -56 66 20 minecraft:stripped_spruce_wood
setblock -57 64 22 minecraft:spruce_planks
setblock -56 64 22 minecraft:tnt
fill -57 65 22 -57 66 22 minecraft:spruce_fence
fill -57 67 20 -56 67 22 minecraft:white_wool
setblock -56 66 21 minecraft:light[level=13]
fill -55 63 20 -54 63 22 minecraft:spruce_planks
fill -55 64 20 -54 66 20 minecraft:stripped_spruce_wood
setblock -55 64 22 minecraft:spruce_planks
setblock -54 64 22 minecraft:chiseled_stone_bricks
fill -55 65 22 -55 66 22 minecraft:spruce_fence
fill -55 67 20 -54 67 22 minecraft:red_wool
setblock -54 66 21 minecraft:light[level=13]
fill -53 63 20 -52 63 22 minecraft:spruce_planks
fill -53 64 20 -52 66 20 minecraft:stripped_spruce_wood
setblock -53 64 22 minecraft:spruce_planks
setblock -52 64 22 minecraft:red_wool
fill -53 65 22 -53 66 22 minecraft:spruce_fence
fill -53 67 20 -52 67 22 minecraft:white_wool
setblock -52 66 21 minecraft:light[level=13]
fill -51 63 20 -50 63 22 minecraft:spruce_planks
fill -51 64 20 -50 66 20 minecraft:stripped_spruce_wood
setblock -51 64 22 minecraft:spruce_planks
setblock -50 64 22 minecraft:white_wool
fill -51 65 22 -51 66 22 minecraft:spruce_fence
fill -51 67 20 -50 67 22 minecraft:red_wool
setblock -50 66 21 minecraft:light[level=13]
fill -49 63 20 -48 63 22 minecraft:spruce_planks
fill -49 64 20 -48 66 20 minecraft:stripped_spruce_wood
setblock -49 64 22 minecraft:spruce_planks
setblock -48 64 22 minecraft:mossy_cobblestone
fill -49 65 22 -49 66 22 minecraft:spruce_fence
fill -49 67 20 -48 67 22 minecraft:white_wool
setblock -48 66 21 minecraft:light[level=13]
fill -47 63 20 -46 63 22 minecraft:spruce_planks
fill -47 64 20 -46 66 20 minecraft:stripped_spruce_wood
setblock -47 64 22 minecraft:spruce_planks
setblock -46 64 22 minecraft:hay_block
fill -47 65 22 -47 66 22 minecraft:spruce_fence
fill -47 67 20 -46 67 22 minecraft:red_wool
setblock -46 66 21 minecraft:light[level=13]
fill -45 63 20 -44 63 22 minecraft:spruce_planks
fill -45 64 20 -44 66 20 minecraft:stripped_spruce_wood
setblock -45 64 22 minecraft:spruce_planks
setblock -44 64 22 minecraft:slime_block
fill -45 65 22 -45 66 22 minecraft:spruce_fence
fill -45 67 20 -44 67 22 minecraft:white_wool
setblock -44 66 21 minecraft:light[level=13]
fill -43 63 20 -42 63 22 minecraft:spruce_planks
fill -43 64 20 -42 66 20 minecraft:stripped_spruce_wood
setblock -43 64 22 minecraft:spruce_planks
setblock -42 64 22 minecraft:blue_ice
fill -43 65 22 -43 66 22 minecraft:spruce_fence
fill -43 67 20 -42 67 22 minecraft:red_wool
setblock -42 66 21 minecraft:light[level=13]
fill -41 63 20 -40 63 22 minecraft:spruce_planks
fill -41 64 20 -40 66 20 minecraft:stripped_spruce_wood
setblock -41 64 22 minecraft:spruce_planks
setblock -40 64 22 minecraft:target
fill -41 65 22 -41 66 22 minecraft:spruce_fence
fill -41 67 20 -40 67 22 minecraft:white_wool
setblock -40 66 21 minecraft:light[level=13]
fill -39 63 20 -38 63 22 minecraft:spruce_planks
fill -39 64 20 -38 66 20 minecraft:stripped_spruce_wood
setblock -39 64 22 minecraft:spruce_planks
setblock -38 64 22 minecraft:red_concrete
fill -39 65 22 -39 66 22 minecraft:spruce_fence
fill -39 67 20 -38 67 22 minecraft:red_wool
setblock -38 66 21 minecraft:light[level=13]
fill -37 63 20 -36 63 22 minecraft:spruce_planks
fill -37 64 20 -36 66 20 minecraft:stripped_spruce_wood
setblock -37 64 22 minecraft:spruce_planks
setblock -36 64 22 minecraft:jukebox
fill -37 65 22 -37 66 22 minecraft:spruce_fence
fill -37 67 20 -36 67 22 minecraft:white_wool
setblock -36 66 21 minecraft:light[level=13]
fill -35 63 20 -34 63 22 minecraft:spruce_planks
fill -35 64 20 -34 66 20 minecraft:stripped_spruce_wood
setblock -35 64 22 minecraft:spruce_planks
setblock -34 64 22 minecraft:anvil
fill -35 65 22 -35 66 22 minecraft:spruce_fence
fill -35 67 20 -34 67 22 minecraft:red_wool
setblock -34 66 21 minecraft:light[level=13]
fill -33 63 20 -32 63 22 minecraft:spruce_planks
fill -33 64 20 -32 66 20 minecraft:stripped_spruce_wood
setblock -33 64 22 minecraft:spruce_planks
setblock -32 64 22 minecraft:red_terracotta
fill -33 65 22 -33 66 22 minecraft:spruce_fence
fill -33 67 20 -32 67 22 minecraft:white_wool
setblock -32 66 21 minecraft:light[level=13]
fill -31 63 20 -30 63 22 minecraft:spruce_planks
fill -31 64 20 -30 66 20 minecraft:stripped_spruce_wood
setblock -31 64 22 minecraft:spruce_planks
setblock -30 64 22 minecraft:target
fill -31 65 22 -31 66 22 minecraft:spruce_fence
fill -31 67 20 -30 67 22 minecraft:red_wool
setblock -30 66 21 minecraft:light[level=13]
fill -29 63 20 -28 63 22 minecraft:spruce_planks
fill -29 64 20 -28 66 20 minecraft:stripped_spruce_wood
setblock -29 64 22 minecraft:spruce_planks
setblock -28 64 22 minecraft:lime_concrete
fill -29 65 22 -29 66 22 minecraft:spruce_fence
fill -29 67 20 -28 67 22 minecraft:white_wool
setblock -28 66 21 minecraft:light[level=13]
fill -27 63 20 -26 63 22 minecraft:spruce_planks
fill -27 64 20 -26 66 20 minecraft:stripped_spruce_wood
setblock -27 64 22 minecraft:spruce_planks
setblock -26 64 22 minecraft:packed_ice
fill -27 65 22 -27 66 22 minecraft:spruce_fence
fill -27 67 20 -26 67 22 minecraft:red_wool
setblock -26 66 21 minecraft:light[level=13]
fill -25 63 20 -24 63 22 minecraft:spruce_planks
fill -25 64 20 -24 66 20 minecraft:stripped_spruce_wood
setblock -25 64 22 minecraft:spruce_planks
setblock -24 64 22 minecraft:crafting_table
fill -25 65 22 -25 66 22 minecraft:spruce_fence
fill -25 67 20 -24 67 22 minecraft:white_wool
setblock -24 66 21 minecraft:light[level=13]
fill -23 63 20 -22 63 22 minecraft:spruce_planks
fill -23 64 20 -22 66 20 minecraft:stripped_spruce_wood
setblock -23 64 22 minecraft:spruce_planks
setblock -22 64 22 minecraft:cake
fill -23 65 22 -23 66 22 minecraft:spruce_fence
fill -23 67 20 -22 67 22 minecraft:red_wool
setblock -22 66 21 minecraft:light[level=13]
fill -21 63 20 -20 63 22 minecraft:spruce_planks
fill -21 64 20 -20 66 20 minecraft:stripped_spruce_wood
setblock -21 64 22 minecraft:spruce_planks
setblock -20 64 22 minecraft:redstone_block
fill -21 65 22 -21 66 22 minecraft:spruce_fence
fill -21 67 20 -20 67 22 minecraft:white_wool
setblock -20 66 21 minecraft:light[level=13]
fill -19 63 20 -18 63 22 minecraft:spruce_planks
fill -19 64 20 -18 66 20 minecraft:stripped_spruce_wood
setblock -19 64 22 minecraft:spruce_planks
setblock -18 64 22 minecraft:end_stone_bricks
fill -19 65 22 -19 66 22 minecraft:spruce_fence
fill -19 67 20 -18 67 22 minecraft:red_wool
setblock -18 66 21 minecraft:light[level=13]
fill -17 63 20 -16 63 22 minecraft:spruce_planks
fill -17 64 20 -16 66 20 minecraft:stripped_spruce_wood
setblock -17 64 22 minecraft:spruce_planks
setblock -16 64 22 minecraft:purpur_block
fill -17 65 22 -17 66 22 minecraft:spruce_fence
fill -17 67 20 -16 67 22 minecraft:white_wool
setblock -16 66 21 minecraft:light[level=13]
fill -59 63 28 -58 63 30 minecraft:spruce_planks
fill -59 64 30 -58 66 30 minecraft:stripped_spruce_wood
setblock -59 64 28 minecraft:spruce_planks
setblock -58 64 28 minecraft:bookshelf
fill -59 65 28 -59 66 28 minecraft:spruce_fence
fill -59 67 30 -58 67 28 minecraft:red_wool
setblock -58 66 29 minecraft:light[level=13]
fill -57 63 28 -56 63 30 minecraft:spruce_planks
fill -57 64 30 -56 66 30 minecraft:stripped_spruce_wood
setblock -57 64 28 minecraft:spruce_planks
setblock -56 64 28 minecraft:sea_lantern
fill -57 65 28 -57 66 28 minecraft:spruce_fence
fill -57 67 30 -56 67 28 minecraft:white_wool
setblock -56 66 29 minecraft:light[level=13]
fill -55 63 28 -54 63 30 minecraft:spruce_planks
fill -55 64 30 -54 66 30 minecraft:stripped_spruce_wood
setblock -55 64 28 minecraft:spruce_planks
setblock -54 64 28 minecraft:gold_block
fill -55 65 28 -55 66 28 minecraft:spruce_fence
fill -55 67 30 -54 67 28 minecraft:red_wool
setblock -54 66 29 minecraft:light[level=13]
fill -53 63 28 -52 63 30 minecraft:spruce_planks
fill -53 64 30 -52 66 30 minecraft:stripped_spruce_wood
setblock -53 64 28 minecraft:spruce_planks
setblock -52 64 28 minecraft:quartz_block
fill -53 65 28 -53 66 28 minecraft:spruce_fence
fill -53 67 30 -52 67 28 minecraft:white_wool
setblock -52 66 29 minecraft:light[level=13]
fill -51 63 28 -50 63 30 minecraft:spruce_planks
fill -51 64 30 -50 66 30 minecraft:stripped_spruce_wood
setblock -51 64 28 minecraft:spruce_planks
setblock -50 64 28 minecraft:barrel
fill -51 65 28 -51 66 28 minecraft:spruce_fence
fill -51 67 30 -50 67 28 minecraft:red_wool
setblock -50 66 29 minecraft:light[level=13]
fill -49 63 28 -48 63 30 minecraft:spruce_planks
fill -49 64 30 -48 66 30 minecraft:stripped_spruce_wood
setblock -49 64 28 minecraft:spruce_planks
setblock -48 64 28 minecraft:blue_wool
fill -49 65 28 -49 66 28 minecraft:spruce_fence
fill -49 67 30 -48 67 28 minecraft:white_wool
setblock -48 66 29 minecraft:light[level=13]
fill -47 63 28 -46 63 30 minecraft:spruce_planks
fill -47 64 30 -46 66 30 minecraft:stripped_spruce_wood
setblock -47 64 28 minecraft:spruce_planks
setblock -46 64 28 minecraft:grass_block
fill -47 65 28 -47 66 28 minecraft:spruce_fence
fill -47 67 30 -46 67 28 minecraft:red_wool
setblock -46 66 29 minecraft:light[level=13]
fill -45 63 28 -44 63 30 minecraft:spruce_planks
fill -45 64 30 -44 66 30 minecraft:stripped_spruce_wood
setblock -45 64 28 minecraft:spruce_planks
setblock -44 64 28 minecraft:chest
fill -45 65 28 -45 66 28 minecraft:spruce_fence
fill -45 67 30 -44 67 28 minecraft:white_wool
setblock -44 66 29 minecraft:light[level=13]
fill -43 63 28 -42 63 30 minecraft:spruce_planks
fill -43 64 30 -42 66 30 minecraft:stripped_spruce_wood
setblock -43 64 28 minecraft:spruce_planks
setblock -42 64 28 minecraft:pumpkin
fill -43 65 28 -43 66 28 minecraft:spruce_fence
fill -43 67 30 -42 67 28 minecraft:red_wool
setblock -42 66 29 minecraft:light[level=13]
fill -41 63 28 -40 63 30 minecraft:spruce_planks
fill -41 64 30 -40 66 30 minecraft:stripped_spruce_wood
setblock -41 64 28 minecraft:spruce_planks
setblock -40 64 28 minecraft:mossy_stone_bricks
fill -41 65 28 -41 66 28 minecraft:spruce_fence
fill -41 67 30 -40 67 28 minecraft:white_wool
setblock -40 66 29 minecraft:light[level=13]
fill -39 63 28 -38 63 30 minecraft:spruce_planks
fill -39 64 30 -38 66 30 minecraft:stripped_spruce_wood
setblock -39 64 28 minecraft:spruce_planks
setblock -38 64 28 minecraft:green_concrete
fill -39 65 28 -39 66 28 minecraft:spruce_fence
fill -39 67 30 -38 67 28 minecraft:red_wool
setblock -38 66 29 minecraft:light[level=13]
fill -37 63 28 -36 63 30 minecraft:spruce_planks
fill -37 64 30 -36 66 30 minecraft:stripped_spruce_wood
setblock -37 64 28 minecraft:spruce_planks
setblock -36 64 28 minecraft:tnt
fill -37 65 28 -37 66 28 minecraft:spruce_fence
fill -37 67 30 -36 67 28 minecraft:white_wool
setblock -36 66 29 minecraft:light[level=13]
fill -35 63 28 -34 63 30 minecraft:spruce_planks
fill -35 64 30 -34 66 30 minecraft:stripped_spruce_wood
setblock -35 64 28 minecraft:spruce_planks
setblock -34 64 28 minecraft:moss_block
fill -35 65 28 -35 66 28 minecraft:spruce_fence
fill -35 67 30 -34 67 28 minecraft:red_wool
setblock -34 66 29 minecraft:light[level=13]
fill -33 63 28 -32 63 30 minecraft:spruce_planks
fill -33 64 30 -32 66 30 minecraft:stripped_spruce_wood
setblock -33 64 28 minecraft:spruce_planks
setblock -32 64 28 minecraft:white_concrete
fill -33 65 28 -33 66 28 minecraft:spruce_fence
fill -33 67 30 -32 67 28 minecraft:white_wool
setblock -32 66 29 minecraft:light[level=13]
fill -31 63 28 -30 63 30 minecraft:spruce_planks
fill -31 64 30 -30 66 30 minecraft:stripped_spruce_wood
setblock -31 64 28 minecraft:spruce_planks
setblock -30 64 28 minecraft:red_concrete
fill -31 65 28 -31 66 28 minecraft:spruce_fence
fill -31 67 30 -30 67 28 minecraft:red_wool
setblock -30 66 29 minecraft:light[level=13]
fill -29 63 28 -28 63 30 minecraft:spruce_planks
fill -29 64 30 -28 66 30 minecraft:stripped_spruce_wood
setblock -29 64 28 minecraft:spruce_planks
setblock -28 64 28 minecraft:blue_ice
fill -29 65 28 -29 66 28 minecraft:spruce_fence
fill -29 67 30 -28 67 28 minecraft:white_wool
setblock -28 66 29 minecraft:light[level=13]
fill -27 63 28 -26 63 30 minecraft:spruce_planks
fill -27 64 30 -26 66 30 minecraft:stripped_spruce_wood
setblock -27 64 28 minecraft:spruce_planks
setblock -26 64 28 minecraft:slime_block
fill -27 65 28 -27 66 28 minecraft:spruce_fence
fill -27 67 30 -26 67 28 minecraft:red_wool
setblock -26 66 29 minecraft:light[level=13]
fill -25 63 28 -24 63 30 minecraft:spruce_planks
fill -25 64 30 -24 66 30 minecraft:stripped_spruce_wood
setblock -25 64 28 minecraft:spruce_planks
setblock -24 64 28 minecraft:black_concrete
fill -25 65 28 -25 66 28 minecraft:spruce_fence
fill -25 67 30 -24 67 28 minecraft:white_wool
setblock -24 66 29 minecraft:light[level=13]
fill -23 63 28 -22 63 30 minecraft:spruce_planks
fill -23 64 30 -22 66 30 minecraft:stripped_spruce_wood
setblock -23 64 28 minecraft:spruce_planks
setblock -22 64 28 minecraft:gold_block
fill -23 65 28 -23 66 28 minecraft:spruce_fence
fill -23 67 30 -22 67 28 minecraft:red_wool
setblock -22 66 29 minecraft:light[level=13]
fill -21 63 28 -20 63 30 minecraft:spruce_planks
fill -21 64 30 -20 66 30 minecraft:stripped_spruce_wood
setblock -21 64 28 minecraft:spruce_planks
setblock -20 64 28 minecraft:redstone_block
fill -21 65 28 -21 66 28 minecraft:spruce_fence
fill -21 67 30 -20 67 28 minecraft:white_wool
setblock -20 66 29 minecraft:light[level=13]
fill -19 63 28 -18 63 30 minecraft:spruce_planks
fill -19 64 30 -18 66 30 minecraft:stripped_spruce_wood
setblock -19 64 28 minecraft:spruce_planks
setblock -18 64 28 minecraft:stone_bricks
fill -19 65 28 -19 66 28 minecraft:spruce_fence
fill -19 67 30 -18 67 28 minecraft:red_wool
setblock -18 66 29 minecraft:light[level=13]
fill -17 63 28 -16 63 30 minecraft:spruce_planks
fill -17 64 30 -16 66 30 minecraft:stripped_spruce_wood
setblock -17 64 28 minecraft:spruce_planks
setblock -16 64 28 minecraft:moss_block
fill -17 65 28 -17 66 28 minecraft:spruce_fence
fill -17 67 30 -16 67 28 minecraft:white_wool
setblock -16 66 29 minecraft:light[level=13]
setblock -15 64 22 minecraft:spruce_planks
fill -15 65 22 -15 66 22 minecraft:spruce_fence
setblock -15 64 28 minecraft:spruce_planks
fill -15 65 28 -15 66 28 minecraft:spruce_fence

# Décor : arches d'entrée (est) et de sortie (ouest)
fill -12 64 22 -12 68 22 minecraft:stripped_spruce_log
fill -12 64 28 -12 68 28 minecraft:stripped_spruce_log
fill -12 69 22 -12 69 28 minecraft:spruce_planks
fill -12 70 22 -12 70 28 minecraft:spruce_slab[type=bottom]
setblock -12 70 25 minecraft:spruce_planks
setblock -12 71 25 minecraft:lantern
setblock -12 68 24 minecraft:lantern[hanging=true]
setblock -12 68 26 minecraft:lantern[hanging=true]
fill -60 64 22 -60 68 22 minecraft:stripped_spruce_log
fill -60 64 28 -60 68 28 minecraft:stripped_spruce_log
fill -60 69 22 -60 69 28 minecraft:spruce_planks
fill -60 70 22 -60 70 28 minecraft:spruce_slab[type=bottom]
setblock -60 70 25 minecraft:spruce_planks
setblock -60 71 25 minecraft:lantern
setblock -60 68 24 minecraft:lantern[hanging=true]
setblock -60 68 26 minecraft:lantern[hanging=true]
# Décor : arbres de part et d'autre (chênes et bouleaux)
fill -58 67 14 -54 68 18 minecraft:oak_leaves[persistent=true]
fill -58 67 14 -58 68 14 minecraft:air
fill -54 67 14 -54 68 14 minecraft:air
fill -58 67 18 -58 68 18 minecraft:air
fill -54 67 18 -54 68 18 minecraft:air
fill -57 69 16 -55 69 16 minecraft:oak_leaves[persistent=true]
fill -56 69 15 -56 69 17 minecraft:oak_leaves[persistent=true]
setblock -56 70 16 minecraft:oak_leaves[persistent=true]
fill -56 64 16 -56 69 16 minecraft:oak_log
fill -52 67 32 -48 68 36 minecraft:birch_leaves[persistent=true]
fill -52 67 32 -52 68 32 minecraft:air
fill -48 67 32 -48 68 32 minecraft:air
fill -52 67 36 -52 68 36 minecraft:air
fill -48 67 36 -48 68 36 minecraft:air
fill -51 69 34 -49 69 34 minecraft:birch_leaves[persistent=true]
fill -50 69 33 -50 69 35 minecraft:birch_leaves[persistent=true]
setblock -50 70 34 minecraft:birch_leaves[persistent=true]
fill -50 64 34 -50 69 34 minecraft:birch_log
fill -46 67 14 -42 68 18 minecraft:birch_leaves[persistent=true]
fill -46 67 14 -46 68 14 minecraft:air
fill -42 67 14 -42 68 14 minecraft:air
fill -46 67 18 -46 68 18 minecraft:air
fill -42 67 18 -42 68 18 minecraft:air
fill -45 69 16 -43 69 16 minecraft:birch_leaves[persistent=true]
fill -44 69 15 -44 69 17 minecraft:birch_leaves[persistent=true]
setblock -44 70 16 minecraft:birch_leaves[persistent=true]
fill -44 64 16 -44 69 16 minecraft:birch_log
fill -40 67 32 -36 68 36 minecraft:oak_leaves[persistent=true]
fill -40 67 32 -40 68 32 minecraft:air
fill -36 67 32 -36 68 32 minecraft:air
fill -40 67 36 -40 68 36 minecraft:air
fill -36 67 36 -36 68 36 minecraft:air
fill -39 69 34 -37 69 34 minecraft:oak_leaves[persistent=true]
fill -38 69 33 -38 69 35 minecraft:oak_leaves[persistent=true]
setblock -38 70 34 minecraft:oak_leaves[persistent=true]
fill -38 64 34 -38 69 34 minecraft:oak_log
fill -34 67 14 -30 68 18 minecraft:oak_leaves[persistent=true]
fill -34 67 14 -34 68 14 minecraft:air
fill -30 67 14 -30 68 14 minecraft:air
fill -34 67 18 -34 68 18 minecraft:air
fill -30 67 18 -30 68 18 minecraft:air
fill -33 69 16 -31 69 16 minecraft:oak_leaves[persistent=true]
fill -32 69 15 -32 69 17 minecraft:oak_leaves[persistent=true]
setblock -32 70 16 minecraft:oak_leaves[persistent=true]
fill -32 64 16 -32 69 16 minecraft:oak_log
fill -28 67 32 -24 68 36 minecraft:birch_leaves[persistent=true]
fill -28 67 32 -28 68 32 minecraft:air
fill -24 67 32 -24 68 32 minecraft:air
fill -28 67 36 -28 68 36 minecraft:air
fill -24 67 36 -24 68 36 minecraft:air
fill -27 69 34 -25 69 34 minecraft:birch_leaves[persistent=true]
fill -26 69 33 -26 69 35 minecraft:birch_leaves[persistent=true]
setblock -26 70 34 minecraft:birch_leaves[persistent=true]
fill -26 64 34 -26 69 34 minecraft:birch_log
fill -22 67 14 -18 68 18 minecraft:birch_leaves[persistent=true]
fill -22 67 14 -22 68 14 minecraft:air
fill -18 67 14 -18 68 14 minecraft:air
fill -22 67 18 -22 68 18 minecraft:air
fill -18 67 18 -18 68 18 minecraft:air
fill -21 69 16 -19 69 16 minecraft:birch_leaves[persistent=true]
fill -20 69 15 -20 69 17 minecraft:birch_leaves[persistent=true]
setblock -20 70 16 minecraft:birch_leaves[persistent=true]
fill -20 64 16 -20 69 16 minecraft:birch_log
fill -16 67 32 -12 68 36 minecraft:oak_leaves[persistent=true]
fill -16 67 32 -16 68 32 minecraft:air
fill -12 67 32 -12 68 32 minecraft:air
fill -16 67 36 -16 68 36 minecraft:air
fill -12 67 36 -12 68 36 minecraft:air
fill -15 69 34 -13 69 34 minecraft:oak_leaves[persistent=true]
fill -14 69 33 -14 69 35 minecraft:oak_leaves[persistent=true]
setblock -14 70 34 minecraft:oak_leaves[persistent=true]
fill -14 64 34 -14 69 34 minecraft:oak_log
# Décor : massifs fleuris le long de la bordure, herbes et buissons
setblock -60 64 18 minecraft:dandelion
setblock -59 64 18 minecraft:oxeye_daisy
setblock -58 64 18 minecraft:lily_of_the_valley
setblock -57 64 18 minecraft:azalea
setblock -56 64 18 minecraft:allium
setblock -55 64 18 minecraft:lily_of_the_valley
setblock -54 64 18 minecraft:red_tulip
setblock -53 64 18 minecraft:lily_of_the_valley
setblock -52 64 18 minecraft:white_tulip
setblock -51 64 18 minecraft:flowering_azalea
setblock -50 64 18 minecraft:allium
setblock -49 64 18 minecraft:poppy
setblock -48 64 18 minecraft:dandelion
setblock -47 64 18 minecraft:dandelion
setblock -46 64 18 minecraft:azure_bluet
setblock -45 64 18 minecraft:azalea
setblock -44 64 18 minecraft:white_tulip
setblock -43 64 18 minecraft:poppy
setblock -42 64 18 minecraft:white_tulip
setblock -41 64 18 minecraft:oxeye_daisy
setblock -40 64 18 minecraft:allium
setblock -39 64 18 minecraft:flowering_azalea
setblock -38 64 18 minecraft:azure_bluet
setblock -37 64 18 minecraft:oxeye_daisy
setblock -36 64 18 minecraft:oxeye_daisy
setblock -35 64 18 minecraft:red_tulip
setblock -34 64 18 minecraft:lily_of_the_valley
setblock -33 64 18 minecraft:azalea
setblock -32 64 18 minecraft:oxeye_daisy
setblock -31 64 18 minecraft:dandelion
setblock -30 64 18 minecraft:lily_of_the_valley
setblock -29 64 18 minecraft:lily_of_the_valley
setblock -28 64 18 minecraft:azure_bluet
setblock -27 64 18 minecraft:flowering_azalea
setblock -26 64 18 minecraft:white_tulip
setblock -25 64 18 minecraft:cornflower
setblock -24 64 18 minecraft:azure_bluet
setblock -23 64 18 minecraft:poppy
setblock -22 64 18 minecraft:oxeye_daisy
setblock -21 64 18 minecraft:flowering_azalea
setblock -20 64 18 minecraft:white_tulip
setblock -19 64 18 minecraft:red_tulip
setblock -18 64 18 minecraft:dandelion
setblock -17 64 18 minecraft:red_tulip
setblock -16 64 18 minecraft:lily_of_the_valley
setblock -15 64 18 minecraft:flowering_azalea
setblock -14 64 18 minecraft:dandelion
setblock -13 64 18 minecraft:red_tulip
setblock -12 64 18 minecraft:lily_of_the_valley
setblock -60 64 32 minecraft:white_tulip
setblock -59 64 32 minecraft:red_tulip
setblock -58 64 32 minecraft:lily_of_the_valley
setblock -57 64 32 minecraft:flowering_azalea
setblock -56 64 32 minecraft:red_tulip
setblock -55 64 32 minecraft:white_tulip
setblock -54 64 32 minecraft:lily_of_the_valley
setblock -53 64 32 minecraft:lily_of_the_valley
setblock -52 64 32 minecraft:poppy
setblock -51 64 32 minecraft:azalea
setblock -50 64 32 minecraft:cornflower
setblock -49 64 32 minecraft:poppy
setblock -48 64 32 minecraft:lily_of_the_valley
setblock -47 64 32 minecraft:dandelion
setblock -46 64 32 minecraft:red_tulip
setblock -45 64 32 minecraft:flowering_azalea
setblock -44 64 32 minecraft:cornflower
setblock -43 64 32 minecraft:white_tulip
setblock -42 64 32 minecraft:allium
setblock -41 64 32 minecraft:dandelion
setblock -40 64 32 minecraft:white_tulip
setblock -39 64 32 minecraft:flowering_azalea
setblock -38 64 32 minecraft:lily_of_the_valley
setblock -37 64 32 minecraft:azure_bluet
setblock -36 64 32 minecraft:lily_of_the_valley
setblock -35 64 32 minecraft:red_tulip
setblock -34 64 32 minecraft:azure_bluet
setblock -33 64 32 minecraft:flowering_azalea
setblock -32 64 32 minecraft:red_tulip
setblock -31 64 32 minecraft:red_tulip
setblock -30 64 32 minecraft:allium
setblock -29 64 32 minecraft:azure_bluet
setblock -28 64 32 minecraft:azure_bluet
setblock -27 64 32 minecraft:azalea
setblock -26 64 32 minecraft:poppy
setblock -25 64 32 minecraft:cornflower
setblock -24 64 32 minecraft:white_tulip
setblock -23 64 32 minecraft:lily_of_the_valley
setblock -22 64 32 minecraft:white_tulip
setblock -21 64 32 minecraft:flowering_azalea
setblock -20 64 32 minecraft:allium
setblock -19 64 32 minecraft:azure_bluet
setblock -18 64 32 minecraft:white_tulip
setblock -17 64 32 minecraft:white_tulip
setblock -16 64 32 minecraft:lily_of_the_valley
setblock -15 64 32 minecraft:flowering_azalea
setblock -14 64 32 minecraft:red_tulip
setblock -13 64 32 minecraft:lily_of_the_valley
setblock -12 64 32 minecraft:poppy
execute if block -60 64 15 minecraft:air if block -60 63 15 minecraft:grass_block run setblock -60 64 15 minecraft:cornflower
execute if block -46 64 15 minecraft:air if block -46 63 15 minecraft:grass_block run setblock -46 64 15 minecraft:short_grass
execute if block -45 64 15 minecraft:air if block -45 63 15 minecraft:grass_block run setblock -45 64 15 minecraft:poppy
execute if block -42 64 15 minecraft:air if block -42 63 15 minecraft:grass_block run setblock -42 64 15 minecraft:short_grass
execute if block -35 64 15 minecraft:air if block -35 63 15 minecraft:grass_block run setblock -35 64 15 minecraft:fern
execute if block -26 64 15 minecraft:air if block -26 63 15 minecraft:grass_block run setblock -26 64 15 minecraft:dandelion
execute if block -23 64 15 minecraft:air if block -23 63 15 minecraft:grass_block run setblock -23 64 15 minecraft:cornflower
execute if block -22 64 15 minecraft:air if block -22 63 15 minecraft:grass_block run setblock -22 64 15 minecraft:short_grass
execute if block -14 64 15 minecraft:air if block -14 63 15 minecraft:grass_block run setblock -14 64 15 minecraft:short_grass
execute if block -12 64 15 minecraft:air if block -12 63 15 minecraft:grass_block run setblock -12 64 15 minecraft:fern
execute if block -8 64 15 minecraft:air if block -8 63 15 minecraft:grass_block run setblock -8 64 15 minecraft:poppy
execute if block -62 64 16 minecraft:air if block -62 63 16 minecraft:grass_block run setblock -62 64 16 minecraft:poppy
execute if block -59 64 16 minecraft:air if block -59 63 16 minecraft:grass_block run setblock -59 64 16 minecraft:dandelion
execute if block -52 64 16 minecraft:air if block -52 63 16 minecraft:grass_block run setblock -52 64 16 minecraft:cornflower
execute if block -50 64 16 minecraft:air if block -50 63 16 minecraft:grass_block run setblock -50 64 16 minecraft:dandelion
execute if block -48 64 16 minecraft:air if block -48 63 16 minecraft:grass_block run setblock -48 64 16 minecraft:cornflower
execute if block -44 64 16 minecraft:air if block -44 63 16 minecraft:grass_block run setblock -44 64 16 minecraft:dandelion
execute if block -40 64 16 minecraft:air if block -40 63 16 minecraft:grass_block run setblock -40 64 16 minecraft:cornflower
execute if block -35 64 16 minecraft:air if block -35 63 16 minecraft:grass_block run setblock -35 64 16 minecraft:fern
execute if block -33 64 16 minecraft:air if block -33 63 16 minecraft:grass_block run setblock -33 64 16 minecraft:poppy
execute if block -26 64 16 minecraft:air if block -26 63 16 minecraft:grass_block run setblock -26 64 16 minecraft:dandelion
execute if block -12 64 16 minecraft:air if block -12 63 16 minecraft:grass_block run setblock -12 64 16 minecraft:dandelion
execute if block -59 64 17 minecraft:air if block -59 63 17 minecraft:grass_block run setblock -59 64 17 minecraft:fern
execute if block -58 64 17 minecraft:air if block -58 63 17 minecraft:grass_block run setblock -58 64 17 minecraft:poppy
execute if block -57 64 17 minecraft:air if block -57 63 17 minecraft:grass_block run setblock -57 64 17 minecraft:cornflower
execute if block -56 64 17 minecraft:air if block -56 63 17 minecraft:grass_block run setblock -56 64 17 minecraft:fern
execute if block -46 64 17 minecraft:air if block -46 63 17 minecraft:grass_block run setblock -46 64 17 minecraft:poppy
execute if block -41 64 17 minecraft:air if block -41 63 17 minecraft:grass_block run setblock -41 64 17 minecraft:short_grass
execute if block -40 64 17 minecraft:air if block -40 63 17 minecraft:grass_block run setblock -40 64 17 minecraft:short_grass
execute if block -39 64 17 minecraft:air if block -39 63 17 minecraft:grass_block run setblock -39 64 17 minecraft:dandelion
execute if block -16 64 17 minecraft:air if block -16 63 17 minecraft:grass_block run setblock -16 64 17 minecraft:cornflower
execute if block -8 64 17 minecraft:air if block -8 63 17 minecraft:grass_block run setblock -8 64 17 minecraft:fern
execute if block -6 64 17 minecraft:air if block -6 63 17 minecraft:grass_block run setblock -6 64 17 minecraft:short_grass
execute if block -63 64 33 minecraft:air if block -63 63 33 minecraft:grass_block run setblock -63 64 33 minecraft:short_grass
execute if block -62 64 33 minecraft:air if block -62 63 33 minecraft:grass_block run setblock -62 64 33 minecraft:short_grass
execute if block -56 64 33 minecraft:air if block -56 63 33 minecraft:grass_block run setblock -56 64 33 minecraft:poppy
execute if block -51 64 33 minecraft:air if block -51 63 33 minecraft:grass_block run setblock -51 64 33 minecraft:dandelion
execute if block -50 64 33 minecraft:air if block -50 63 33 minecraft:grass_block run setblock -50 64 33 minecraft:cornflower
execute if block -45 64 33 minecraft:air if block -45 63 33 minecraft:grass_block run setblock -45 64 33 minecraft:short_grass
execute if block -44 64 33 minecraft:air if block -44 63 33 minecraft:grass_block run setblock -44 64 33 minecraft:dandelion
execute if block -28 64 33 minecraft:air if block -28 63 33 minecraft:grass_block run setblock -28 64 33 minecraft:short_grass
execute if block -6 64 33 minecraft:air if block -6 63 33 minecraft:grass_block run setblock -6 64 33 minecraft:short_grass
execute if block -57 64 34 minecraft:air if block -57 63 34 minecraft:grass_block run setblock -57 64 34 minecraft:fern
execute if block -53 64 34 minecraft:air if block -53 63 34 minecraft:grass_block run setblock -53 64 34 minecraft:short_grass
execute if block -48 64 34 minecraft:air if block -48 63 34 minecraft:grass_block run setblock -48 64 34 minecraft:poppy
execute if block -43 64 34 minecraft:air if block -43 63 34 minecraft:grass_block run setblock -43 64 34 minecraft:dandelion
execute if block -42 64 34 minecraft:air if block -42 63 34 minecraft:grass_block run setblock -42 64 34 minecraft:short_grass
execute if block -38 64 34 minecraft:air if block -38 63 34 minecraft:grass_block run setblock -38 64 34 minecraft:dandelion
execute if block -32 64 34 minecraft:air if block -32 63 34 minecraft:grass_block run setblock -32 64 34 minecraft:poppy
execute if block -29 64 34 minecraft:air if block -29 63 34 minecraft:grass_block run setblock -29 64 34 minecraft:dandelion
execute if block -20 64 34 minecraft:air if block -20 63 34 minecraft:grass_block run setblock -20 64 34 minecraft:fern
execute if block -18 64 34 minecraft:air if block -18 63 34 minecraft:grass_block run setblock -18 64 34 minecraft:short_grass
execute if block -14 64 34 minecraft:air if block -14 63 34 minecraft:grass_block run setblock -14 64 34 minecraft:fern
execute if block -13 64 34 minecraft:air if block -13 63 34 minecraft:grass_block run setblock -13 64 34 minecraft:fern
execute if block -11 64 34 minecraft:air if block -11 63 34 minecraft:grass_block run setblock -11 64 34 minecraft:dandelion
execute if block -9 64 34 minecraft:air if block -9 63 34 minecraft:grass_block run setblock -9 64 34 minecraft:fern
execute if block -58 64 35 minecraft:air if block -58 63 35 minecraft:grass_block run setblock -58 64 35 minecraft:dandelion
execute if block -52 64 35 minecraft:air if block -52 63 35 minecraft:grass_block run setblock -52 64 35 minecraft:short_grass
execute if block -47 64 35 minecraft:air if block -47 63 35 minecraft:grass_block run setblock -47 64 35 minecraft:poppy
execute if block -40 64 35 minecraft:air if block -40 63 35 minecraft:grass_block run setblock -40 64 35 minecraft:poppy
execute if block -32 64 35 minecraft:air if block -32 63 35 minecraft:grass_block run setblock -32 64 35 minecraft:cornflower
execute if block -27 64 35 minecraft:air if block -27 63 35 minecraft:grass_block run setblock -27 64 35 minecraft:fern
execute if block -24 64 35 minecraft:air if block -24 63 35 minecraft:grass_block run setblock -24 64 35 minecraft:cornflower
execute if block -21 64 35 minecraft:air if block -21 63 35 minecraft:grass_block run setblock -21 64 35 minecraft:short_grass
execute if block -13 64 35 minecraft:air if block -13 63 35 minecraft:grass_block run setblock -13 64 35 minecraft:poppy
execute if block -60 64 36 minecraft:air if block -60 63 36 minecraft:grass_block run setblock -60 64 36 minecraft:dandelion
execute if block -58 64 36 minecraft:air if block -58 63 36 minecraft:grass_block run setblock -58 64 36 minecraft:dandelion
execute if block -51 64 36 minecraft:air if block -51 63 36 minecraft:grass_block run setblock -51 64 36 minecraft:short_grass
execute if block -37 64 36 minecraft:air if block -37 63 36 minecraft:grass_block run setblock -37 64 36 minecraft:short_grass
execute if block -32 64 36 minecraft:air if block -32 63 36 minecraft:grass_block run setblock -32 64 36 minecraft:poppy
execute if block -28 64 36 minecraft:air if block -28 63 36 minecraft:grass_block run setblock -28 64 36 minecraft:fern
execute if block -26 64 36 minecraft:air if block -26 63 36 minecraft:grass_block run setblock -26 64 36 minecraft:dandelion
execute if block -14 64 36 minecraft:air if block -14 63 36 minecraft:grass_block run setblock -14 64 36 minecraft:poppy
execute if block -13 64 36 minecraft:air if block -13 63 36 minecraft:grass_block run setblock -13 64 36 minecraft:poppy
# Décor : réverbères et bancs de la place d'entrée
fill -11 64 19 -11 66 19 minecraft:dark_oak_fence
setblock -11 67 19 minecraft:lantern
fill -6 64 19 -6 66 19 minecraft:dark_oak_fence
setblock -6 67 19 minecraft:lantern
fill -11 64 31 -11 66 31 minecraft:dark_oak_fence
setblock -11 67 31 minecraft:lantern
fill -6 64 31 -6 66 31 minecraft:dark_oak_fence
setblock -6 67 31 minecraft:lantern
fill -10 64 19 -7 64 19 minecraft:spruce_stairs[facing=north]
fill -10 64 31 -7 64 31 minecraft:spruce_stairs[facing=south]

# Place d'entrée (est) : piédestaux d'honneur
setblock -9 64 20 minecraft:emerald_block
setblock -9 64 25 minecraft:gold_block
setblock -9 64 30 minecraft:lapis_block

# Tampon de résolution des noms (invisible)
summon minecraft:item_display -8.5 64.5 25.5 {Tags:["mg.hall","mg.hallbuf"],item:{id:"minecraft:paper"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.001f,0.001f,0.001f]}}
summon minecraft:text_display -8.5 70.8 25.5 {Tags:["mg.hall"],billboard:"vertical",background:0,text:[{"text":"🏆 Allée des champions","color":"gold","bold":true},{"text":"\n🥇 🥈 🥉 le top 3 de chaque jeu, de chaque côté de l'allée","color":"gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.6f,1.6f,1.6f]}}

# Piédestaux : objet qui tourne + plaque
summon minecraft:item_display -8.5 65.8 20.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:clock"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -8.5 65.8 25.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:totem_of_undying"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -8.5 65.8 30.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}

# Plaques d'honneur : texte par défaut, puis meneur enregistré s'il existe
summon minecraft:text_display -8.5 66.7 20.5 {Tags:["mg.hall","mg.h_stp"],billboard:"vertical",line_width:115,text:[{"text":"▶ Le plus assidu","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.stp run data modify entity @e[type=minecraft:text_display,tag=mg.h_stp,limit=1] text set from storage mg:hall e.stp
summon minecraft:text_display -8.5 66.7 25.5 {Tags:["mg.hall","mg.h_wins"],billboard:"vertical",line_width:115,text:[{"text":"👑 Champion des mini-jeux","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.wins run data modify entity @e[type=minecraft:text_display,tag=mg.h_wins,limit=1] text set from storage mg:hall e.wins
summon minecraft:text_display -8.5 66.7 30.5 {Tags:["mg.hall","mg.h_ely"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record petit parcours d'élytra","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely,limit=1] text set from storage mg:hall e.ely
summon minecraft:text_display -8.5 68.1 30.5 {Tags:["mg.hall","mg.h_ely2"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record grand parcours d'élytra","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely2 run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely2,limit=1] text set from storage mg:hall e.ely2
summon minecraft:text_display -8.5 69.5 30.5 {Tags:["mg.hall","mg.h_elyg"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record Élytra : course","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.elyg run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyg,limit=1] text set from storage mg:hall e.elyg
summon minecraft:text_display -8.5 68.6 25.5 {Tags:["mg.hall","mg.h_gen"],billboard:"vertical",line_width:200,text:[{"text":"🏅 Meilleur niveau général","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.1f,1.1f,1.1f]}}
execute if data storage mg:hall e.gen run data modify entity @e[type=minecraft:text_display,tag=mg.h_gen,limit=1] text set from storage mg:hall e.gen

# Étals : top 3 de chaque jeu sur fond sombre (texte par défaut, puis top 3 enregistré), objet du jeu sur le comptoir
summon minecraft:text_display -58.0 65.35 21.5 {Tags:["mg.hall","mg.h3_spleef"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"❄ Spleef","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -57.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:diamond_shovel"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.spleef run data modify entity @e[type=minecraft:text_display,tag=mg.h3_spleef,limit=1] text set from storage mg:hall t3x.spleef
summon minecraft:text_display -56.0 65.35 21.5 {Tags:["mg.hall","mg.h3_tntrun"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"✷ TNT Run","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -55.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:tnt"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.tntrun run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tntrun,limit=1] text set from storage mg:hall t3x.tntrun
summon minecraft:text_display -54.0 65.35 21.5 {Tags:["mg.hall","mg.h3_pvp"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"⚔ PvP","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -53.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:iron_sword"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.pvp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_pvp,limit=1] text set from storage mg:hall t3x.pvp
summon minecraft:text_display -52.0 65.35 21.5 {Tags:["mg.hall","mg.h3_bedwars"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🛏 Bedwars","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -51.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:red_bed"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.bedwars run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bedwars,limit=1] text set from storage mg:hall t3x.bedwars
summon minecraft:text_display -50.0 65.35 21.5 {Tags:["mg.hall","mg.h3_sheepwar"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🐑 Sheep War","color":"white","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -49.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:shears"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.sheepwar run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sheepwar,limit=1] text set from storage mg:hall t3x.sheepwar
summon minecraft:text_display -48.0 65.35 21.5 {Tags:["mg.hall","mg.h3_mobarena"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -47.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:zombie_head"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.mobarena run data modify entity @e[type=minecraft:text_display,tag=mg.h3_mobarena,limit=1] text set from storage mg:hall t3x.mobarena
summon minecraft:text_display -46.0 65.35 21.5 {Tags:["mg.hall","mg.h3_splegg"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"❍ Splegg","color":"yellow","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -45.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:egg"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.splegg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_splegg,limit=1] text set from storage mg:hall t3x.splegg
summon minecraft:text_display -44.0 65.35 21.5 {Tags:["mg.hall","mg.h3_sumo"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"✊ Sumo","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -43.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:slime_ball"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.sumo run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sumo,limit=1] text set from storage mg:hall t3x.sumo
summon minecraft:text_display -42.0 65.35 21.5 {Tags:["mg.hall","mg.h3_dropper"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"⬇ Dropper","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -41.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:feather"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.dropper run data modify entity @e[type=minecraft:text_display,tag=mg.h3_dropper,limit=1] text set from storage mg:hall t3x.dropper
summon minecraft:text_display -40.0 65.35 21.5 {Tags:["mg.hall","mg.h3_oitc"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -39.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:bow"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.oitc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_oitc,limit=1] text set from storage mg:hall t3x.oitc
summon minecraft:text_display -38.0 65.35 21.5 {Tags:["mg.hall","mg.h3_tnttag"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"✹ TNT Tag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -37.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:tnt"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.tnttag run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tnttag,limit=1] text set from storage mg:hall t3x.tnttag
summon minecraft:text_display -36.0 65.35 21.5 {Tags:["mg.hall","mg.h3_blockparty"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -35.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:music_disc_cat"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.blockparty run data modify entity @e[type=minecraft:text_display,tag=mg.h3_blockparty,limit=1] text set from storage mg:hall t3x.blockparty
summon minecraft:text_display -34.0 65.35 21.5 {Tags:["mg.hall","mg.h3_anvil"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"⚓ Pluie d'enclumes","color":"gray","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -33.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:anvil"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.anvil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_anvil,limit=1] text set from storage mg:hall t3x.anvil
summon minecraft:text_display -32.0 65.35 21.5 {Tags:["mg.hall","mg.h3_turf"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -31.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:bow"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.turf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_turf,limit=1] text set from storage mg:hall t3x.turf
summon minecraft:text_display -30.0 65.35 21.5 {Tags:["mg.hall","mg.h3_quake"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -29.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:diamond_hoe"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.quake run data modify entity @e[type=minecraft:text_display,tag=mg.h3_quake,limit=1] text set from storage mg:hall t3x.quake
summon minecraft:text_display -28.0 65.35 21.5 {Tags:["mg.hall","mg.h3_paintball"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"▓ Paintball","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -27.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:snowball"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.paintball run data modify entity @e[type=minecraft:text_display,tag=mg.h3_paintball,limit=1] text set from storage mg:hall t3x.paintball
summon minecraft:text_display -26.0 65.35 21.5 {Tags:["mg.hall","mg.h3_icerace"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"⛵ Course de bateaux","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -25.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:oak_boat"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.icerace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_icerace,limit=1] text set from storage mg:hall t3x.icerace
summon minecraft:text_display -24.0 65.35 21.5 {Tags:["mg.hall","mg.h3_bb"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"✎ Build Battle","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -23.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:brick"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.bb run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bb,limit=1] text set from storage mg:hall t3x.bb
summon minecraft:text_display -22.0 65.35 21.5 {Tags:["mg.hall","mg.h3_party"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"★ Mini Party","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -21.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:cake"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.party run data modify entity @e[type=minecraft:text_display,tag=mg.h3_party,limit=1] text set from storage mg:hall t3x.party
summon minecraft:text_display -20.0 65.35 21.5 {Tags:["mg.hall","mg.h3_kart"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🏎 Kart","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -19.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:minecart"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.kart run data modify entity @e[type=minecraft:text_display,tag=mg.h3_kart,limit=1] text set from storage mg:hall t3x.kart
summon minecraft:text_display -18.0 65.35 21.5 {Tags:["mg.hall","mg.h3_elyrace"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🪽 Course d'élytres","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -17.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.elyrace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elyrace,limit=1] text set from storage mg:hall t3x.elyrace
summon minecraft:text_display -16.0 65.35 21.5 {Tags:["mg.hall","mg.h3_elytra"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🪽 Élytra (3 modes)","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -15.5 65.45 22.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:firework_rocket"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.elytra run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elytra,limit=1] text set from storage mg:hall t3x.elytra
summon minecraft:text_display -58.0 65.35 29.5 {Tags:["mg.hall","mg.h3_telephone"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"📞 Téléphone","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -57.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:writable_book"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.telephone run data modify entity @e[type=minecraft:text_display,tag=mg.h3_telephone,limit=1] text set from storage mg:hall t3x.telephone
summon minecraft:text_display -56.0 65.35 29.5 {Tags:["mg.hall","mg.h3_tron"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"⚡ Tron","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -55.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:blaze_rod"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.tron run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tron,limit=1] text set from storage mg:hall t3x.tron
summon minecraft:text_display -54.0 65.35 29.5 {Tags:["mg.hall","mg.h3_koth"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"👑 King of the Hill","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -53.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:golden_helmet"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.koth run data modify entity @e[type=minecraft:text_display,tag=mg.h3_koth,limit=1] text set from storage mg:hall t3x.koth
summon minecraft:text_display -52.0 65.35 29.5 {Tags:["mg.hall","mg.h3_tower"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🏰 The Towers","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -51.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:golden_apple"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.tower run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tower,limit=1] text set from storage mg:hall t3x.tower
summon minecraft:text_display -50.0 65.35 29.5 {Tags:["mg.hall","mg.h3_convoy"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🚚 Convoi","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -49.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:chest_minecart"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.convoy run data modify entity @e[type=minecraft:text_display,tag=mg.h3_convoy,limit=1] text set from storage mg:hall t3x.convoy
summon minecraft:text_display -48.0 65.35 29.5 {Tags:["mg.hall","mg.h3_ctf"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🚩 Capture the Flag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -47.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:red_banner"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.ctf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_ctf,limit=1] text set from storage mg:hall t3x.ctf
summon minecraft:text_display -46.0 65.35 29.5 {Tags:["mg.hall","mg.h3_uhc"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"⛏ Mini UHC Run","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -45.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:golden_apple"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.uhc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_uhc,limit=1] text set from storage mg:hall t3x.uhc
summon minecraft:text_display -44.0 65.35 29.5 {Tags:["mg.hall","mg.h3_hg"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🏹 Mini Hunger Games","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -43.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:iron_axe"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.hg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_hg,limit=1] text set from storage mg:hall t3x.hg
summon minecraft:text_display -42.0 65.35 29.5 {Tags:["mg.hall","mg.h3_prophunt"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🎭 Prop Hunt","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -41.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:armor_stand"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.prophunt run data modify entity @e[type=minecraft:text_display,tag=mg.h3_prophunt,limit=1] text set from storage mg:hall t3x.prophunt
summon minecraft:text_display -40.0 65.35 29.5 {Tags:["mg.hall","mg.h3_zombies"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🧟 Zombies","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -39.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:rotten_flesh"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.zombies run data modify entity @e[type=minecraft:text_display,tag=mg.h3_zombies,limit=1] text set from storage mg:hall t3x.zombies
summon minecraft:text_display -38.0 65.35 29.5 {Tags:["mg.hall","mg.h3_infection"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🧪 Infection","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -37.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:zombie_head"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.infection run data modify entity @e[type=minecraft:text_display,tag=mg.h3_infection,limit=1] text set from storage mg:hall t3x.infection
summon minecraft:text_display -36.0 65.35 29.5 {Tags:["mg.hall","mg.h3_bomber"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"💣 Bombardier","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -35.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:fire_charge"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.bomber run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bomber,limit=1] text set from storage mg:hall t3x.bomber
summon minecraft:text_display -34.0 65.35 29.5 {Tags:["mg.hall","mg.h3_chameleon"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🦎 Meccha Chameleon","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -33.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:lime_dye"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.chameleon run data modify entity @e[type=minecraft:text_display,tag=mg.h3_chameleon,limit=1] text set from storage mg:hall t3x.chameleon
summon minecraft:text_display -32.0 65.35 29.5 {Tags:["mg.hall","mg.h3_wii"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🎾 Wii Sports","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -31.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:snowball"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.wii run data modify entity @e[type=minecraft:text_display,tag=mg.h3_wii,limit=1] text set from storage mg:hall t3x.wii
summon minecraft:text_display -30.0 65.35 29.5 {Tags:["mg.hall","mg.h3_soleil"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🔴 1, 2, 3 Soleil","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -29.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:red_dye"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.soleil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_soleil,limit=1] text set from storage mg:hall t3x.soleil
summon minecraft:text_display -28.0 65.35 29.5 {Tags:["mg.hall","mg.h3_autotamp"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🚗 Autos tamponneuses","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -27.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:oak_boat"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.autotamp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_autotamp,limit=1] text set from storage mg:hall t3x.autotamp
summon minecraft:text_display -26.0 65.35 29.5 {Tags:["mg.hall","mg.h3_slimejump"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🟩 Slime Jump","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -25.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:slime_ball"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.slimejump run data modify entity @e[type=minecraft:text_display,tag=mg.h3_slimejump,limit=1] text set from storage mg:hall t3x.slimejump
summon minecraft:text_display -24.0 65.35 29.5 {Tags:["mg.hall","mg.h3_lab"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🙈 Labyrinthe aveugle","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -23.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:ink_sac"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.lab run data modify entity @e[type=minecraft:text_display,tag=mg.h3_lab,limit=1] text set from storage mg:hall t3x.lab
summon minecraft:text_display -22.0 65.35 29.5 {Tags:["mg.hall","mg.h3_master"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"👑 Master dit","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -21.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:clock"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.master run data modify entity @e[type=minecraft:text_display,tag=mg.h3_master,limit=1] text set from storage mg:hall t3x.master
summon minecraft:text_display -20.0 65.35 29.5 {Tags:["mg.hall","mg.h3_murder"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🔪 Murder Mystery","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -19.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:iron_sword"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.murder run data modify entity @e[type=minecraft:text_display,tag=mg.h3_murder,limit=1] text set from storage mg:hall t3x.murder
summon minecraft:text_display -18.0 65.35 29.5 {Tags:["mg.hall","mg.h3_bman"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"💣 Bomberman","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -17.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:tnt"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall t3x.bman run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bman,limit=1] text set from storage mg:hall t3x.bman
summon minecraft:text_display -16.0 65.35 29.5 {Tags:["mg.hall","mg.h3_maze"],billboard:"vertical",line_width:120,background:-937815024,text:[{"text":"🌀 Labyrinthe géant","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:item_display -15.5 65.45 28.5 {Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{id:"minecraft:compass"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
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
data modify storage mg:hall v16 set value 1b
data modify storage mg:hall v17 set value 1b
data modify storage mg:hall v18 set value 1b
data modify storage mg:hall v19 set value 1b
data modify storage mg:hall v20 set value 1b
data modify storage mg:hall v21 set value 1b
data modify storage mg:hall v22 set value 1b
