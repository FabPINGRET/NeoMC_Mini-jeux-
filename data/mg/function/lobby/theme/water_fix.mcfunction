# Fontaines et cascades du spawn remises d'aplomb : ouvrage reposé, passage de l'eau dégagé, eau débordée retirée,
# sources, plantes et nénuphars d'origine reposés (relancé à chaque bascule de thème ; à la main : /function mg:lobby/theme/water_fix)
# Contrôle sans rien modifier : /function mg:lobby/theme/water_check
setblock -59 62 -38 minecraft:dirt
setblock -59 63 -38 minecraft:grass_block
setblock -58 62 -40 minecraft:dirt
setblock -58 62 -39 minecraft:stone
setblock -58 62 -38 minecraft:dirt
setblock -58 62 -37 minecraft:dirt
setblock -58 63 -40 minecraft:grass_block
setblock -58 63 -38 minecraft:grass_block
setblock -58 63 -37 minecraft:grass_block
setblock -57 62 -40 minecraft:dirt
setblock -57 62 -39 minecraft:dirt
setblock -57 62 -38 minecraft:stone
setblock -57 62 -37 minecraft:dirt
setblock -57 62 -36 minecraft:dirt
setblock -57 63 -40 minecraft:grass_block
setblock -57 63 -39 minecraft:grass_block
setblock -57 63 -37 minecraft:grass_block
setblock -57 63 -36 minecraft:grass_block
setblock -56 62 -39 minecraft:dirt
setblock -56 62 -38 minecraft:stone
setblock -56 62 -37 minecraft:stone
setblock -56 62 -36 minecraft:dirt
setblock -56 62 -35 minecraft:dirt
setblock -56 63 -39 minecraft:grass_block
setblock -56 63 -36 minecraft:grass_block
setblock -56 63 -35 minecraft:grass_block
setblock -55 62 -39 minecraft:dirt
setblock -55 62 -38 minecraft:dirt
setblock -55 62 -37 minecraft:stone
setblock -55 62 -36 minecraft:stone
setblock -55 62 -35 minecraft:dirt
setblock -55 63 -39 minecraft:grass_block
setblock -55 63 -38 minecraft:grass_block
setblock -55 63 -35 minecraft:grass_block
setblock -54 62 -38 minecraft:dirt
setblock -54 62 -37 minecraft:dirt
setblock -54 62 -36 minecraft:stone
setblock -54 62 -35 minecraft:dirt
setblock -54 62 -34 minecraft:dirt
setblock -54 63 -38 minecraft:grass_block
setblock -54 63 -37 minecraft:grass_block
setblock -54 63 -35 minecraft:grass_block
setblock -54 63 -34 minecraft:packed_mud
setblock -54 64 -34 minecraft:stone_bricks
setblock -53 62 -37 minecraft:dirt
setblock -53 62 -36 minecraft:stone
setblock -53 62 -35 minecraft:stone
setblock -53 62 -34 minecraft:dirt
setblock -53 63 -37 minecraft:grass_block
setblock -53 63 -34 minecraft:packed_mud
setblock -53 64 -34 minecraft:stone_bricks
setblock -52 62 -37 minecraft:dirt
setblock -52 62 -36 minecraft:dirt
setblock -52 62 -35 minecraft:dirt
setblock -52 62 -34 minecraft:dirt
setblock -52 63 -37 minecraft:grass_block
setblock -52 63 -36 minecraft:dirt_path
setblock -52 63 -35 minecraft:dirt_path
setblock -52 63 -34 minecraft:coarse_dirt
setblock -52 64 -34 minecraft:stone_bricks
execute unless block -60 62 -39 minecraft:air unless block -60 62 -39 minecraft:water run setblock -60 62 -39 minecraft:air
execute unless block -60 63 -39 minecraft:air unless block -60 63 -39 minecraft:water run setblock -60 63 -39 minecraft:air
execute unless block -59 61 -39 minecraft:air unless block -59 61 -39 minecraft:water run setblock -59 61 -39 minecraft:air
execute unless block -59 62 -40 minecraft:air unless block -59 62 -40 minecraft:water run setblock -59 62 -40 minecraft:air
execute unless block -59 62 -39 minecraft:air unless block -59 62 -39 minecraft:water run setblock -59 62 -39 minecraft:air
execute unless block -59 63 -40 minecraft:air unless block -59 63 -40 minecraft:water run setblock -59 63 -40 minecraft:air
execute unless block -59 64 -39 minecraft:air unless block -59 64 -39 minecraft:water run setblock -59 64 -39 minecraft:air
execute unless block -58 64 -39 minecraft:air unless block -58 64 -39 minecraft:water run setblock -58 64 -39 minecraft:air
execute unless block -57 64 -38 minecraft:air unless block -57 64 -38 minecraft:water run setblock -57 64 -38 minecraft:air
execute unless block -56 64 -38 minecraft:air unless block -56 64 -38 minecraft:water run setblock -56 64 -38 minecraft:air
execute unless block -56 64 -37 minecraft:air unless block -56 64 -37 minecraft:water run setblock -56 64 -37 minecraft:air
execute unless block -55 64 -37 minecraft:air unless block -55 64 -37 minecraft:water run setblock -55 64 -37 minecraft:air
execute unless block -55 64 -36 minecraft:air unless block -55 64 -36 minecraft:water run setblock -55 64 -36 minecraft:air
execute unless block -54 64 -36 minecraft:air unless block -54 64 -36 minecraft:water run setblock -54 64 -36 minecraft:air
execute unless block -53 64 -36 minecraft:air unless block -53 64 -36 minecraft:water run setblock -53 64 -36 minecraft:air
execute unless block -53 64 -35 minecraft:air unless block -53 64 -35 minecraft:water run setblock -53 64 -35 minecraft:air
fill -61 62 -41 -51 64 -33 minecraft:air replace minecraft:lily_pad
fill -61 62 -41 -51 64 -33 minecraft:air replace minecraft:water
setblock -59 63 -39 minecraft:water
setblock -58 63 -39 minecraft:water
setblock -57 63 -38 minecraft:water
setblock -56 63 -38 minecraft:water
setblock -56 63 -37 minecraft:water
setblock -55 63 -37 minecraft:water
setblock -55 63 -36 minecraft:water
setblock -54 63 -36 minecraft:water
setblock -53 63 -36 minecraft:water
setblock -53 63 -35 minecraft:water
execute if block -60 64 -35 minecraft:air run setblock -60 64 -35 minecraft:short_grass
execute if block -60 64 -33 minecraft:air run setblock -60 64 -33 minecraft:short_grass
execute if block -59 64 -38 minecraft:air run setblock -59 64 -38 minecraft:short_grass
execute if block -59 64 -35 minecraft:air run setblock -59 64 -35 minecraft:white_tulip
execute if block -59 64 -34 minecraft:air run setblock -59 64 -34 minecraft:short_grass
execute if block -58 64 -36 minecraft:air run setblock -58 64 -36 minecraft:cornflower
execute if block -57 64 -41 minecraft:air run setblock -57 64 -41 minecraft:short_grass
execute if block -57 64 -40 minecraft:air run setblock -57 64 -40 minecraft:red_tulip
execute if block -56 64 -41 minecraft:air run setblock -56 64 -41 minecraft:short_grass
execute if block -55 64 -38 minecraft:air run setblock -55 64 -38 minecraft:short_grass
execute if block -54 64 -37 minecraft:air run setblock -54 64 -37 minecraft:dandelion
execute if block -54 64 -35 minecraft:air run setblock -54 64 -35 minecraft:short_grass
execute if block -53 64 -40 minecraft:air run setblock -53 64 -40 minecraft:fern
execute if block -53 64 -39 minecraft:air run setblock -53 64 -39 minecraft:short_grass
execute if block -53 64 -38 minecraft:air run setblock -53 64 -38 minecraft:fern
execute if block -52 64 -40 minecraft:air run setblock -52 64 -40 minecraft:short_grass
execute if block -52 64 -38 minecraft:air run setblock -52 64 -38 minecraft:short_grass
execute if block -51 64 -41 minecraft:air run setblock -51 64 -41 minecraft:fern
execute if block -51 64 -38 minecraft:air run setblock -51 64 -38 minecraft:white_tulip
setblock -40 62 57 minecraft:coarse_dirt
setblock -40 63 57 minecraft:grass_block
setblock -39 62 55 minecraft:dirt
setblock -39 62 56 minecraft:dirt
setblock -39 62 57 minecraft:dirt
setblock -39 62 58 minecraft:stone
setblock -39 63 55 minecraft:grass_block
setblock -39 63 56 minecraft:grass_block
setblock -39 63 57 minecraft:grass_block
setblock -38 62 54 minecraft:dirt
setblock -38 62 55 minecraft:dirt
setblock -38 62 56 minecraft:stone
setblock -38 62 57 minecraft:stone
setblock -38 62 58 minecraft:rooted_dirt
setblock -38 63 54 minecraft:grass_block
setblock -38 63 55 minecraft:grass_block
setblock -38 63 58 minecraft:grass_block
setblock -37 62 52 minecraft:dirt
setblock -37 62 53 minecraft:dirt
setblock -37 62 54 minecraft:dirt
setblock -37 62 55 minecraft:stone
setblock -37 62 56 minecraft:stone
setblock -37 62 57 minecraft:dirt
setblock -37 62 58 minecraft:rooted_dirt
setblock -37 63 52 minecraft:grass_block
setblock -37 63 53 minecraft:grass_block
setblock -37 63 54 minecraft:grass_block
setblock -37 63 57 minecraft:grass_block
setblock -37 63 58 minecraft:grass_block
setblock -36 62 52 minecraft:dirt
setblock -36 62 53 minecraft:stone
setblock -36 62 54 minecraft:stone
setblock -36 62 55 minecraft:stone
setblock -36 62 56 minecraft:dirt
setblock -36 62 57 minecraft:dirt
setblock -36 63 52 minecraft:dirt_path
setblock -36 63 56 minecraft:grass_block
setblock -36 63 57 minecraft:grass_block
setblock -35 62 52 minecraft:dirt
setblock -35 62 53 minecraft:stone
setblock -35 62 54 minecraft:dirt
setblock -35 62 55 minecraft:dirt
setblock -35 62 56 minecraft:dirt
setblock -35 63 52 minecraft:dirt_path
setblock -35 63 54 minecraft:grass_block
setblock -35 63 55 minecraft:grass_block
setblock -35 63 56 minecraft:grass_block
setblock -34 62 52 minecraft:dirt
setblock -34 62 53 minecraft:dirt
setblock -34 62 54 minecraft:dirt
setblock -34 63 52 minecraft:dirt_path
setblock -34 63 53 minecraft:coarse_dirt
setblock -34 63 54 minecraft:grass_block
execute unless block -40 62 58 minecraft:air unless block -40 62 58 minecraft:water run setblock -40 62 58 minecraft:air
execute unless block -40 62 59 minecraft:air unless block -40 62 59 minecraft:water run setblock -40 62 59 minecraft:air
execute unless block -40 63 58 minecraft:air unless block -40 63 58 minecraft:water run setblock -40 63 58 minecraft:air
execute unless block -40 63 59 minecraft:air unless block -40 63 59 minecraft:water run setblock -40 63 59 minecraft:air
execute unless block -39 61 59 minecraft:air unless block -39 61 59 minecraft:water run setblock -39 61 59 minecraft:air
execute unless block -39 62 59 minecraft:air unless block -39 62 59 minecraft:water run setblock -39 62 59 minecraft:air
execute unless block -39 62 60 minecraft:air unless block -39 62 60 minecraft:water run setblock -39 62 60 minecraft:air
execute unless block -39 63 60 minecraft:air unless block -39 63 60 minecraft:water run setblock -39 63 60 minecraft:air
execute unless block -39 64 58 minecraft:air unless block -39 64 58 minecraft:water run setblock -39 64 58 minecraft:air
execute unless block -39 64 59 minecraft:air unless block -39 64 59 minecraft:water run setblock -39 64 59 minecraft:air
execute unless block -38 63 59 minecraft:air unless block -38 63 59 minecraft:water run setblock -38 63 59 minecraft:air
execute unless block -38 64 56 minecraft:air unless block -38 64 56 minecraft:water run setblock -38 64 56 minecraft:air
execute unless block -38 64 57 minecraft:air unless block -38 64 57 minecraft:water run setblock -38 64 57 minecraft:air
execute unless block -37 64 55 minecraft:air unless block -37 64 55 minecraft:water run setblock -37 64 55 minecraft:air
execute unless block -37 64 56 minecraft:air unless block -37 64 56 minecraft:water run setblock -37 64 56 minecraft:air
execute unless block -36 64 53 minecraft:air unless block -36 64 53 minecraft:water run setblock -36 64 53 minecraft:air
execute unless block -36 64 54 minecraft:air unless block -36 64 54 minecraft:water run setblock -36 64 54 minecraft:air
execute unless block -36 64 55 minecraft:air unless block -36 64 55 minecraft:water run setblock -36 64 55 minecraft:air
execute unless block -35 64 53 minecraft:air unless block -35 64 53 minecraft:water run setblock -35 64 53 minecraft:air
fill -41 62 51 -33 64 61 minecraft:air replace minecraft:lily_pad
fill -41 62 51 -33 64 61 minecraft:air replace minecraft:water
setblock -39 63 58 minecraft:water
setblock -39 63 59 minecraft:water
setblock -38 63 56 minecraft:water
setblock -38 63 57 minecraft:water
setblock -37 63 55 minecraft:water
setblock -37 63 56 minecraft:water
setblock -36 63 53 minecraft:water
setblock -36 63 54 minecraft:water
setblock -36 63 55 minecraft:water
setblock -35 63 53 minecraft:water
execute if block -41 64 52 minecraft:air run setblock -41 64 52 minecraft:orange_tulip
execute if block -41 64 54 minecraft:air run setblock -41 64 54 minecraft:short_grass
execute if block -41 64 55 minecraft:air run setblock -41 64 55 minecraft:short_grass
execute if block -41 64 56 minecraft:air run setblock -41 64 56 minecraft:short_grass
execute if block -40 64 51 minecraft:air run setblock -40 64 51 minecraft:fern
execute if block -39 64 51 minecraft:air run setblock -39 64 51 minecraft:short_grass
execute if block -39 64 54 minecraft:air run setblock -39 64 54 minecraft:short_grass
execute if block -39 64 57 minecraft:air run setblock -39 64 57 minecraft:short_grass
execute if block -37 64 54 minecraft:air run setblock -37 64 54 minecraft:short_grass
execute if block -37 64 57 minecraft:air run setblock -37 64 57 minecraft:short_grass
execute if block -36 64 56 minecraft:air run setblock -36 64 56 minecraft:oxeye_daisy
execute if block -34 64 58 minecraft:air run setblock -34 64 58 minecraft:short_grass
execute if block -34 64 59 minecraft:air run setblock -34 64 59 minecraft:white_tulip
execute if block -33 64 55 minecraft:air run setblock -33 64 55 minecraft:dandelion
execute if block -33 64 56 minecraft:air run setblock -33 64 56 minecraft:fern
execute if block -33 64 60 minecraft:air run setblock -33 64 60 minecraft:short_grass
setblock -34 63 28 minecraft:stone_bricks
setblock -34 63 29 minecraft:stone_bricks
setblock -34 63 30 minecraft:stone_bricks
setblock -34 63 31 minecraft:stone_bricks
setblock -34 63 32 minecraft:stone_bricks
setblock -34 64 28 minecraft:stone_brick_slab
setblock -34 64 29 minecraft:stone_brick_slab
setblock -34 64 30 minecraft:stone_brick_slab
setblock -34 64 31 minecraft:stone_brick_slab
setblock -34 64 32 minecraft:stone_brick_slab
setblock -33 63 27 minecraft:stone_bricks
setblock -33 63 28 minecraft:stone_bricks
setblock -33 63 29 minecraft:stone_bricks
setblock -33 63 30 minecraft:stone_bricks
setblock -33 63 31 minecraft:stone_bricks
setblock -33 63 32 minecraft:stone_bricks
setblock -33 63 33 minecraft:stone_bricks
setblock -33 64 27 minecraft:stone_brick_slab
setblock -33 64 28 minecraft:stone_brick_slab
setblock -33 64 32 minecraft:stone_brick_slab
setblock -33 64 33 minecraft:stone_brick_slab
setblock -32 63 26 minecraft:stone_bricks
setblock -32 63 27 minecraft:stone_bricks
setblock -32 63 28 minecraft:stone_bricks
setblock -32 63 29 minecraft:stone_bricks
setblock -32 63 30 minecraft:stone_bricks
setblock -32 63 31 minecraft:stone_bricks
setblock -32 63 32 minecraft:stone_bricks
setblock -32 63 33 minecraft:stone_bricks
setblock -32 63 34 minecraft:stone_bricks
setblock -32 64 26 minecraft:stone_brick_slab
setblock -32 64 27 minecraft:stone_brick_slab
setblock -32 64 33 minecraft:stone_brick_slab
setblock -32 64 34 minecraft:stone_brick_slab
setblock -31 63 26 minecraft:stone_bricks
setblock -31 63 27 minecraft:stone_bricks
setblock -31 63 28 minecraft:stone_bricks
setblock -31 63 29 minecraft:stone_bricks
setblock -31 63 30 minecraft:stone_bricks
setblock -31 63 31 minecraft:stone_bricks
setblock -31 63 32 minecraft:stone_bricks
setblock -31 63 33 minecraft:stone_bricks
setblock -31 63 34 minecraft:stone_bricks
setblock -31 64 26 minecraft:stone_brick_slab
setblock -31 64 34 minecraft:stone_brick_slab
setblock -30 63 26 minecraft:stone_bricks
setblock -30 63 27 minecraft:stone_bricks
setblock -30 63 28 minecraft:stone_bricks
setblock -30 63 29 minecraft:stone_bricks
setblock -30 63 30 minecraft:stone_bricks
setblock -30 63 31 minecraft:stone_bricks
setblock -30 63 32 minecraft:stone_bricks
setblock -30 63 33 minecraft:stone_bricks
setblock -30 63 34 minecraft:stone_bricks
setblock -30 64 26 minecraft:stone_brick_slab
setblock -30 64 30 minecraft:stone_brick_wall
setblock -30 64 34 minecraft:stone_brick_slab
setblock -30 65 30 minecraft:stone_brick_wall
setblock -30 66 30 minecraft:chiseled_stone_bricks
setblock -29 63 26 minecraft:stone_bricks
setblock -29 63 27 minecraft:stone_bricks
setblock -29 63 28 minecraft:stone_bricks
setblock -29 63 29 minecraft:stone_bricks
setblock -29 63 30 minecraft:stone_bricks
setblock -29 63 31 minecraft:stone_bricks
setblock -29 63 32 minecraft:stone_bricks
setblock -29 63 33 minecraft:stone_bricks
setblock -29 63 34 minecraft:stone_bricks
setblock -29 64 26 minecraft:stone_brick_slab
setblock -29 64 34 minecraft:stone_brick_slab
setblock -28 63 26 minecraft:stone_bricks
setblock -28 63 27 minecraft:stone_bricks
setblock -28 63 28 minecraft:stone_bricks
setblock -28 63 29 minecraft:stone_bricks
setblock -28 63 30 minecraft:stone_bricks
setblock -28 63 31 minecraft:stone_bricks
setblock -28 63 32 minecraft:stone_bricks
setblock -28 63 33 minecraft:stone_bricks
setblock -28 63 34 minecraft:stone_bricks
setblock -28 64 26 minecraft:stone_brick_slab
setblock -28 64 27 minecraft:stone_brick_slab
setblock -28 64 33 minecraft:stone_brick_slab
setblock -28 64 34 minecraft:stone_brick_slab
setblock -27 63 27 minecraft:stone_bricks
setblock -27 63 28 minecraft:stone_bricks
setblock -27 63 29 minecraft:stone_bricks
setblock -27 63 30 minecraft:stone_bricks
setblock -27 63 31 minecraft:stone_bricks
setblock -27 63 32 minecraft:stone_bricks
setblock -27 63 33 minecraft:stone_bricks
setblock -27 64 27 minecraft:stone_brick_slab
setblock -27 64 28 minecraft:stone_brick_slab
setblock -27 64 32 minecraft:stone_brick_slab
setblock -27 64 33 minecraft:stone_brick_slab
setblock -26 63 28 minecraft:stone_bricks
setblock -26 63 29 minecraft:stone_bricks
setblock -26 63 30 minecraft:stone_bricks
setblock -26 63 31 minecraft:stone_bricks
setblock -26 63 32 minecraft:stone_bricks
setblock -26 64 28 minecraft:stone_brick_slab
setblock -26 64 29 minecraft:stone_brick_slab
setblock -26 64 30 minecraft:stone_brick_slab
setblock -26 64 31 minecraft:stone_brick_slab
setblock -26 64 32 minecraft:stone_brick_slab
execute unless block -33 65 29 minecraft:air unless block -33 65 29 minecraft:water run setblock -33 65 29 minecraft:air
execute unless block -33 65 30 minecraft:air unless block -33 65 30 minecraft:water run setblock -33 65 30 minecraft:air
execute unless block -33 65 31 minecraft:air unless block -33 65 31 minecraft:water run setblock -33 65 31 minecraft:air
execute unless block -32 65 28 minecraft:air unless block -32 65 28 minecraft:water run setblock -32 65 28 minecraft:air
execute unless block -32 65 29 minecraft:air unless block -32 65 29 minecraft:water run setblock -32 65 29 minecraft:air
execute unless block -32 65 30 minecraft:air unless block -32 65 30 minecraft:water run setblock -32 65 30 minecraft:air
execute unless block -32 65 31 minecraft:air unless block -32 65 31 minecraft:water run setblock -32 65 31 minecraft:air
execute unless block -32 65 32 minecraft:air unless block -32 65 32 minecraft:water run setblock -32 65 32 minecraft:air
execute unless block -31 65 27 minecraft:air unless block -31 65 27 minecraft:water run setblock -31 65 27 minecraft:air
execute unless block -31 65 28 minecraft:air unless block -31 65 28 minecraft:water run setblock -31 65 28 minecraft:air
execute unless block -31 65 29 minecraft:air unless block -31 65 29 minecraft:water run setblock -31 65 29 minecraft:air
execute unless block -31 65 30 minecraft:air unless block -31 65 30 minecraft:water run setblock -31 65 30 minecraft:air
execute unless block -31 65 31 minecraft:air unless block -31 65 31 minecraft:water run setblock -31 65 31 minecraft:air
execute unless block -31 65 32 minecraft:air unless block -31 65 32 minecraft:water run setblock -31 65 32 minecraft:air
execute unless block -31 65 33 minecraft:air unless block -31 65 33 minecraft:water run setblock -31 65 33 minecraft:air
execute unless block -31 66 30 minecraft:air unless block -31 66 30 minecraft:water run setblock -31 66 30 minecraft:air
execute unless block -31 67 30 minecraft:air unless block -31 67 30 minecraft:water run setblock -31 67 30 minecraft:air
execute unless block -30 65 27 minecraft:air unless block -30 65 27 minecraft:water run setblock -30 65 27 minecraft:air
execute unless block -30 65 28 minecraft:air unless block -30 65 28 minecraft:water run setblock -30 65 28 minecraft:air
execute unless block -30 65 29 minecraft:air unless block -30 65 29 minecraft:water run setblock -30 65 29 minecraft:air
execute unless block -30 65 31 minecraft:air unless block -30 65 31 minecraft:water run setblock -30 65 31 minecraft:air
execute unless block -30 65 32 minecraft:air unless block -30 65 32 minecraft:water run setblock -30 65 32 minecraft:air
execute unless block -30 65 33 minecraft:air unless block -30 65 33 minecraft:water run setblock -30 65 33 minecraft:air
execute unless block -30 66 29 minecraft:air unless block -30 66 29 minecraft:water run setblock -30 66 29 minecraft:air
execute unless block -30 66 31 minecraft:air unless block -30 66 31 minecraft:water run setblock -30 66 31 minecraft:air
execute unless block -30 67 29 minecraft:air unless block -30 67 29 minecraft:water run setblock -30 67 29 minecraft:air
execute unless block -30 67 31 minecraft:air unless block -30 67 31 minecraft:water run setblock -30 67 31 minecraft:air
execute unless block -30 68 30 minecraft:air unless block -30 68 30 minecraft:water run setblock -30 68 30 minecraft:air
execute unless block -29 65 27 minecraft:air unless block -29 65 27 minecraft:water run setblock -29 65 27 minecraft:air
execute unless block -29 65 28 minecraft:air unless block -29 65 28 minecraft:water run setblock -29 65 28 minecraft:air
execute unless block -29 65 29 minecraft:air unless block -29 65 29 minecraft:water run setblock -29 65 29 minecraft:air
execute unless block -29 65 30 minecraft:air unless block -29 65 30 minecraft:water run setblock -29 65 30 minecraft:air
execute unless block -29 65 31 minecraft:air unless block -29 65 31 minecraft:water run setblock -29 65 31 minecraft:air
execute unless block -29 65 32 minecraft:air unless block -29 65 32 minecraft:water run setblock -29 65 32 minecraft:air
execute unless block -29 65 33 minecraft:air unless block -29 65 33 minecraft:water run setblock -29 65 33 minecraft:air
execute unless block -29 66 30 minecraft:air unless block -29 66 30 minecraft:water run setblock -29 66 30 minecraft:air
execute unless block -29 67 30 minecraft:air unless block -29 67 30 minecraft:water run setblock -29 67 30 minecraft:air
execute unless block -28 65 28 minecraft:air unless block -28 65 28 minecraft:water run setblock -28 65 28 minecraft:air
execute unless block -28 65 29 minecraft:air unless block -28 65 29 minecraft:water run setblock -28 65 29 minecraft:air
execute unless block -28 65 30 minecraft:air unless block -28 65 30 minecraft:water run setblock -28 65 30 minecraft:air
execute unless block -28 65 31 minecraft:air unless block -28 65 31 minecraft:water run setblock -28 65 31 minecraft:air
execute unless block -28 65 32 minecraft:air unless block -28 65 32 minecraft:water run setblock -28 65 32 minecraft:air
execute unless block -27 65 29 minecraft:air unless block -27 65 29 minecraft:water run setblock -27 65 29 minecraft:air
execute unless block -27 65 30 minecraft:air unless block -27 65 30 minecraft:water run setblock -27 65 30 minecraft:air
execute unless block -27 65 31 minecraft:air unless block -27 65 31 minecraft:water run setblock -27 65 31 minecraft:air
fill -35 63 25 -25 68 35 minecraft:air replace minecraft:lily_pad
fill -35 63 25 -25 68 35 minecraft:air replace minecraft:water
setblock -33 64 29 minecraft:water
setblock -33 64 30 minecraft:water
setblock -33 64 31 minecraft:water
setblock -32 64 28 minecraft:water
setblock -32 64 29 minecraft:water
setblock -32 64 30 minecraft:water
setblock -32 64 31 minecraft:water
setblock -32 64 32 minecraft:water
setblock -31 64 27 minecraft:water
setblock -31 64 28 minecraft:water
setblock -31 64 29 minecraft:water
setblock -31 64 30 minecraft:water
setblock -31 64 31 minecraft:water
setblock -31 64 32 minecraft:water
setblock -31 64 33 minecraft:water
setblock -30 64 27 minecraft:water
setblock -30 64 28 minecraft:water
setblock -30 64 29 minecraft:water
setblock -30 64 31 minecraft:water
setblock -30 64 32 minecraft:water
setblock -30 64 33 minecraft:water
setblock -30 67 30 minecraft:water
setblock -29 64 27 minecraft:water
setblock -29 64 28 minecraft:water
setblock -29 64 29 minecraft:water
setblock -29 64 30 minecraft:water
setblock -29 64 31 minecraft:water
setblock -29 64 32 minecraft:water
setblock -29 64 33 minecraft:water
setblock -28 64 28 minecraft:water
setblock -28 64 29 minecraft:water
setblock -28 64 30 minecraft:water
setblock -28 64 31 minecraft:water
setblock -28 64 32 minecraft:water
setblock -27 64 29 minecraft:water
setblock -27 64 30 minecraft:water
setblock -27 64 31 minecraft:water
execute if block -35 64 25 minecraft:air run setblock -35 64 25 minecraft:short_grass
execute if block -35 64 26 minecraft:air run setblock -35 64 26 minecraft:dandelion
execute if block -35 64 27 minecraft:air run setblock -35 64 27 minecraft:short_grass
execute if block -35 64 33 minecraft:air run setblock -35 64 33 minecraft:blue_orchid
execute if block -35 64 34 minecraft:air run setblock -35 64 34 minecraft:short_grass
execute if block -34 64 26 minecraft:air run setblock -34 64 26 minecraft:poppy
execute if block -27 64 25 minecraft:air run setblock -27 64 25 minecraft:short_grass
execute if block -26 64 26 minecraft:air run setblock -26 64 26 minecraft:pink_tulip
execute if block -25 64 34 minecraft:air run setblock -25 64 34 minecraft:cornflower
setblock -9 62 -5 minecraft:dirt
setblock -9 62 -4 minecraft:dirt
setblock -9 62 -3 minecraft:dirt
setblock -9 62 -2 minecraft:dirt
setblock -9 62 -1 minecraft:dirt
setblock -9 62 1 minecraft:dirt
setblock -9 62 2 minecraft:dirt
setblock -9 62 3 minecraft:dirt
setblock -9 62 4 minecraft:dirt
setblock -9 62 5 minecraft:dirt
setblock -9 63 -5 minecraft:polished_andesite
setblock -9 63 -4 minecraft:stone_bricks
setblock -9 63 -3 minecraft:stone_bricks
setblock -9 63 -2 minecraft:stone_bricks
setblock -9 63 -1 minecraft:stone_bricks
setblock -9 63 1 minecraft:stone_bricks
setblock -9 63 2 minecraft:stone_bricks
setblock -9 63 3 minecraft:stone_bricks
setblock -9 63 4 minecraft:stone_bricks
setblock -9 63 5 minecraft:polished_diorite
setblock -8 62 -6 minecraft:dirt
setblock -8 62 -5 minecraft:dirt
setblock -8 62 -4 minecraft:dark_prismarine
setblock -8 62 -3 minecraft:prismarine
setblock -8 62 -2 minecraft:prismarine
setblock -8 62 -1 minecraft:dirt
setblock -8 62 1 minecraft:dirt
setblock -8 62 2 minecraft:dark_prismarine
setblock -8 62 3 minecraft:prismarine
setblock -8 62 4 minecraft:prismarine
setblock -8 62 5 minecraft:dirt
setblock -8 62 6 minecraft:dirt
setblock -8 63 -6 minecraft:polished_diorite
setblock -8 63 -5 minecraft:chiseled_stone_bricks
setblock -8 63 -1 minecraft:smooth_quartz
setblock -8 63 1 minecraft:smooth_quartz
setblock -8 63 5 minecraft:stone_bricks
setblock -8 63 6 minecraft:polished_andesite
setblock -7 62 -7 minecraft:dirt
setblock -7 62 -6 minecraft:dirt
setblock -7 62 -5 minecraft:dark_prismarine
setblock -7 62 -4 minecraft:prismarine
setblock -7 62 -3 minecraft:prismarine
setblock -7 62 -2 minecraft:dark_prismarine
setblock -7 62 -1 minecraft:dirt
setblock -7 62 1 minecraft:dirt
setblock -7 62 2 minecraft:prismarine
setblock -7 62 3 minecraft:prismarine
setblock -7 62 4 minecraft:dark_prismarine
setblock -7 62 5 minecraft:prismarine
setblock -7 62 6 minecraft:dirt
setblock -7 62 7 minecraft:dirt
setblock -7 63 -7 minecraft:grass_block
setblock -7 63 -6 minecraft:stone_bricks
setblock -7 63 -1 minecraft:smooth_quartz
setblock -7 63 1 minecraft:smooth_quartz
setblock -7 63 6 minecraft:stone_bricks
setblock -7 63 7 minecraft:grass_block
setblock -6 62 -8 minecraft:dirt
setblock -6 62 -7 minecraft:dirt
setblock -6 62 -6 minecraft:dark_prismarine
setblock -6 62 -5 minecraft:prismarine
setblock -6 62 -4 minecraft:sea_lantern
setblock -6 62 -3 minecraft:dark_prismarine
setblock -6 62 -2 minecraft:prismarine
setblock -6 62 -1 minecraft:dirt
setblock -6 62 1 minecraft:dirt
setblock -6 62 2 minecraft:prismarine
setblock -6 62 3 minecraft:dark_prismarine
setblock -6 62 4 minecraft:prismarine
setblock -6 62 5 minecraft:prismarine
setblock -6 62 6 minecraft:dark_prismarine
setblock -6 62 7 minecraft:dirt
setblock -6 62 8 minecraft:dirt
setblock -6 63 -8 minecraft:polished_andesite
setblock -6 63 -7 minecraft:stone_bricks
setblock -6 63 -1 minecraft:smooth_quartz
setblock -6 63 1 minecraft:smooth_quartz
setblock -6 63 7 minecraft:stone_bricks
setblock -6 63 8 minecraft:polished_diorite
setblock -5 62 -9 minecraft:dirt
setblock -5 62 -8 minecraft:dirt
setblock -5 62 -7 minecraft:dark_prismarine
setblock -5 62 -6 minecraft:prismarine
setblock -5 62 -5 minecraft:prismarine
setblock -5 62 -4 minecraft:dark_prismarine
setblock -5 62 -3 minecraft:prismarine
setblock -5 62 -2 minecraft:dirt
setblock -5 62 -1 minecraft:dirt
setblock -5 62 1 minecraft:dirt
setblock -5 62 2 minecraft:dirt
setblock -5 62 3 minecraft:prismarine
setblock -5 62 4 minecraft:prismarine
setblock -5 62 5 minecraft:dark_prismarine
setblock -5 62 6 minecraft:prismarine
setblock -5 62 7 minecraft:prismarine
setblock -5 62 8 minecraft:dirt
setblock -5 62 9 minecraft:dirt
setblock -5 63 -9 minecraft:polished_diorite
setblock -5 63 -8 minecraft:stone_bricks
setblock -5 63 -5 minecraft:prismarine_bricks
setblock -5 63 -2 minecraft:polished_blackstone_bricks
setblock -5 63 -1 minecraft:polished_blackstone_bricks
setblock -5 63 1 minecraft:polished_blackstone_bricks
setblock -5 63 2 minecraft:polished_blackstone_bricks
setblock -5 63 5 minecraft:prismarine_bricks
setblock -5 63 8 minecraft:chiseled_stone_bricks
setblock -5 63 9 minecraft:polished_andesite
setblock -5 64 -5 minecraft:prismarine_bricks
setblock -5 64 5 minecraft:prismarine_bricks
setblock -5 66 -5 minecraft:sea_lantern
setblock -5 66 5 minecraft:sea_lantern
setblock -4 62 -9 minecraft:dirt
setblock -4 62 -8 minecraft:dark_prismarine
setblock -4 62 -7 minecraft:prismarine
setblock -4 62 -6 minecraft:prismarine
setblock -4 62 -5 minecraft:dark_prismarine
setblock -4 62 -4 minecraft:prismarine
setblock -4 62 -3 minecraft:dirt
setblock -4 62 -2 minecraft:dirt
setblock -4 62 2 minecraft:dirt
setblock -4 62 3 minecraft:dirt
setblock -4 62 4 minecraft:dark_prismarine
setblock -4 62 5 minecraft:prismarine
setblock -4 62 6 minecraft:sea_lantern
setblock -4 62 7 minecraft:dark_prismarine
setblock -4 62 8 minecraft:prismarine
setblock -4 62 9 minecraft:dirt
setblock -4 63 -9 minecraft:stone_bricks
setblock -4 63 -3 minecraft:polished_blackstone_bricks
setblock -4 63 -2 minecraft:smooth_quartz
setblock -4 63 2 minecraft:smooth_quartz
setblock -4 63 3 minecraft:polished_blackstone_bricks
setblock -4 63 9 minecraft:stone_bricks
setblock -3 62 -9 minecraft:dirt
setblock -3 62 -8 minecraft:prismarine
setblock -3 62 -7 minecraft:prismarine
setblock -3 62 -6 minecraft:dark_prismarine
setblock -3 62 -5 minecraft:prismarine
setblock -3 62 -4 minecraft:dirt
setblock -3 62 -3 minecraft:dirt
setblock -3 62 3 minecraft:dirt
setblock -3 62 4 minecraft:dirt
setblock -3 62 5 minecraft:prismarine
setblock -3 62 6 minecraft:dark_prismarine
setblock -3 62 7 minecraft:prismarine
setblock -3 62 8 minecraft:prismarine
setblock -3 62 9 minecraft:dirt
setblock -3 63 -9 minecraft:stone_bricks
setblock -3 63 -4 minecraft:polished_blackstone_bricks
setblock -3 63 -3 minecraft:waxed_cut_copper
setblock -3 63 3 minecraft:waxed_cut_copper
setblock -3 63 4 minecraft:polished_blackstone_bricks
setblock -3 63 9 minecraft:stone_bricks
setblock -2 62 -9 minecraft:dirt
setblock -2 62 -8 minecraft:prismarine
setblock -2 62 -7 minecraft:dark_prismarine
setblock -2 62 -6 minecraft:prismarine
setblock -2 62 -5 minecraft:dirt
setblock -2 62 -4 minecraft:dirt
setblock -2 62 4 minecraft:dirt
setblock -2 62 5 minecraft:dirt
setblock -2 62 6 minecraft:prismarine
setblock -2 62 7 minecraft:prismarine
setblock -2 62 8 minecraft:dark_prismarine
setblock -2 62 9 minecraft:dirt
setblock -2 63 -9 minecraft:stone_bricks
setblock -2 63 -5 minecraft:polished_blackstone_bricks
setblock -2 63 -4 minecraft:smooth_quartz
setblock -2 63 4 minecraft:smooth_quartz
setblock -2 63 5 minecraft:polished_blackstone_bricks
setblock -2 63 9 minecraft:stone_bricks
setblock -1 62 -9 minecraft:dirt
setblock -1 62 -8 minecraft:dirt
setblock -1 62 -7 minecraft:dirt
setblock -1 62 -6 minecraft:dirt
setblock -1 62 -5 minecraft:dirt
setblock -1 62 5 minecraft:dirt
setblock -1 62 6 minecraft:dirt
setblock -1 62 7 minecraft:dirt
setblock -1 62 8 minecraft:dirt
setblock -1 62 9 minecraft:dirt
setblock -1 63 -9 minecraft:stone_bricks
setblock -1 63 -8 minecraft:smooth_quartz
setblock -1 63 -7 minecraft:smooth_quartz
setblock -1 63 -6 minecraft:smooth_quartz
setblock -1 63 -5 minecraft:polished_blackstone_bricks
setblock -1 63 5 minecraft:polished_blackstone_bricks
setblock -1 63 6 minecraft:smooth_quartz
setblock -1 63 7 minecraft:smooth_quartz
setblock -1 63 8 minecraft:smooth_quartz
setblock -1 63 9 minecraft:stone_bricks
setblock 1 62 -9 minecraft:dirt
setblock 1 62 -8 minecraft:dirt
setblock 1 62 -7 minecraft:dirt
setblock 1 62 -6 minecraft:dirt
setblock 1 62 -5 minecraft:dirt
setblock 1 62 5 minecraft:dirt
setblock 1 62 6 minecraft:dirt
setblock 1 62 7 minecraft:dirt
setblock 1 62 8 minecraft:dirt
setblock 1 62 9 minecraft:dirt
setblock 1 63 -9 minecraft:stone_bricks
setblock 1 63 -8 minecraft:smooth_quartz
setblock 1 63 -7 minecraft:smooth_quartz
setblock 1 63 -6 minecraft:smooth_quartz
setblock 1 63 -5 minecraft:polished_blackstone_bricks
setblock 1 63 5 minecraft:polished_blackstone_bricks
setblock 1 63 6 minecraft:smooth_quartz
setblock 1 63 7 minecraft:smooth_quartz
setblock 1 63 8 minecraft:smooth_quartz
setblock 1 63 9 minecraft:stone_bricks
setblock 2 62 -9 minecraft:dirt
setblock 2 62 -8 minecraft:dark_prismarine
setblock 2 62 -7 minecraft:prismarine
setblock 2 62 -6 minecraft:prismarine
setblock 2 62 -5 minecraft:dirt
setblock 2 62 -4 minecraft:dirt
setblock 2 62 4 minecraft:dirt
setblock 2 62 5 minecraft:dirt
setblock 2 62 6 minecraft:prismarine
setblock 2 62 7 minecraft:dark_prismarine
setblock 2 62 8 minecraft:prismarine
setblock 2 62 9 minecraft:dirt
setblock 2 63 -9 minecraft:stone_bricks
setblock 2 63 -5 minecraft:polished_blackstone_bricks
setblock 2 63 -4 minecraft:smooth_quartz
setblock 2 63 4 minecraft:smooth_quartz
setblock 2 63 5 minecraft:polished_blackstone_bricks
setblock 2 63 9 minecraft:stone_bricks
setblock 3 62 -9 minecraft:dirt
setblock 3 62 -8 minecraft:prismarine
setblock 3 62 -7 minecraft:prismarine
setblock 3 62 -6 minecraft:dark_prismarine
setblock 3 62 -5 minecraft:prismarine
setblock 3 62 -4 minecraft:dirt
setblock 3 62 -3 minecraft:dirt
setblock 3 62 3 minecraft:dirt
setblock 3 62 4 minecraft:dirt
setblock 3 62 5 minecraft:prismarine
setblock 3 62 6 minecraft:dark_prismarine
setblock 3 62 7 minecraft:prismarine
setblock 3 62 8 minecraft:prismarine
setblock 3 62 9 minecraft:dirt
setblock 3 63 -9 minecraft:stone_bricks
setblock 3 63 -4 minecraft:polished_blackstone_bricks
setblock 3 63 -3 minecraft:waxed_cut_copper
setblock 3 63 3 minecraft:waxed_cut_copper
setblock 3 63 4 minecraft:polished_blackstone_bricks
setblock 3 63 9 minecraft:stone_bricks
setblock 4 62 -9 minecraft:dirt
setblock 4 62 -8 minecraft:prismarine
setblock 4 62 -7 minecraft:dark_prismarine
setblock 4 62 -6 minecraft:sea_lantern
setblock 4 62 -5 minecraft:prismarine
setblock 4 62 -4 minecraft:dark_prismarine
setblock 4 62 -3 minecraft:dirt
setblock 4 62 -2 minecraft:dirt
setblock 4 62 2 minecraft:dirt
setblock 4 62 3 minecraft:dirt
setblock 4 62 4 minecraft:prismarine
setblock 4 62 5 minecraft:dark_prismarine
setblock 4 62 6 minecraft:prismarine
setblock 4 62 7 minecraft:prismarine
setblock 4 62 8 minecraft:dark_prismarine
setblock 4 62 9 minecraft:dirt
setblock 4 63 -9 minecraft:stone_bricks
setblock 4 63 -3 minecraft:polished_blackstone_bricks
setblock 4 63 -2 minecraft:smooth_quartz
setblock 4 63 2 minecraft:smooth_quartz
setblock 4 63 3 minecraft:polished_blackstone_bricks
setblock 4 63 9 minecraft:stone_bricks
setblock 5 62 -9 minecraft:dirt
setblock 5 62 -8 minecraft:dirt
setblock 5 62 -7 minecraft:prismarine
setblock 5 62 -6 minecraft:prismarine
setblock 5 62 -5 minecraft:dark_prismarine
setblock 5 62 -4 minecraft:prismarine
setblock 5 62 -3 minecraft:prismarine
setblock 5 62 -2 minecraft:dirt
setblock 5 62 -1 minecraft:dirt
setblock 5 62 1 minecraft:dirt
setblock 5 62 2 minecraft:dirt
setblock 5 62 3 minecraft:prismarine
setblock 5 62 4 minecraft:dark_prismarine
setblock 5 62 5 minecraft:prismarine
setblock 5 62 6 minecraft:prismarine
setblock 5 62 7 minecraft:dark_prismarine
setblock 5 62 8 minecraft:dirt
setblock 5 62 9 minecraft:dirt
setblock 5 63 -9 minecraft:polished_andesite
setblock 5 63 -8 minecraft:chiseled_stone_bricks
setblock 5 63 -5 minecraft:prismarine_bricks
setblock 5 63 -2 minecraft:polished_blackstone_bricks
setblock 5 63 -1 minecraft:polished_blackstone_bricks
setblock 5 63 1 minecraft:polished_blackstone_bricks
setblock 5 63 2 minecraft:polished_blackstone_bricks
setblock 5 63 5 minecraft:prismarine_bricks
setblock 5 63 8 minecraft:stone_bricks
setblock 5 63 9 minecraft:polished_diorite
setblock 5 64 -5 minecraft:prismarine_bricks
setblock 5 64 5 minecraft:prismarine_bricks
setblock 5 66 -5 minecraft:sea_lantern
setblock 5 66 5 minecraft:sea_lantern
setblock 6 62 -8 minecraft:dirt
setblock 6 62 -7 minecraft:dirt
setblock 6 62 -6 minecraft:dark_prismarine
setblock 6 62 -5 minecraft:prismarine
setblock 6 62 -4 minecraft:prismarine
setblock 6 62 -3 minecraft:dark_prismarine
setblock 6 62 -2 minecraft:prismarine
setblock 6 62 -1 minecraft:dirt
setblock 6 62 1 minecraft:dirt
setblock 6 62 2 minecraft:prismarine
setblock 6 62 3 minecraft:dark_prismarine
setblock 6 62 4 minecraft:sea_lantern
setblock 6 62 5 minecraft:prismarine
setblock 6 62 6 minecraft:dark_prismarine
setblock 6 62 7 minecraft:dirt
setblock 6 62 8 minecraft:dirt
setblock 6 63 -8 minecraft:polished_diorite
setblock 6 63 -7 minecraft:stone_bricks
setblock 6 63 -1 minecraft:smooth_quartz
setblock 6 63 1 minecraft:smooth_quartz
setblock 6 63 7 minecraft:stone_bricks
setblock 6 63 8 minecraft:polished_andesite
setblock 7 62 -7 minecraft:dirt
setblock 7 62 -6 minecraft:dirt
setblock 7 62 -5 minecraft:prismarine
setblock 7 62 -4 minecraft:dark_prismarine
setblock 7 62 -3 minecraft:prismarine
setblock 7 62 -2 minecraft:prismarine
setblock 7 62 -1 minecraft:dirt
setblock 7 62 1 minecraft:dirt
setblock 7 62 2 minecraft:dark_prismarine
setblock 7 62 3 minecraft:prismarine
setblock 7 62 4 minecraft:prismarine
setblock 7 62 5 minecraft:dark_prismarine
setblock 7 62 6 minecraft:dirt
setblock 7 62 7 minecraft:dirt
setblock 7 63 -7 minecraft:grass_block
setblock 7 63 -6 minecraft:stone_bricks
setblock 7 63 -1 minecraft:smooth_quartz
setblock 7 63 1 minecraft:smooth_quartz
setblock 7 63 6 minecraft:stone_bricks
setblock 7 63 7 minecraft:grass_block
setblock 8 62 -6 minecraft:dirt
setblock 8 62 -5 minecraft:dirt
setblock 8 62 -4 minecraft:prismarine
setblock 8 62 -3 minecraft:prismarine
setblock 8 62 -2 minecraft:dark_prismarine
setblock 8 62 -1 minecraft:dirt
setblock 8 62 1 minecraft:dirt
setblock 8 62 2 minecraft:prismarine
setblock 8 62 3 minecraft:prismarine
setblock 8 62 4 minecraft:dark_prismarine
setblock 8 62 5 minecraft:dirt
setblock 8 62 6 minecraft:dirt
setblock 8 63 -6 minecraft:polished_andesite
setblock 8 63 -5 minecraft:stone_bricks
setblock 8 63 -1 minecraft:smooth_quartz
setblock 8 63 1 minecraft:smooth_quartz
setblock 8 63 5 minecraft:chiseled_stone_bricks
setblock 8 63 6 minecraft:polished_diorite
setblock 9 62 -5 minecraft:dirt
setblock 9 62 -4 minecraft:dirt
setblock 9 62 -3 minecraft:dirt
setblock 9 62 -2 minecraft:dirt
setblock 9 62 -1 minecraft:dirt
setblock 9 62 1 minecraft:dirt
setblock 9 62 2 minecraft:dirt
setblock 9 62 3 minecraft:dirt
setblock 9 62 4 minecraft:dirt
setblock 9 62 5 minecraft:dirt
setblock 9 63 -5 minecraft:polished_diorite
setblock 9 63 -4 minecraft:stone_bricks
setblock 9 63 -3 minecraft:stone_bricks
setblock 9 63 -2 minecraft:stone_bricks
setblock 9 63 -1 minecraft:stone_bricks
setblock 9 63 1 minecraft:stone_bricks
setblock 9 63 2 minecraft:stone_bricks
setblock 9 63 3 minecraft:stone_bricks
setblock 9 63 4 minecraft:stone_bricks
setblock 9 63 5 minecraft:polished_andesite
execute unless block -8 64 -4 minecraft:air unless block -8 64 -4 minecraft:water run setblock -8 64 -4 minecraft:air
execute unless block -8 64 -3 minecraft:air unless block -8 64 -3 minecraft:water run setblock -8 64 -3 minecraft:air
execute unless block -8 64 -2 minecraft:air unless block -8 64 -2 minecraft:water run setblock -8 64 -2 minecraft:air
execute unless block -8 64 2 minecraft:air unless block -8 64 2 minecraft:water run setblock -8 64 2 minecraft:air
execute unless block -8 64 3 minecraft:air unless block -8 64 3 minecraft:water run setblock -8 64 3 minecraft:air
execute unless block -8 64 4 minecraft:air unless block -8 64 4 minecraft:water run setblock -8 64 4 minecraft:air
execute unless block -7 64 -5 minecraft:air unless block -7 64 -5 minecraft:water run setblock -7 64 -5 minecraft:air
execute unless block -7 64 -4 minecraft:air unless block -7 64 -4 minecraft:water run setblock -7 64 -4 minecraft:air
execute unless block -7 64 -3 minecraft:air unless block -7 64 -3 minecraft:water run setblock -7 64 -3 minecraft:air
execute unless block -7 64 -2 minecraft:air unless block -7 64 -2 minecraft:water run setblock -7 64 -2 minecraft:air
execute unless block -7 64 2 minecraft:air unless block -7 64 2 minecraft:water run setblock -7 64 2 minecraft:air
execute unless block -7 64 3 minecraft:air unless block -7 64 3 minecraft:water run setblock -7 64 3 minecraft:air
execute unless block -7 64 4 minecraft:air unless block -7 64 4 minecraft:water run setblock -7 64 4 minecraft:air
execute unless block -7 64 5 minecraft:air unless block -7 64 5 minecraft:water run setblock -7 64 5 minecraft:air
execute unless block -6 64 -6 minecraft:air unless block -6 64 -6 minecraft:water run setblock -6 64 -6 minecraft:air
execute unless block -6 64 -5 minecraft:air unless block -6 64 -5 minecraft:water run setblock -6 64 -5 minecraft:air
execute unless block -6 64 -4 minecraft:air unless block -6 64 -4 minecraft:water run setblock -6 64 -4 minecraft:air
execute unless block -6 64 -3 minecraft:air unless block -6 64 -3 minecraft:water run setblock -6 64 -3 minecraft:air
execute unless block -6 64 -2 minecraft:air unless block -6 64 -2 minecraft:water run setblock -6 64 -2 minecraft:air
execute unless block -6 64 2 minecraft:air unless block -6 64 2 minecraft:water run setblock -6 64 2 minecraft:air
execute unless block -6 64 3 minecraft:air unless block -6 64 3 minecraft:water run setblock -6 64 3 minecraft:air
execute unless block -6 64 4 minecraft:air unless block -6 64 4 minecraft:water run setblock -6 64 4 minecraft:air
execute unless block -6 64 5 minecraft:air unless block -6 64 5 minecraft:water run setblock -6 64 5 minecraft:air
execute unless block -6 64 6 minecraft:air unless block -6 64 6 minecraft:water run setblock -6 64 6 minecraft:air
execute unless block -6 65 -5 minecraft:air unless block -6 65 -5 minecraft:water run setblock -6 65 -5 minecraft:air
execute unless block -6 65 5 minecraft:air unless block -6 65 5 minecraft:water run setblock -6 65 5 minecraft:air
execute unless block -6 66 -5 minecraft:air unless block -6 66 -5 minecraft:water run setblock -6 66 -5 minecraft:air
execute unless block -6 66 5 minecraft:air unless block -6 66 5 minecraft:water run setblock -6 66 5 minecraft:air
execute unless block -6 67 -5 minecraft:air unless block -6 67 -5 minecraft:water run setblock -6 67 -5 minecraft:air
execute unless block -6 67 5 minecraft:air unless block -6 67 5 minecraft:water run setblock -6 67 5 minecraft:air
execute unless block -5 64 -7 minecraft:air unless block -5 64 -7 minecraft:water run setblock -5 64 -7 minecraft:air
execute unless block -5 64 -6 minecraft:air unless block -5 64 -6 minecraft:water run setblock -5 64 -6 minecraft:air
execute unless block -5 64 -4 minecraft:air unless block -5 64 -4 minecraft:water run setblock -5 64 -4 minecraft:air
execute unless block -5 64 -3 minecraft:air unless block -5 64 -3 minecraft:water run setblock -5 64 -3 minecraft:air
execute unless block -5 64 3 minecraft:air unless block -5 64 3 minecraft:water run setblock -5 64 3 minecraft:air
execute unless block -5 64 4 minecraft:air unless block -5 64 4 minecraft:water run setblock -5 64 4 minecraft:air
execute unless block -5 64 6 minecraft:air unless block -5 64 6 minecraft:water run setblock -5 64 6 minecraft:air
execute unless block -5 64 7 minecraft:air unless block -5 64 7 minecraft:water run setblock -5 64 7 minecraft:air
execute unless block -5 65 -6 minecraft:air unless block -5 65 -6 minecraft:water run setblock -5 65 -6 minecraft:air
execute unless block -5 65 -4 minecraft:air unless block -5 65 -4 minecraft:water run setblock -5 65 -4 minecraft:air
execute unless block -5 65 4 minecraft:air unless block -5 65 4 minecraft:water run setblock -5 65 4 minecraft:air
execute unless block -5 65 6 minecraft:air unless block -5 65 6 minecraft:water run setblock -5 65 6 minecraft:air
execute unless block -5 66 -6 minecraft:air unless block -5 66 -6 minecraft:water run setblock -5 66 -6 minecraft:air
execute unless block -5 66 -4 minecraft:air unless block -5 66 -4 minecraft:water run setblock -5 66 -4 minecraft:air
execute unless block -5 66 4 minecraft:air unless block -5 66 4 minecraft:water run setblock -5 66 4 minecraft:air
execute unless block -5 66 6 minecraft:air unless block -5 66 6 minecraft:water run setblock -5 66 6 minecraft:air
execute unless block -5 67 -6 minecraft:air unless block -5 67 -6 minecraft:water run setblock -5 67 -6 minecraft:air
execute unless block -5 67 -4 minecraft:air unless block -5 67 -4 minecraft:water run setblock -5 67 -4 minecraft:air
execute unless block -5 67 4 minecraft:air unless block -5 67 4 minecraft:water run setblock -5 67 4 minecraft:air
execute unless block -5 67 6 minecraft:air unless block -5 67 6 minecraft:water run setblock -5 67 6 minecraft:air
execute unless block -5 68 -5 minecraft:air unless block -5 68 -5 minecraft:water run setblock -5 68 -5 minecraft:air
execute unless block -5 68 5 minecraft:air unless block -5 68 5 minecraft:water run setblock -5 68 5 minecraft:air
execute unless block -4 64 -8 minecraft:air unless block -4 64 -8 minecraft:water run setblock -4 64 -8 minecraft:air
execute unless block -4 64 -7 minecraft:air unless block -4 64 -7 minecraft:water run setblock -4 64 -7 minecraft:air
execute unless block -4 64 -6 minecraft:air unless block -4 64 -6 minecraft:water run setblock -4 64 -6 minecraft:air
execute unless block -4 64 -5 minecraft:air unless block -4 64 -5 minecraft:water run setblock -4 64 -5 minecraft:air
execute unless block -4 64 -4 minecraft:air unless block -4 64 -4 minecraft:water run setblock -4 64 -4 minecraft:air
execute unless block -4 64 4 minecraft:air unless block -4 64 4 minecraft:water run setblock -4 64 4 minecraft:air
execute unless block -4 64 5 minecraft:air unless block -4 64 5 minecraft:water run setblock -4 64 5 minecraft:air
execute unless block -4 64 6 minecraft:air unless block -4 64 6 minecraft:water run setblock -4 64 6 minecraft:air
execute unless block -4 64 7 minecraft:air unless block -4 64 7 minecraft:water run setblock -4 64 7 minecraft:air
execute unless block -4 64 8 minecraft:air unless block -4 64 8 minecraft:water run setblock -4 64 8 minecraft:air
execute unless block -4 65 -5 minecraft:air unless block -4 65 -5 minecraft:water run setblock -4 65 -5 minecraft:air
execute unless block -4 65 5 minecraft:air unless block -4 65 5 minecraft:water run setblock -4 65 5 minecraft:air
execute unless block -4 66 -5 minecraft:air unless block -4 66 -5 minecraft:water run setblock -4 66 -5 minecraft:air
execute unless block -4 66 5 minecraft:air unless block -4 66 5 minecraft:water run setblock -4 66 5 minecraft:air
execute unless block -4 67 -5 minecraft:air unless block -4 67 -5 minecraft:water run setblock -4 67 -5 minecraft:air
execute unless block -4 67 5 minecraft:air unless block -4 67 5 minecraft:water run setblock -4 67 5 minecraft:air
execute unless block -3 64 -8 minecraft:air unless block -3 64 -8 minecraft:water run setblock -3 64 -8 minecraft:air
execute unless block -3 64 -7 minecraft:air unless block -3 64 -7 minecraft:water run setblock -3 64 -7 minecraft:air
execute unless block -3 64 -6 minecraft:air unless block -3 64 -6 minecraft:water run setblock -3 64 -6 minecraft:air
execute unless block -3 64 -5 minecraft:air unless block -3 64 -5 minecraft:water run setblock -3 64 -5 minecraft:air
execute unless block -3 64 5 minecraft:air unless block -3 64 5 minecraft:water run setblock -3 64 5 minecraft:air
execute unless block -3 64 6 minecraft:air unless block -3 64 6 minecraft:water run setblock -3 64 6 minecraft:air
execute unless block -3 64 7 minecraft:air unless block -3 64 7 minecraft:water run setblock -3 64 7 minecraft:air
execute unless block -3 64 8 minecraft:air unless block -3 64 8 minecraft:water run setblock -3 64 8 minecraft:air
execute unless block -2 64 -8 minecraft:air unless block -2 64 -8 minecraft:water run setblock -2 64 -8 minecraft:air
execute unless block -2 64 -7 minecraft:air unless block -2 64 -7 minecraft:water run setblock -2 64 -7 minecraft:air
execute unless block -2 64 -6 minecraft:air unless block -2 64 -6 minecraft:water run setblock -2 64 -6 minecraft:air
execute unless block -2 64 6 minecraft:air unless block -2 64 6 minecraft:water run setblock -2 64 6 minecraft:air
execute unless block -2 64 7 minecraft:air unless block -2 64 7 minecraft:water run setblock -2 64 7 minecraft:air
execute unless block -2 64 8 minecraft:air unless block -2 64 8 minecraft:water run setblock -2 64 8 minecraft:air
execute unless block 2 64 -8 minecraft:air unless block 2 64 -8 minecraft:water run setblock 2 64 -8 minecraft:air
execute unless block 2 64 -7 minecraft:air unless block 2 64 -7 minecraft:water run setblock 2 64 -7 minecraft:air
execute unless block 2 64 -6 minecraft:air unless block 2 64 -6 minecraft:water run setblock 2 64 -6 minecraft:air
execute unless block 2 64 6 minecraft:air unless block 2 64 6 minecraft:water run setblock 2 64 6 minecraft:air
execute unless block 2 64 7 minecraft:air unless block 2 64 7 minecraft:water run setblock 2 64 7 minecraft:air
execute unless block 2 64 8 minecraft:air unless block 2 64 8 minecraft:water run setblock 2 64 8 minecraft:air
execute unless block 3 64 -8 minecraft:air unless block 3 64 -8 minecraft:water run setblock 3 64 -8 minecraft:air
execute unless block 3 64 -7 minecraft:air unless block 3 64 -7 minecraft:water run setblock 3 64 -7 minecraft:air
execute unless block 3 64 -6 minecraft:air unless block 3 64 -6 minecraft:water run setblock 3 64 -6 minecraft:air
execute unless block 3 64 -5 minecraft:air unless block 3 64 -5 minecraft:water run setblock 3 64 -5 minecraft:air
execute unless block 3 64 5 minecraft:air unless block 3 64 5 minecraft:water run setblock 3 64 5 minecraft:air
execute unless block 3 64 6 minecraft:air unless block 3 64 6 minecraft:water run setblock 3 64 6 minecraft:air
execute unless block 3 64 7 minecraft:air unless block 3 64 7 minecraft:water run setblock 3 64 7 minecraft:air
execute unless block 3 64 8 minecraft:air unless block 3 64 8 minecraft:water run setblock 3 64 8 minecraft:air
execute unless block 4 64 -8 minecraft:air unless block 4 64 -8 minecraft:water run setblock 4 64 -8 minecraft:air
execute unless block 4 64 -7 minecraft:air unless block 4 64 -7 minecraft:water run setblock 4 64 -7 minecraft:air
execute unless block 4 64 -6 minecraft:air unless block 4 64 -6 minecraft:water run setblock 4 64 -6 minecraft:air
execute unless block 4 64 -5 minecraft:air unless block 4 64 -5 minecraft:water run setblock 4 64 -5 minecraft:air
execute unless block 4 64 -4 minecraft:air unless block 4 64 -4 minecraft:water run setblock 4 64 -4 minecraft:air
execute unless block 4 64 4 minecraft:air unless block 4 64 4 minecraft:water run setblock 4 64 4 minecraft:air
execute unless block 4 64 5 minecraft:air unless block 4 64 5 minecraft:water run setblock 4 64 5 minecraft:air
execute unless block 4 64 6 minecraft:air unless block 4 64 6 minecraft:water run setblock 4 64 6 minecraft:air
execute unless block 4 64 7 minecraft:air unless block 4 64 7 minecraft:water run setblock 4 64 7 minecraft:air
execute unless block 4 64 8 minecraft:air unless block 4 64 8 minecraft:water run setblock 4 64 8 minecraft:air
execute unless block 4 65 -5 minecraft:air unless block 4 65 -5 minecraft:water run setblock 4 65 -5 minecraft:air
execute unless block 4 65 5 minecraft:air unless block 4 65 5 minecraft:water run setblock 4 65 5 minecraft:air
execute unless block 4 66 -5 minecraft:air unless block 4 66 -5 minecraft:water run setblock 4 66 -5 minecraft:air
execute unless block 4 66 5 minecraft:air unless block 4 66 5 minecraft:water run setblock 4 66 5 minecraft:air
execute unless block 4 67 -5 minecraft:air unless block 4 67 -5 minecraft:water run setblock 4 67 -5 minecraft:air
execute unless block 4 67 5 minecraft:air unless block 4 67 5 minecraft:water run setblock 4 67 5 minecraft:air
execute unless block 5 64 -7 minecraft:air unless block 5 64 -7 minecraft:water run setblock 5 64 -7 minecraft:air
execute unless block 5 64 -6 minecraft:air unless block 5 64 -6 minecraft:water run setblock 5 64 -6 minecraft:air
execute unless block 5 64 -4 minecraft:air unless block 5 64 -4 minecraft:water run setblock 5 64 -4 minecraft:air
execute unless block 5 64 -3 minecraft:air unless block 5 64 -3 minecraft:water run setblock 5 64 -3 minecraft:air
execute unless block 5 64 3 minecraft:air unless block 5 64 3 minecraft:water run setblock 5 64 3 minecraft:air
execute unless block 5 64 4 minecraft:air unless block 5 64 4 minecraft:water run setblock 5 64 4 minecraft:air
execute unless block 5 64 6 minecraft:air unless block 5 64 6 minecraft:water run setblock 5 64 6 minecraft:air
execute unless block 5 64 7 minecraft:air unless block 5 64 7 minecraft:water run setblock 5 64 7 minecraft:air
execute unless block 5 65 -6 minecraft:air unless block 5 65 -6 minecraft:water run setblock 5 65 -6 minecraft:air
execute unless block 5 65 -4 minecraft:air unless block 5 65 -4 minecraft:water run setblock 5 65 -4 minecraft:air
execute unless block 5 65 4 minecraft:air unless block 5 65 4 minecraft:water run setblock 5 65 4 minecraft:air
execute unless block 5 65 6 minecraft:air unless block 5 65 6 minecraft:water run setblock 5 65 6 minecraft:air
execute unless block 5 66 -6 minecraft:air unless block 5 66 -6 minecraft:water run setblock 5 66 -6 minecraft:air
execute unless block 5 66 -4 minecraft:air unless block 5 66 -4 minecraft:water run setblock 5 66 -4 minecraft:air
execute unless block 5 66 4 minecraft:air unless block 5 66 4 minecraft:water run setblock 5 66 4 minecraft:air
execute unless block 5 66 6 minecraft:air unless block 5 66 6 minecraft:water run setblock 5 66 6 minecraft:air
execute unless block 5 67 -6 minecraft:air unless block 5 67 -6 minecraft:water run setblock 5 67 -6 minecraft:air
execute unless block 5 67 -4 minecraft:air unless block 5 67 -4 minecraft:water run setblock 5 67 -4 minecraft:air
execute unless block 5 67 4 minecraft:air unless block 5 67 4 minecraft:water run setblock 5 67 4 minecraft:air
execute unless block 5 67 6 minecraft:air unless block 5 67 6 minecraft:water run setblock 5 67 6 minecraft:air
execute unless block 5 68 -5 minecraft:air unless block 5 68 -5 minecraft:water run setblock 5 68 -5 minecraft:air
execute unless block 5 68 5 minecraft:air unless block 5 68 5 minecraft:water run setblock 5 68 5 minecraft:air
execute unless block 6 64 -6 minecraft:air unless block 6 64 -6 minecraft:water run setblock 6 64 -6 minecraft:air
execute unless block 6 64 -5 minecraft:air unless block 6 64 -5 minecraft:water run setblock 6 64 -5 minecraft:air
execute unless block 6 64 -4 minecraft:air unless block 6 64 -4 minecraft:water run setblock 6 64 -4 minecraft:air
execute unless block 6 64 -3 minecraft:air unless block 6 64 -3 minecraft:water run setblock 6 64 -3 minecraft:air
execute unless block 6 64 -2 minecraft:air unless block 6 64 -2 minecraft:water run setblock 6 64 -2 minecraft:air
execute unless block 6 64 2 minecraft:air unless block 6 64 2 minecraft:water run setblock 6 64 2 minecraft:air
execute unless block 6 64 3 minecraft:air unless block 6 64 3 minecraft:water run setblock 6 64 3 minecraft:air
execute unless block 6 64 4 minecraft:air unless block 6 64 4 minecraft:water run setblock 6 64 4 minecraft:air
execute unless block 6 64 5 minecraft:air unless block 6 64 5 minecraft:water run setblock 6 64 5 minecraft:air
execute unless block 6 64 6 minecraft:air unless block 6 64 6 minecraft:water run setblock 6 64 6 minecraft:air
execute unless block 6 65 -5 minecraft:air unless block 6 65 -5 minecraft:water run setblock 6 65 -5 minecraft:air
execute unless block 6 65 5 minecraft:air unless block 6 65 5 minecraft:water run setblock 6 65 5 minecraft:air
execute unless block 6 66 -5 minecraft:air unless block 6 66 -5 minecraft:water run setblock 6 66 -5 minecraft:air
execute unless block 6 66 5 minecraft:air unless block 6 66 5 minecraft:water run setblock 6 66 5 minecraft:air
execute unless block 6 67 -5 minecraft:air unless block 6 67 -5 minecraft:water run setblock 6 67 -5 minecraft:air
execute unless block 6 67 5 minecraft:air unless block 6 67 5 minecraft:water run setblock 6 67 5 minecraft:air
execute unless block 7 64 -5 minecraft:air unless block 7 64 -5 minecraft:water run setblock 7 64 -5 minecraft:air
execute unless block 7 64 -4 minecraft:air unless block 7 64 -4 minecraft:water run setblock 7 64 -4 minecraft:air
execute unless block 7 64 -3 minecraft:air unless block 7 64 -3 minecraft:water run setblock 7 64 -3 minecraft:air
execute unless block 7 64 -2 minecraft:air unless block 7 64 -2 minecraft:water run setblock 7 64 -2 minecraft:air
execute unless block 7 64 2 minecraft:air unless block 7 64 2 minecraft:water run setblock 7 64 2 minecraft:air
execute unless block 7 64 3 minecraft:air unless block 7 64 3 minecraft:water run setblock 7 64 3 minecraft:air
execute unless block 7 64 4 minecraft:air unless block 7 64 4 minecraft:water run setblock 7 64 4 minecraft:air
execute unless block 7 64 5 minecraft:air unless block 7 64 5 minecraft:water run setblock 7 64 5 minecraft:air
execute unless block 8 64 -4 minecraft:air unless block 8 64 -4 minecraft:water run setblock 8 64 -4 minecraft:air
execute unless block 8 64 -3 minecraft:air unless block 8 64 -3 minecraft:water run setblock 8 64 -3 minecraft:air
execute unless block 8 64 -2 minecraft:air unless block 8 64 -2 minecraft:water run setblock 8 64 -2 minecraft:air
execute unless block 8 64 2 minecraft:air unless block 8 64 2 minecraft:water run setblock 8 64 2 minecraft:air
execute unless block 8 64 3 minecraft:air unless block 8 64 3 minecraft:water run setblock 8 64 3 minecraft:air
execute unless block 8 64 4 minecraft:air unless block 8 64 4 minecraft:water run setblock 8 64 4 minecraft:air
fill -10 62 -10 10 68 10 minecraft:air replace minecraft:lily_pad
fill -10 62 -10 10 68 10 minecraft:air replace minecraft:water
setblock -8 63 -4 minecraft:water
setblock -8 63 -3 minecraft:water
setblock -8 63 -2 minecraft:water
setblock -8 63 2 minecraft:water
setblock -8 63 3 minecraft:water
setblock -8 63 4 minecraft:water
setblock -7 63 -5 minecraft:water
setblock -7 63 -4 minecraft:water
setblock -7 63 -3 minecraft:water
setblock -7 63 -2 minecraft:water
setblock -7 63 2 minecraft:water
setblock -7 63 3 minecraft:water
setblock -7 63 4 minecraft:water
setblock -7 63 5 minecraft:water
setblock -6 63 -6 minecraft:water
setblock -6 63 -5 minecraft:water
setblock -6 63 -4 minecraft:water
setblock -6 63 -3 minecraft:water
setblock -6 63 -2 minecraft:water
setblock -6 63 2 minecraft:water
setblock -6 63 3 minecraft:water
setblock -6 63 4 minecraft:water
setblock -6 63 5 minecraft:water
setblock -6 63 6 minecraft:water
setblock -5 63 -7 minecraft:water
setblock -5 63 -6 minecraft:water
setblock -5 63 -4 minecraft:water
setblock -5 63 -3 minecraft:water
setblock -5 63 3 minecraft:water
setblock -5 63 4 minecraft:water
setblock -5 63 6 minecraft:water
setblock -5 63 7 minecraft:water
setblock -5 67 -5 minecraft:water
setblock -5 67 5 minecraft:water
setblock -4 63 -8 minecraft:water
setblock -4 63 -7 minecraft:water
setblock -4 63 -6 minecraft:water
setblock -4 63 -5 minecraft:water
setblock -4 63 -4 minecraft:water
setblock -4 63 4 minecraft:water
setblock -4 63 5 minecraft:water
setblock -4 63 6 minecraft:water
setblock -4 63 7 minecraft:water
setblock -4 63 8 minecraft:water
setblock -3 63 -8 minecraft:water
setblock -3 63 -7 minecraft:water
setblock -3 63 -6 minecraft:water
setblock -3 63 -5 minecraft:water
setblock -3 63 5 minecraft:water
setblock -3 63 6 minecraft:water
setblock -3 63 7 minecraft:water
setblock -3 63 8 minecraft:water
setblock -2 63 -8 minecraft:water
setblock -2 63 -7 minecraft:water
setblock -2 63 -6 minecraft:water
setblock -2 63 6 minecraft:water
setblock -2 63 7 minecraft:water
setblock -2 63 8 minecraft:water
setblock 2 63 -8 minecraft:water
setblock 2 63 -7 minecraft:water
setblock 2 63 -6 minecraft:water
setblock 2 63 6 minecraft:water
setblock 2 63 7 minecraft:water
setblock 2 63 8 minecraft:water
setblock 3 63 -8 minecraft:water
setblock 3 63 -7 minecraft:water
setblock 3 63 -6 minecraft:water
setblock 3 63 -5 minecraft:water
setblock 3 63 5 minecraft:water
setblock 3 63 6 minecraft:water
setblock 3 63 7 minecraft:water
setblock 3 63 8 minecraft:water
setblock 4 63 -8 minecraft:water
setblock 4 63 -7 minecraft:water
setblock 4 63 -6 minecraft:water
setblock 4 63 -5 minecraft:water
setblock 4 63 -4 minecraft:water
setblock 4 63 4 minecraft:water
setblock 4 63 5 minecraft:water
setblock 4 63 6 minecraft:water
setblock 4 63 7 minecraft:water
setblock 4 63 8 minecraft:water
setblock 5 63 -7 minecraft:water
setblock 5 63 -6 minecraft:water
setblock 5 63 -4 minecraft:water
setblock 5 63 -3 minecraft:water
setblock 5 63 3 minecraft:water
setblock 5 63 4 minecraft:water
setblock 5 63 6 minecraft:water
setblock 5 63 7 minecraft:water
setblock 5 67 -5 minecraft:water
setblock 5 67 5 minecraft:water
setblock 6 63 -6 minecraft:water
setblock 6 63 -5 minecraft:water
setblock 6 63 -4 minecraft:water
setblock 6 63 -3 minecraft:water
setblock 6 63 -2 minecraft:water
setblock 6 63 2 minecraft:water
setblock 6 63 3 minecraft:water
setblock 6 63 4 minecraft:water
setblock 6 63 5 minecraft:water
setblock 6 63 6 minecraft:water
setblock 7 63 -5 minecraft:water
setblock 7 63 -4 minecraft:water
setblock 7 63 -3 minecraft:water
setblock 7 63 -2 minecraft:water
setblock 7 63 2 minecraft:water
setblock 7 63 3 minecraft:water
setblock 7 63 4 minecraft:water
setblock 7 63 5 minecraft:water
setblock 8 63 -4 minecraft:water
setblock 8 63 -3 minecraft:water
setblock 8 63 -2 minecraft:water
setblock 8 63 2 minecraft:water
setblock 8 63 3 minecraft:water
setblock 8 63 4 minecraft:water
execute if block -10 64 -8 minecraft:air run setblock -10 64 -8 minecraft:white_tulip
execute if block -10 64 8 minecraft:air run setblock -10 64 8 minecraft:blue_orchid
execute if block -9 64 -9 minecraft:air run setblock -9 64 -9 minecraft:lily_of_the_valley
execute if block -9 64 -8 minecraft:air run setblock -9 64 -8 minecraft:blue_orchid
execute if block -9 64 -7 minecraft:air run setblock -9 64 -7 minecraft:short_grass
execute if block -9 64 7 minecraft:air run setblock -9 64 7 minecraft:red_tulip
execute if block -9 64 8 minecraft:air run setblock -9 64 8 minecraft:dandelion
execute if block -9 64 9 minecraft:air run setblock -9 64 9 minecraft:azure_bluet
execute if block -8 64 -10 minecraft:air run setblock -8 64 -10 minecraft:short_grass
execute if block -8 64 -9 minecraft:air run setblock -8 64 -9 minecraft:poppy
execute if block -8 64 -7 minecraft:air run setblock -8 64 -7 minecraft:dandelion
execute if block -8 64 9 minecraft:air run setblock -8 64 9 minecraft:red_tulip
execute if block -8 64 10 minecraft:air run setblock -8 64 10 minecraft:short_grass
execute if block -7 64 -9 minecraft:air run setblock -7 64 -9 minecraft:orange_tulip
execute if block -7 64 -8 minecraft:air run setblock -7 64 -8 minecraft:dandelion
execute if block -7 64 -7 minecraft:air run setblock -7 64 -7 minecraft:short_grass
execute if block -7 64 7 minecraft:air run setblock -7 64 7 minecraft:lily_of_the_valley
execute if block -7 64 8 minecraft:air run setblock -7 64 8 minecraft:white_tulip
execute if block -7 64 9 minecraft:air run setblock -7 64 9 minecraft:azure_bluet
execute if block 7 64 -9 minecraft:air run setblock 7 64 -9 minecraft:blue_orchid
execute if block 7 64 -8 minecraft:air run setblock 7 64 -8 minecraft:red_tulip
execute if block 7 64 7 minecraft:air run setblock 7 64 7 minecraft:red_tulip
execute if block 7 64 8 minecraft:air run setblock 7 64 8 minecraft:blue_orchid
execute if block 7 64 9 minecraft:air run setblock 7 64 9 minecraft:blue_orchid
execute if block 8 64 -10 minecraft:air run setblock 8 64 -10 minecraft:short_grass
execute if block 8 64 -9 minecraft:air run setblock 8 64 -9 minecraft:poppy
execute if block 8 64 -7 minecraft:air run setblock 8 64 -7 minecraft:red_tulip
execute if block 8 64 7 minecraft:air run setblock 8 64 7 minecraft:short_grass
execute if block 8 64 9 minecraft:air run setblock 8 64 9 minecraft:cornflower
execute if block 8 64 10 minecraft:air run setblock 8 64 10 minecraft:lily_of_the_valley
execute if block 9 64 -9 minecraft:air run setblock 9 64 -9 minecraft:poppy
execute if block 9 64 -8 minecraft:air run setblock 9 64 -8 minecraft:orange_tulip
execute if block 9 64 -7 minecraft:air run setblock 9 64 -7 minecraft:red_tulip
execute if block 9 64 7 minecraft:air run setblock 9 64 7 minecraft:short_grass
execute if block 9 64 9 minecraft:air run setblock 9 64 9 minecraft:allium
execute if block 10 64 -8 minecraft:air run setblock 10 64 -8 minecraft:dandelion
execute if block 10 64 8 minecraft:air run setblock 10 64 8 minecraft:short_grass
setblock 23 62 -33 minecraft:dirt
setblock 23 62 -32 minecraft:dirt
setblock 23 62 -31 minecraft:dirt
setblock 23 62 -30 minecraft:dirt
setblock 23 62 -29 minecraft:dirt
setblock 23 62 -28 minecraft:dirt
setblock 23 62 -27 minecraft:dirt
setblock 23 63 -33 minecraft:stone
setblock 23 63 -32 minecraft:stone
setblock 23 63 -31 minecraft:mossy_cobblestone
setblock 23 63 -30 minecraft:moss_block
setblock 23 63 -29 minecraft:moss_block
setblock 23 63 -28 minecraft:moss_block
setblock 23 63 -27 minecraft:stone
setblock 24 62 -34 minecraft:dirt
setblock 24 62 -33 minecraft:dirt
setblock 24 62 -32 minecraft:clay
setblock 24 62 -31 minecraft:sand
setblock 24 62 -30 minecraft:clay
setblock 24 62 -29 minecraft:sand
setblock 24 62 -28 minecraft:sand
setblock 24 62 -27 minecraft:dirt
setblock 24 62 -26 minecraft:dirt
setblock 24 62 -25 minecraft:dirt
setblock 24 63 -34 minecraft:grass_block
setblock 24 63 -33 minecraft:moss_block
setblock 24 63 -27 minecraft:stone
setblock 24 63 -26 minecraft:moss_block
setblock 24 63 -25 minecraft:grass_block
setblock 25 62 -34 minecraft:clay
setblock 25 62 -33 minecraft:sand
setblock 25 62 -32 minecraft:sand
setblock 25 62 -31 minecraft:sand
setblock 25 62 -30 minecraft:clay
setblock 25 62 -29 minecraft:clay
setblock 25 62 -28 minecraft:sand
setblock 25 62 -27 minecraft:sand
setblock 25 62 -26 minecraft:clay
setblock 25 62 -25 minecraft:dirt
setblock 25 62 -24 minecraft:dirt
setblock 25 63 -25 minecraft:mossy_cobblestone
setblock 25 63 -24 minecraft:grass_block
setblock 26 61 -32 minecraft:dirt
setblock 26 61 -31 minecraft:dirt
setblock 26 61 -30 minecraft:dirt
setblock 26 61 -29 minecraft:dirt
setblock 26 61 -28 minecraft:dirt
setblock 26 62 -34 minecraft:clay
setblock 26 62 -33 minecraft:sand
setblock 26 62 -32 minecraft:clay
setblock 26 62 -31 minecraft:clay
setblock 26 62 -30 minecraft:clay
setblock 26 62 -29 minecraft:clay
setblock 26 62 -28 minecraft:clay
setblock 26 62 -27 minecraft:sand
setblock 26 62 -26 minecraft:sand
setblock 26 62 -25 minecraft:sand
setblock 26 62 -24 minecraft:dirt
setblock 26 63 -24 minecraft:mossy_cobblestone
setblock 27 61 -33 minecraft:dirt
setblock 27 61 -32 minecraft:dirt
setblock 27 61 -31 minecraft:clay
setblock 27 61 -30 minecraft:clay
setblock 27 61 -29 minecraft:clay
setblock 27 61 -28 minecraft:dirt
setblock 27 61 -27 minecraft:dirt
setblock 27 62 -34 minecraft:sand
setblock 27 62 -33 minecraft:sand
setblock 27 62 -32 minecraft:clay
setblock 27 62 -28 minecraft:clay
setblock 27 62 -27 minecraft:sand
setblock 27 62 -26 minecraft:clay
setblock 27 62 -25 minecraft:sand
setblock 27 62 -24 minecraft:dirt
setblock 27 62 -23 minecraft:dirt
setblock 27 63 -24 minecraft:grass_block
setblock 27 63 -23 minecraft:grass_block
setblock 27 89 -28 minecraft:dirt
setblock 27 90 -28 minecraft:grass_block
setblock 28 61 -34 minecraft:dirt
setblock 28 61 -33 minecraft:dirt
setblock 28 61 -32 minecraft:clay
setblock 28 61 -31 minecraft:clay
setblock 28 61 -30 minecraft:clay
setblock 28 61 -29 minecraft:clay
setblock 28 61 -28 minecraft:clay
setblock 28 61 -27 minecraft:dirt
setblock 28 61 -26 minecraft:dirt
setblock 28 62 -34 minecraft:sand
setblock 28 62 -33 minecraft:sand
setblock 28 62 -27 minecraft:sand
setblock 28 62 -26 minecraft:clay
setblock 28 62 -25 minecraft:clay
setblock 28 62 -24 minecraft:sand
setblock 28 62 -23 minecraft:dirt
setblock 28 63 -23 minecraft:grass_block
setblock 28 89 -28 minecraft:dirt
setblock 28 89 -27 minecraft:dirt
setblock 28 90 -28 minecraft:grass_block
setblock 28 90 -27 minecraft:grass_block
setblock 29 61 -34 minecraft:dirt
setblock 29 61 -33 minecraft:clay
setblock 29 61 -32 minecraft:clay
setblock 29 61 -31 minecraft:clay
setblock 29 61 -30 minecraft:clay
setblock 29 61 -29 minecraft:clay
setblock 29 61 -28 minecraft:clay
setblock 29 61 -27 minecraft:clay
setblock 29 61 -26 minecraft:dirt
setblock 29 62 -34 minecraft:sand
setblock 29 62 -26 minecraft:sand
setblock 29 62 -25 minecraft:clay
setblock 29 62 -24 minecraft:sand
setblock 29 62 -23 minecraft:dirt
setblock 29 63 -23 minecraft:mossy_cobblestone
setblock 30 61 -34 minecraft:dirt
setblock 30 61 -33 minecraft:clay
setblock 30 61 -32 minecraft:clay
setblock 30 61 -31 minecraft:clay
setblock 30 61 -30 minecraft:clay
setblock 30 61 -29 minecraft:clay
setblock 30 61 -28 minecraft:clay
setblock 30 61 -27 minecraft:clay
setblock 30 61 -26 minecraft:dirt
setblock 30 62 -34 minecraft:sand
setblock 30 62 -26 minecraft:sand
setblock 30 62 -25 minecraft:clay
setblock 30 62 -24 minecraft:sand
setblock 30 62 -23 minecraft:dirt
setblock 30 63 -23 minecraft:mossy_cobblestone
setblock 31 61 -34 minecraft:dirt
setblock 31 61 -33 minecraft:clay
setblock 31 61 -32 minecraft:clay
setblock 31 61 -31 minecraft:clay
setblock 31 61 -30 minecraft:clay
setblock 31 61 -29 minecraft:clay
setblock 31 61 -28 minecraft:clay
setblock 31 61 -27 minecraft:clay
setblock 31 61 -26 minecraft:dirt
setblock 31 62 -34 minecraft:sand
setblock 31 62 -26 minecraft:sand
setblock 31 62 -25 minecraft:sand
setblock 31 62 -24 minecraft:clay
setblock 31 62 -23 minecraft:dirt
setblock 31 63 -23 minecraft:moss_block
setblock 32 61 -34 minecraft:dirt
setblock 32 61 -33 minecraft:dirt
setblock 32 61 -32 minecraft:clay
setblock 32 61 -31 minecraft:clay
setblock 32 61 -30 minecraft:clay
setblock 32 61 -29 minecraft:clay
setblock 32 61 -28 minecraft:clay
setblock 32 61 -27 minecraft:dirt
setblock 32 61 -26 minecraft:dirt
setblock 32 62 -34 minecraft:clay
setblock 32 62 -33 minecraft:sand
setblock 32 62 -27 minecraft:sand
setblock 32 62 -26 minecraft:sand
setblock 32 62 -25 minecraft:clay
setblock 32 62 -24 minecraft:sand
setblock 32 62 -23 minecraft:dirt
setblock 32 63 -23 minecraft:mossy_cobblestone
setblock 33 61 -33 minecraft:dirt
setblock 33 61 -32 minecraft:dirt
setblock 33 61 -31 minecraft:clay
setblock 33 61 -30 minecraft:clay
setblock 33 61 -29 minecraft:clay
setblock 33 61 -28 minecraft:dirt
setblock 33 61 -27 minecraft:dirt
setblock 33 62 -34 minecraft:sand
setblock 33 62 -33 minecraft:sand
setblock 33 62 -32 minecraft:sand
setblock 33 62 -28 minecraft:sand
setblock 33 62 -27 minecraft:sand
setblock 33 62 -26 minecraft:sand
setblock 33 62 -25 minecraft:clay
setblock 33 62 -24 minecraft:dirt
setblock 33 62 -23 minecraft:dirt
setblock 33 63 -24 minecraft:grass_block
setblock 33 63 -23 minecraft:mossy_cobblestone
setblock 34 61 -32 minecraft:dirt
setblock 34 61 -31 minecraft:dirt
setblock 34 61 -30 minecraft:dirt
setblock 34 61 -29 minecraft:dirt
setblock 34 61 -28 minecraft:dirt
setblock 34 62 -34 minecraft:clay
setblock 34 62 -33 minecraft:sand
setblock 34 62 -32 minecraft:clay
setblock 34 62 -31 minecraft:sand
setblock 34 62 -30 minecraft:clay
setblock 34 62 -29 minecraft:clay
setblock 34 62 -28 minecraft:clay
setblock 34 62 -27 minecraft:clay
setblock 34 62 -26 minecraft:clay
setblock 34 62 -25 minecraft:sand
setblock 34 62 -24 minecraft:dirt
setblock 34 63 -24 minecraft:moss_block
execute unless block 24 64 -32 minecraft:air unless block 24 64 -32 minecraft:water run setblock 24 64 -32 minecraft:air
execute unless block 24 64 -31 minecraft:air unless block 24 64 -31 minecraft:water run setblock 24 64 -31 minecraft:air
execute unless block 24 64 -29 minecraft:air unless block 24 64 -29 minecraft:water run setblock 24 64 -29 minecraft:air
execute unless block 24 64 -28 minecraft:air unless block 24 64 -28 minecraft:water run setblock 24 64 -28 minecraft:air
execute unless block 25 64 -33 minecraft:air unless block 25 64 -33 minecraft:water run setblock 25 64 -33 minecraft:air
execute unless block 25 64 -32 minecraft:air unless block 25 64 -32 minecraft:water run setblock 25 64 -32 minecraft:air
execute unless block 25 64 -31 minecraft:air unless block 25 64 -31 minecraft:water run setblock 25 64 -31 minecraft:air
execute unless block 25 64 -30 minecraft:air unless block 25 64 -30 minecraft:water run setblock 25 64 -30 minecraft:air
execute unless block 25 64 -29 minecraft:air unless block 25 64 -29 minecraft:water run setblock 25 64 -29 minecraft:air
execute unless block 25 64 -28 minecraft:air unless block 25 64 -28 minecraft:water run setblock 25 64 -28 minecraft:air
execute unless block 25 64 -27 minecraft:air unless block 25 64 -27 minecraft:water run setblock 25 64 -27 minecraft:air
execute unless block 25 64 -26 minecraft:air unless block 25 64 -26 minecraft:water run setblock 25 64 -26 minecraft:air
execute unless block 26 64 -33 minecraft:air unless block 26 64 -33 minecraft:water run setblock 26 64 -33 minecraft:air
execute unless block 26 64 -32 minecraft:air unless block 26 64 -32 minecraft:water run setblock 26 64 -32 minecraft:air
execute unless block 26 64 -31 minecraft:air unless block 26 64 -31 minecraft:water run setblock 26 64 -31 minecraft:air
execute unless block 26 64 -30 minecraft:air unless block 26 64 -30 minecraft:water run setblock 26 64 -30 minecraft:air
execute unless block 26 64 -29 minecraft:air unless block 26 64 -29 minecraft:water run setblock 26 64 -29 minecraft:air
execute unless block 26 64 -27 minecraft:air unless block 26 64 -27 minecraft:water run setblock 26 64 -27 minecraft:air
execute unless block 26 65 -27 minecraft:air unless block 26 65 -27 minecraft:water run setblock 26 65 -27 minecraft:air
execute unless block 26 66 -27 minecraft:air unless block 26 66 -27 minecraft:water run setblock 26 66 -27 minecraft:air
execute unless block 26 67 -27 minecraft:air unless block 26 67 -27 minecraft:water run setblock 26 67 -27 minecraft:air
execute unless block 26 68 -27 minecraft:air unless block 26 68 -27 minecraft:water run setblock 26 68 -27 minecraft:air
execute unless block 26 69 -27 minecraft:air unless block 26 69 -27 minecraft:water run setblock 26 69 -27 minecraft:air
execute unless block 26 70 -27 minecraft:air unless block 26 70 -27 minecraft:water run setblock 26 70 -27 minecraft:air
execute unless block 26 71 -27 minecraft:air unless block 26 71 -27 minecraft:water run setblock 26 71 -27 minecraft:air
execute unless block 26 72 -27 minecraft:air unless block 26 72 -27 minecraft:water run setblock 26 72 -27 minecraft:air
execute unless block 26 73 -27 minecraft:air unless block 26 73 -27 minecraft:water run setblock 26 73 -27 minecraft:air
execute unless block 26 74 -27 minecraft:air unless block 26 74 -27 minecraft:water run setblock 26 74 -27 minecraft:air
execute unless block 26 75 -27 minecraft:air unless block 26 75 -27 minecraft:water run setblock 26 75 -27 minecraft:air
execute unless block 26 76 -27 minecraft:air unless block 26 76 -27 minecraft:water run setblock 26 76 -27 minecraft:air
execute unless block 26 77 -27 minecraft:air unless block 26 77 -27 minecraft:water run setblock 26 77 -27 minecraft:air
execute unless block 26 78 -27 minecraft:air unless block 26 78 -27 minecraft:water run setblock 26 78 -27 minecraft:air
execute unless block 26 79 -27 minecraft:air unless block 26 79 -27 minecraft:water run setblock 26 79 -27 minecraft:air
execute unless block 26 80 -27 minecraft:air unless block 26 80 -27 minecraft:water run setblock 26 80 -27 minecraft:air
execute unless block 26 81 -27 minecraft:air unless block 26 81 -27 minecraft:water run setblock 26 81 -27 minecraft:air
execute unless block 26 82 -27 minecraft:air unless block 26 82 -27 minecraft:water run setblock 26 82 -27 minecraft:air
execute unless block 26 83 -27 minecraft:air unless block 26 83 -27 minecraft:water run setblock 26 83 -27 minecraft:air
execute unless block 26 84 -27 minecraft:air unless block 26 84 -27 minecraft:water run setblock 26 84 -27 minecraft:air
execute unless block 26 85 -27 minecraft:air unless block 26 85 -27 minecraft:water run setblock 26 85 -27 minecraft:air
execute unless block 26 86 -27 minecraft:air unless block 26 86 -27 minecraft:water run setblock 26 86 -27 minecraft:air
execute unless block 26 87 -27 minecraft:air unless block 26 87 -27 minecraft:water run setblock 26 87 -27 minecraft:air
execute unless block 26 88 -27 minecraft:air unless block 26 88 -27 minecraft:water run setblock 26 88 -27 minecraft:air
execute unless block 26 89 -27 minecraft:air unless block 26 89 -27 minecraft:water run setblock 26 89 -27 minecraft:air
execute unless block 26 90 -27 minecraft:air unless block 26 90 -27 minecraft:water run setblock 26 90 -27 minecraft:air
execute unless block 27 64 -33 minecraft:air unless block 27 64 -33 minecraft:water run setblock 27 64 -33 minecraft:air
execute unless block 27 64 -32 minecraft:air unless block 27 64 -32 minecraft:water run setblock 27 64 -32 minecraft:air
execute unless block 27 64 -31 minecraft:air unless block 27 64 -31 minecraft:water run setblock 27 64 -31 minecraft:air
execute unless block 27 64 -30 minecraft:air unless block 27 64 -30 minecraft:water run setblock 27 64 -30 minecraft:air
execute unless block 27 64 -29 minecraft:air unless block 27 64 -29 minecraft:water run setblock 27 64 -29 minecraft:air
execute unless block 27 64 -28 minecraft:air unless block 27 64 -28 minecraft:water run setblock 27 64 -28 minecraft:air
execute unless block 27 64 -27 minecraft:air unless block 27 64 -27 minecraft:water run setblock 27 64 -27 minecraft:air
execute unless block 27 64 -26 minecraft:air unless block 27 64 -26 minecraft:water run setblock 27 64 -26 minecraft:air
execute unless block 27 65 -27 minecraft:air unless block 27 65 -27 minecraft:water run setblock 27 65 -27 minecraft:air
execute unless block 27 65 -26 minecraft:air unless block 27 65 -26 minecraft:water run setblock 27 65 -26 minecraft:air
execute unless block 27 66 -27 minecraft:air unless block 27 66 -27 minecraft:water run setblock 27 66 -27 minecraft:air
execute unless block 27 66 -26 minecraft:air unless block 27 66 -26 minecraft:water run setblock 27 66 -26 minecraft:air
execute unless block 27 67 -27 minecraft:air unless block 27 67 -27 minecraft:water run setblock 27 67 -27 minecraft:air
execute unless block 27 67 -26 minecraft:air unless block 27 67 -26 minecraft:water run setblock 27 67 -26 minecraft:air
execute unless block 27 68 -27 minecraft:air unless block 27 68 -27 minecraft:water run setblock 27 68 -27 minecraft:air
execute unless block 27 68 -26 minecraft:air unless block 27 68 -26 minecraft:water run setblock 27 68 -26 minecraft:air
execute unless block 27 69 -27 minecraft:air unless block 27 69 -27 minecraft:water run setblock 27 69 -27 minecraft:air
execute unless block 27 69 -26 minecraft:air unless block 27 69 -26 minecraft:water run setblock 27 69 -26 minecraft:air
execute unless block 27 70 -27 minecraft:air unless block 27 70 -27 minecraft:water run setblock 27 70 -27 minecraft:air
execute unless block 27 70 -26 minecraft:air unless block 27 70 -26 minecraft:water run setblock 27 70 -26 minecraft:air
execute unless block 27 71 -27 minecraft:air unless block 27 71 -27 minecraft:water run setblock 27 71 -27 minecraft:air
execute unless block 27 71 -26 minecraft:air unless block 27 71 -26 minecraft:water run setblock 27 71 -26 minecraft:air
execute unless block 27 72 -27 minecraft:air unless block 27 72 -27 minecraft:water run setblock 27 72 -27 minecraft:air
execute unless block 27 72 -26 minecraft:air unless block 27 72 -26 minecraft:water run setblock 27 72 -26 minecraft:air
execute unless block 27 73 -27 minecraft:air unless block 27 73 -27 minecraft:water run setblock 27 73 -27 minecraft:air
execute unless block 27 73 -26 minecraft:air unless block 27 73 -26 minecraft:water run setblock 27 73 -26 minecraft:air
execute unless block 27 74 -27 minecraft:air unless block 27 74 -27 minecraft:water run setblock 27 74 -27 minecraft:air
execute unless block 27 74 -26 minecraft:air unless block 27 74 -26 minecraft:water run setblock 27 74 -26 minecraft:air
execute unless block 27 75 -27 minecraft:air unless block 27 75 -27 minecraft:water run setblock 27 75 -27 minecraft:air
execute unless block 27 75 -26 minecraft:air unless block 27 75 -26 minecraft:water run setblock 27 75 -26 minecraft:air
execute unless block 27 76 -27 minecraft:air unless block 27 76 -27 minecraft:water run setblock 27 76 -27 minecraft:air
execute unless block 27 76 -26 minecraft:air unless block 27 76 -26 minecraft:water run setblock 27 76 -26 minecraft:air
execute unless block 27 77 -27 minecraft:air unless block 27 77 -27 minecraft:water run setblock 27 77 -27 minecraft:air
execute unless block 27 77 -26 minecraft:air unless block 27 77 -26 minecraft:water run setblock 27 77 -26 minecraft:air
execute unless block 27 78 -27 minecraft:air unless block 27 78 -27 minecraft:water run setblock 27 78 -27 minecraft:air
execute unless block 27 78 -26 minecraft:air unless block 27 78 -26 minecraft:water run setblock 27 78 -26 minecraft:air
execute unless block 27 79 -27 minecraft:air unless block 27 79 -27 minecraft:water run setblock 27 79 -27 minecraft:air
execute unless block 27 79 -26 minecraft:air unless block 27 79 -26 minecraft:water run setblock 27 79 -26 minecraft:air
execute unless block 27 80 -27 minecraft:air unless block 27 80 -27 minecraft:water run setblock 27 80 -27 minecraft:air
execute unless block 27 80 -26 minecraft:air unless block 27 80 -26 minecraft:water run setblock 27 80 -26 minecraft:air
execute unless block 27 81 -27 minecraft:air unless block 27 81 -27 minecraft:water run setblock 27 81 -27 minecraft:air
execute unless block 27 81 -26 minecraft:air unless block 27 81 -26 minecraft:water run setblock 27 81 -26 minecraft:air
execute unless block 27 82 -27 minecraft:air unless block 27 82 -27 minecraft:water run setblock 27 82 -27 minecraft:air
execute unless block 27 82 -26 minecraft:air unless block 27 82 -26 minecraft:water run setblock 27 82 -26 minecraft:air
execute unless block 27 83 -27 minecraft:air unless block 27 83 -27 minecraft:water run setblock 27 83 -27 minecraft:air
execute unless block 27 83 -26 minecraft:air unless block 27 83 -26 minecraft:water run setblock 27 83 -26 minecraft:air
execute unless block 27 84 -27 minecraft:air unless block 27 84 -27 minecraft:water run setblock 27 84 -27 minecraft:air
execute unless block 27 84 -26 minecraft:air unless block 27 84 -26 minecraft:water run setblock 27 84 -26 minecraft:air
execute unless block 27 85 -27 minecraft:air unless block 27 85 -27 minecraft:water run setblock 27 85 -27 minecraft:air
execute unless block 27 85 -26 minecraft:air unless block 27 85 -26 minecraft:water run setblock 27 85 -26 minecraft:air
execute unless block 27 86 -27 minecraft:air unless block 27 86 -27 minecraft:water run setblock 27 86 -27 minecraft:air
execute unless block 27 86 -26 minecraft:air unless block 27 86 -26 minecraft:water run setblock 27 86 -26 minecraft:air
execute unless block 27 87 -27 minecraft:air unless block 27 87 -27 minecraft:water run setblock 27 87 -27 minecraft:air
execute unless block 27 87 -26 minecraft:air unless block 27 87 -26 minecraft:water run setblock 27 87 -26 minecraft:air
execute unless block 27 88 -27 minecraft:air unless block 27 88 -27 minecraft:water run setblock 27 88 -27 minecraft:air
execute unless block 27 88 -26 minecraft:air unless block 27 88 -26 minecraft:water run setblock 27 88 -26 minecraft:air
execute unless block 27 89 -27 minecraft:air unless block 27 89 -27 minecraft:water run setblock 27 89 -27 minecraft:air
execute unless block 27 89 -26 minecraft:air unless block 27 89 -26 minecraft:water run setblock 27 89 -26 minecraft:air
execute unless block 27 90 -26 minecraft:air unless block 27 90 -26 minecraft:water run setblock 27 90 -26 minecraft:air
execute unless block 27 91 -27 minecraft:air unless block 27 91 -27 minecraft:water run setblock 27 91 -27 minecraft:air
execute unless block 28 64 -33 minecraft:air unless block 28 64 -33 minecraft:water run setblock 28 64 -33 minecraft:air
execute unless block 28 64 -32 minecraft:air unless block 28 64 -32 minecraft:water run setblock 28 64 -32 minecraft:air
execute unless block 28 64 -31 minecraft:air unless block 28 64 -31 minecraft:water run setblock 28 64 -31 minecraft:air
execute unless block 28 64 -30 minecraft:air unless block 28 64 -30 minecraft:water run setblock 28 64 -30 minecraft:air
execute unless block 28 64 -29 minecraft:air unless block 28 64 -29 minecraft:water run setblock 28 64 -29 minecraft:air
execute unless block 28 64 -28 minecraft:air unless block 28 64 -28 minecraft:water run setblock 28 64 -28 minecraft:air
execute unless block 28 64 -27 minecraft:air unless block 28 64 -27 minecraft:water run setblock 28 64 -27 minecraft:air
execute unless block 28 64 -25 minecraft:air unless block 28 64 -25 minecraft:water run setblock 28 64 -25 minecraft:air
execute unless block 29 64 -33 minecraft:air unless block 29 64 -33 minecraft:water run setblock 29 64 -33 minecraft:air
execute unless block 29 64 -31 minecraft:air unless block 29 64 -31 minecraft:water run setblock 29 64 -31 minecraft:air
execute unless block 29 64 -30 minecraft:air unless block 29 64 -30 minecraft:water run setblock 29 64 -30 minecraft:air
execute unless block 29 64 -29 minecraft:air unless block 29 64 -29 minecraft:water run setblock 29 64 -29 minecraft:air
execute unless block 29 64 -28 minecraft:air unless block 29 64 -28 minecraft:water run setblock 29 64 -28 minecraft:air
execute unless block 29 64 -27 minecraft:air unless block 29 64 -27 minecraft:water run setblock 29 64 -27 minecraft:air
execute unless block 29 64 -26 minecraft:air unless block 29 64 -26 minecraft:water run setblock 29 64 -26 minecraft:air
execute unless block 29 64 -25 minecraft:air unless block 29 64 -25 minecraft:water run setblock 29 64 -25 minecraft:air
execute unless block 29 64 -24 minecraft:air unless block 29 64 -24 minecraft:water run setblock 29 64 -24 minecraft:air
execute unless block 30 64 -33 minecraft:air unless block 30 64 -33 minecraft:water run setblock 30 64 -33 minecraft:air
execute unless block 30 64 -32 minecraft:air unless block 30 64 -32 minecraft:water run setblock 30 64 -32 minecraft:air
execute unless block 30 64 -31 minecraft:air unless block 30 64 -31 minecraft:water run setblock 30 64 -31 minecraft:air
execute unless block 30 64 -30 minecraft:air unless block 30 64 -30 minecraft:water run setblock 30 64 -30 minecraft:air
execute unless block 30 64 -29 minecraft:air unless block 30 64 -29 minecraft:water run setblock 30 64 -29 minecraft:air
execute unless block 30 64 -28 minecraft:air unless block 30 64 -28 minecraft:water run setblock 30 64 -28 minecraft:air
execute unless block 30 64 -27 minecraft:air unless block 30 64 -27 minecraft:water run setblock 30 64 -27 minecraft:air
execute unless block 30 64 -26 minecraft:air unless block 30 64 -26 minecraft:water run setblock 30 64 -26 minecraft:air
execute unless block 30 64 -25 minecraft:air unless block 30 64 -25 minecraft:water run setblock 30 64 -25 minecraft:air
execute unless block 30 64 -24 minecraft:air unless block 30 64 -24 minecraft:water run setblock 30 64 -24 minecraft:air
execute unless block 31 64 -33 minecraft:air unless block 31 64 -33 minecraft:water run setblock 31 64 -33 minecraft:air
execute unless block 31 64 -32 minecraft:air unless block 31 64 -32 minecraft:water run setblock 31 64 -32 minecraft:air
execute unless block 31 64 -31 minecraft:air unless block 31 64 -31 minecraft:water run setblock 31 64 -31 minecraft:air
execute unless block 31 64 -30 minecraft:air unless block 31 64 -30 minecraft:water run setblock 31 64 -30 minecraft:air
execute unless block 31 64 -29 minecraft:air unless block 31 64 -29 minecraft:water run setblock 31 64 -29 minecraft:air
execute unless block 31 64 -28 minecraft:air unless block 31 64 -28 minecraft:water run setblock 31 64 -28 minecraft:air
execute unless block 31 64 -27 minecraft:air unless block 31 64 -27 minecraft:water run setblock 31 64 -27 minecraft:air
execute unless block 31 64 -26 minecraft:air unless block 31 64 -26 minecraft:water run setblock 31 64 -26 minecraft:air
execute unless block 31 64 -25 minecraft:air unless block 31 64 -25 minecraft:water run setblock 31 64 -25 minecraft:air
execute unless block 31 64 -24 minecraft:air unless block 31 64 -24 minecraft:water run setblock 31 64 -24 minecraft:air
execute unless block 32 64 -33 minecraft:air unless block 32 64 -33 minecraft:water run setblock 32 64 -33 minecraft:air
execute unless block 32 64 -32 minecraft:air unless block 32 64 -32 minecraft:water run setblock 32 64 -32 minecraft:air
execute unless block 32 64 -31 minecraft:air unless block 32 64 -31 minecraft:water run setblock 32 64 -31 minecraft:air
execute unless block 32 64 -30 minecraft:air unless block 32 64 -30 minecraft:water run setblock 32 64 -30 minecraft:air
execute unless block 32 64 -29 minecraft:air unless block 32 64 -29 minecraft:water run setblock 32 64 -29 minecraft:air
execute unless block 32 64 -28 minecraft:air unless block 32 64 -28 minecraft:water run setblock 32 64 -28 minecraft:air
execute unless block 32 64 -27 minecraft:air unless block 32 64 -27 minecraft:water run setblock 32 64 -27 minecraft:air
execute unless block 32 64 -26 minecraft:air unless block 32 64 -26 minecraft:water run setblock 32 64 -26 minecraft:air
execute unless block 32 64 -24 minecraft:air unless block 32 64 -24 minecraft:water run setblock 32 64 -24 minecraft:air
execute unless block 33 64 -31 minecraft:air unless block 33 64 -31 minecraft:water run setblock 33 64 -31 minecraft:air
execute unless block 33 64 -30 minecraft:air unless block 33 64 -30 minecraft:water run setblock 33 64 -30 minecraft:air
execute unless block 33 64 -29 minecraft:air unless block 33 64 -29 minecraft:water run setblock 33 64 -29 minecraft:air
execute unless block 33 64 -28 minecraft:air unless block 33 64 -28 minecraft:water run setblock 33 64 -28 minecraft:air
execute unless block 33 64 -27 minecraft:air unless block 33 64 -27 minecraft:water run setblock 33 64 -27 minecraft:air
execute unless block 33 64 -26 minecraft:air unless block 33 64 -26 minecraft:water run setblock 33 64 -26 minecraft:air
execute unless block 33 64 -25 minecraft:air unless block 33 64 -25 minecraft:water run setblock 33 64 -25 minecraft:air
fill 22 61 -35 35 91 -22 minecraft:air replace minecraft:lily_pad
fill 22 61 -35 35 91 -22 minecraft:air replace minecraft:water
setblock 24 63 -32 minecraft:water
setblock 24 63 -31 minecraft:water
setblock 24 63 -30 minecraft:water
setblock 24 63 -29 minecraft:water
setblock 24 63 -28 minecraft:water
execute unless block 25 63 -34 minecraft:ice run setblock 25 63 -34 minecraft:water
setblock 25 63 -33 minecraft:water
setblock 25 63 -32 minecraft:water
setblock 25 63 -31 minecraft:water
setblock 25 63 -30 minecraft:water
setblock 25 63 -29 minecraft:water
setblock 25 63 -28 minecraft:water
setblock 25 63 -27 minecraft:water
setblock 25 63 -26 minecraft:water
execute unless block 26 63 -35 minecraft:ice run setblock 26 63 -35 minecraft:water
execute unless block 26 63 -34 minecraft:ice run setblock 26 63 -34 minecraft:water
setblock 26 63 -33 minecraft:water
setblock 26 63 -32 minecraft:water
setblock 26 63 -31 minecraft:water
setblock 26 63 -30 minecraft:water
setblock 26 63 -29 minecraft:water
setblock 26 63 -28 minecraft:water
setblock 26 63 -27 minecraft:water
setblock 26 63 -26 minecraft:water
setblock 26 63 -25 minecraft:water
setblock 27 62 -31 minecraft:water
setblock 27 62 -30 minecraft:water
setblock 27 62 -29 minecraft:water
execute unless block 27 63 -35 minecraft:ice run setblock 27 63 -35 minecraft:water
execute unless block 27 63 -34 minecraft:ice run setblock 27 63 -34 minecraft:water
setblock 27 63 -33 minecraft:water
setblock 27 63 -32 minecraft:water
setblock 27 63 -31 minecraft:water
setblock 27 63 -30 minecraft:water
setblock 27 63 -29 minecraft:water
setblock 27 63 -28 minecraft:water
setblock 27 63 -27 minecraft:water
setblock 27 63 -26 minecraft:water
setblock 27 63 -25 minecraft:water
setblock 27 90 -27 minecraft:water
setblock 28 62 -32 minecraft:water
setblock 28 62 -31 minecraft:water
setblock 28 62 -30 minecraft:water
setblock 28 62 -29 minecraft:water
setblock 28 62 -28 minecraft:water
execute unless block 28 63 -35 minecraft:ice run setblock 28 63 -35 minecraft:water
setblock 28 63 -34 minecraft:water
setblock 28 63 -33 minecraft:water
setblock 28 63 -32 minecraft:water
setblock 28 63 -31 minecraft:water
setblock 28 63 -30 minecraft:water
setblock 28 63 -29 minecraft:water
setblock 28 63 -28 minecraft:water
setblock 28 63 -27 minecraft:water
setblock 28 63 -26 minecraft:water
setblock 28 63 -25 minecraft:water
setblock 28 63 -24 minecraft:water
setblock 29 62 -33 minecraft:water
setblock 29 62 -32 minecraft:water
setblock 29 62 -31 minecraft:water
setblock 29 62 -30 minecraft:water
setblock 29 62 -29 minecraft:water
setblock 29 62 -28 minecraft:water
setblock 29 62 -27 minecraft:water
execute unless block 29 63 -35 minecraft:ice run setblock 29 63 -35 minecraft:water
execute unless block 29 63 -34 minecraft:ice run setblock 29 63 -34 minecraft:water
setblock 29 63 -33 minecraft:water
setblock 29 63 -32 minecraft:water
setblock 29 63 -31 minecraft:water
setblock 29 63 -30 minecraft:water
setblock 29 63 -29 minecraft:water
setblock 29 63 -28 minecraft:water
setblock 29 63 -27 minecraft:water
setblock 29 63 -26 minecraft:water
setblock 29 63 -25 minecraft:water
setblock 29 63 -24 minecraft:water
setblock 30 62 -33 minecraft:water
setblock 30 62 -32 minecraft:water
setblock 30 62 -31 minecraft:water
setblock 30 62 -30 minecraft:water
setblock 30 62 -29 minecraft:water
setblock 30 62 -28 minecraft:water
setblock 30 62 -27 minecraft:water
execute unless block 30 63 -35 minecraft:ice run setblock 30 63 -35 minecraft:water
setblock 30 63 -34 minecraft:water
setblock 30 63 -33 minecraft:water
setblock 30 63 -32 minecraft:water
setblock 30 63 -31 minecraft:water
setblock 30 63 -30 minecraft:water
setblock 30 63 -29 minecraft:water
setblock 30 63 -28 minecraft:water
setblock 30 63 -27 minecraft:water
setblock 30 63 -26 minecraft:water
setblock 30 63 -25 minecraft:water
setblock 30 63 -24 minecraft:water
setblock 31 62 -33 minecraft:water
setblock 31 62 -32 minecraft:water
setblock 31 62 -31 minecraft:water
setblock 31 62 -30 minecraft:water
setblock 31 62 -29 minecraft:water
setblock 31 62 -28 minecraft:water
setblock 31 62 -27 minecraft:water
execute unless block 31 63 -35 minecraft:ice run setblock 31 63 -35 minecraft:water
execute unless block 31 63 -34 minecraft:ice run setblock 31 63 -34 minecraft:water
setblock 31 63 -33 minecraft:water
setblock 31 63 -32 minecraft:water
setblock 31 63 -31 minecraft:water
setblock 31 63 -30 minecraft:water
setblock 31 63 -29 minecraft:water
setblock 31 63 -28 minecraft:water
setblock 31 63 -27 minecraft:water
setblock 31 63 -26 minecraft:water
setblock 31 63 -25 minecraft:water
setblock 31 63 -24 minecraft:water
setblock 32 62 -32 minecraft:water
setblock 32 62 -31 minecraft:water
setblock 32 62 -30 minecraft:water
setblock 32 62 -29 minecraft:water
setblock 32 62 -28 minecraft:water
execute unless block 32 63 -35 minecraft:ice run setblock 32 63 -35 minecraft:water
execute unless block 32 63 -34 minecraft:ice run setblock 32 63 -34 minecraft:water
setblock 32 63 -33 minecraft:water
setblock 32 63 -32 minecraft:water
setblock 32 63 -31 minecraft:water
setblock 32 63 -30 minecraft:water
setblock 32 63 -29 minecraft:water
setblock 32 63 -28 minecraft:water
setblock 32 63 -27 minecraft:water
setblock 32 63 -26 minecraft:water
setblock 32 63 -25 minecraft:water
setblock 32 63 -24 minecraft:water
setblock 33 62 -31 minecraft:water
setblock 33 62 -30 minecraft:water
setblock 33 62 -29 minecraft:water
execute unless block 33 63 -35 minecraft:ice run setblock 33 63 -35 minecraft:water
execute unless block 33 63 -34 minecraft:ice run setblock 33 63 -34 minecraft:water
setblock 33 63 -33 minecraft:water
setblock 33 63 -32 minecraft:water
setblock 33 63 -31 minecraft:water
setblock 33 63 -30 minecraft:water
setblock 33 63 -29 minecraft:water
setblock 33 63 -28 minecraft:water
setblock 33 63 -27 minecraft:water
setblock 33 63 -26 minecraft:water
setblock 33 63 -25 minecraft:water
execute unless block 34 63 -35 minecraft:ice run setblock 34 63 -35 minecraft:water
execute unless block 34 63 -34 minecraft:ice run setblock 34 63 -34 minecraft:water
execute unless block 34 63 -33 minecraft:ice run setblock 34 63 -33 minecraft:water
execute unless block 34 63 -32 minecraft:ice run setblock 34 63 -32 minecraft:water
execute unless block 34 63 -31 minecraft:ice run setblock 34 63 -31 minecraft:water
setblock 34 63 -30 minecraft:water
execute unless block 34 63 -29 minecraft:ice run setblock 34 63 -29 minecraft:water
execute unless block 34 63 -28 minecraft:ice run setblock 34 63 -28 minecraft:water
execute unless block 34 63 -27 minecraft:ice run setblock 34 63 -27 minecraft:water
execute unless block 34 63 -26 minecraft:ice run setblock 34 63 -26 minecraft:water
setblock 34 63 -25 minecraft:water
setblock 35 63 -34 minecraft:water
execute unless block 35 63 -33 minecraft:ice run setblock 35 63 -33 minecraft:water
execute unless block 35 63 -32 minecraft:ice run setblock 35 63 -32 minecraft:water
setblock 35 63 -31 minecraft:water
execute unless block 35 63 -30 minecraft:ice run setblock 35 63 -30 minecraft:water
execute unless block 35 63 -29 minecraft:ice run setblock 35 63 -29 minecraft:water
execute unless block 35 63 -28 minecraft:ice run setblock 35 63 -28 minecraft:water
execute unless block 35 63 -27 minecraft:ice run setblock 35 63 -27 minecraft:water
execute unless block 35 63 -26 minecraft:ice run setblock 35 63 -26 minecraft:water
execute if block 22 64 -27 minecraft:air run setblock 22 64 -27 minecraft:short_grass
execute if block 22 64 -23 minecraft:air run setblock 22 64 -23 minecraft:azure_bluet
execute if block 22 64 -22 minecraft:air run setblock 22 64 -22 minecraft:short_grass
execute if block 23 64 -25 minecraft:air run setblock 23 64 -25 minecraft:fern
execute if block 23 64 -22 minecraft:air run setblock 23 64 -22 minecraft:short_grass
execute if block 24 64 -35 minecraft:air run setblock 24 64 -35 minecraft:blue_orchid
execute if block 24 64 -30 minecraft:air run setblock 24 64 -30 minecraft:lily_pad
execute if block 24 64 -25 minecraft:air run setblock 24 64 -25 minecraft:orange_tulip
execute if block 26 64 -28 minecraft:air run setblock 26 64 -28 minecraft:lily_pad
execute if block 26 64 -26 minecraft:air run setblock 26 64 -26 minecraft:lily_pad
execute if block 26 64 -25 minecraft:air run setblock 26 64 -25 minecraft:lily_pad
execute if block 26 64 -22 minecraft:air run setblock 26 64 -22 minecraft:fern
execute if block 27 64 -25 minecraft:air run setblock 27 64 -25 minecraft:lily_pad
execute if block 27 91 -34 minecraft:air run setblock 27 91 -34 minecraft:short_grass
execute if block 27 91 -32 minecraft:air run setblock 27 91 -32 minecraft:azure_bluet
execute if block 27 91 -30 minecraft:air run setblock 27 91 -30 minecraft:oxeye_daisy
execute if block 27 91 -29 minecraft:air run setblock 27 91 -29 minecraft:allium
execute if block 28 64 -34 minecraft:air run setblock 28 64 -34 minecraft:lily_pad
execute if block 28 64 -26 minecraft:air run setblock 28 64 -26 minecraft:lily_pad
execute if block 28 64 -24 minecraft:air run setblock 28 64 -24 minecraft:lily_pad
execute if block 28 91 -30 minecraft:air run setblock 28 91 -30 minecraft:orange_tulip
execute if block 28 91 -29 minecraft:air run setblock 28 91 -29 minecraft:white_tulip
execute if block 28 91 -28 minecraft:air run setblock 28 91 -28 minecraft:white_tulip
execute if block 29 64 -32 minecraft:air run setblock 29 64 -32 minecraft:lily_pad
execute if block 29 91 -33 minecraft:air run setblock 29 91 -33 minecraft:short_grass
execute if block 29 91 -30 minecraft:air run setblock 29 91 -30 minecraft:short_grass
execute if block 30 64 -34 minecraft:air run setblock 30 64 -34 minecraft:lily_pad
execute if block 30 91 -29 minecraft:air run setblock 30 91 -29 minecraft:poppy
execute if block 30 91 -28 minecraft:air run setblock 30 91 -28 minecraft:azure_bluet
execute if block 30 91 -27 minecraft:air run setblock 30 91 -27 minecraft:white_tulip
execute if block 31 64 -22 minecraft:air run setblock 31 64 -22 minecraft:short_grass
execute if block 31 91 -32 minecraft:air run setblock 31 91 -32 minecraft:short_grass
execute if block 31 91 -29 minecraft:air run setblock 31 91 -29 minecraft:allium
execute if block 32 64 -25 minecraft:air run setblock 32 64 -25 minecraft:lily_pad
execute if block 32 91 -28 minecraft:air run setblock 32 91 -28 minecraft:blue_orchid
execute if block 32 91 -27 minecraft:air run setblock 32 91 -27 minecraft:white_tulip
execute if block 33 64 -33 minecraft:air run setblock 33 64 -33 minecraft:lily_pad
execute if block 33 64 -32 minecraft:air run setblock 33 64 -32 minecraft:lily_pad
execute if block 33 64 -22 minecraft:air run setblock 33 64 -22 minecraft:short_grass
execute if block 33 91 -33 minecraft:air run setblock 33 91 -33 minecraft:azure_bluet
execute if block 33 91 -29 minecraft:air run setblock 33 91 -29 minecraft:red_tulip
execute if block 33 91 -27 minecraft:air run setblock 33 91 -27 minecraft:oxeye_daisy
execute if block 34 64 -30 minecraft:air run setblock 34 64 -30 minecraft:lily_pad
execute if block 34 64 -25 minecraft:air run setblock 34 64 -25 minecraft:lily_pad
execute if block 34 64 -23 minecraft:air run setblock 34 64 -23 minecraft:pink_petals[flower_amount=4,facing=east]
execute if block 34 91 -34 minecraft:air run setblock 34 91 -34 minecraft:dandelion
execute if block 34 91 -31 minecraft:air run setblock 34 91 -31 minecraft:short_grass
execute if block 34 91 -30 minecraft:air run setblock 34 91 -30 minecraft:dandelion
execute if block 34 91 -29 minecraft:air run setblock 34 91 -29 minecraft:blue_orchid
execute if block 35 64 -34 minecraft:air run setblock 35 64 -34 minecraft:lily_pad
execute if block 35 64 -31 minecraft:air run setblock 35 64 -31 minecraft:lily_pad
execute if block 35 64 -23 minecraft:air run setblock 35 64 -23 minecraft:pink_petals[flower_amount=4,facing=north]
setblock 34 62 -54 minecraft:dirt
setblock 34 62 -53 minecraft:dirt
setblock 34 62 -52 minecraft:dirt
setblock 34 63 -54 minecraft:grass_block
setblock 34 63 -53 minecraft:dirt_path
setblock 34 63 -52 minecraft:dirt_path
setblock 35 62 -56 minecraft:dirt
setblock 35 62 -55 minecraft:dirt
setblock 35 62 -54 minecraft:dirt
setblock 35 62 -53 minecraft:stone
setblock 35 62 -52 minecraft:dirt
setblock 35 63 -56 minecraft:grass_block
setblock 35 63 -55 minecraft:grass_block
setblock 35 63 -54 minecraft:grass_block
setblock 35 63 -52 minecraft:coarse_dirt
setblock 36 62 -57 minecraft:dirt
setblock 36 62 -56 minecraft:dirt
setblock 36 62 -55 minecraft:stone
setblock 36 62 -54 minecraft:stone
setblock 36 62 -53 minecraft:stone
setblock 36 62 -52 minecraft:dirt
setblock 36 63 -57 minecraft:grass_block
setblock 36 63 -56 minecraft:grass_block
setblock 36 63 -52 minecraft:coarse_dirt
setblock 37 62 -58 minecraft:dirt
setblock 37 62 -57 minecraft:dirt
setblock 37 62 -56 minecraft:stone
setblock 37 62 -55 minecraft:stone
setblock 37 62 -54 minecraft:dirt
setblock 37 62 -53 minecraft:dirt
setblock 37 62 -52 minecraft:dirt
setblock 37 63 -58 minecraft:grass_block
setblock 37 63 -57 minecraft:grass_block
setblock 37 63 -54 minecraft:grass_block
setblock 37 63 -53 minecraft:grass_block
setblock 37 63 -52 minecraft:grass_block
setblock 38 62 -60 minecraft:dirt
setblock 38 62 -59 minecraft:dirt
setblock 38 62 -58 minecraft:dirt
setblock 38 62 -57 minecraft:stone
setblock 38 62 -56 minecraft:stone
setblock 38 62 -55 minecraft:dirt
setblock 38 62 -54 minecraft:dirt
setblock 38 63 -60 minecraft:grass_block
setblock 38 63 -59 minecraft:grass_block
setblock 38 63 -58 minecraft:grass_block
setblock 38 63 -55 minecraft:grass_block
setblock 38 63 -54 minecraft:grass_block
setblock 39 62 -61 minecraft:dirt
setblock 39 62 -60 minecraft:dirt
setblock 39 62 -59 minecraft:stone
setblock 39 62 -58 minecraft:stone
setblock 39 62 -57 minecraft:dirt
setblock 39 62 -56 minecraft:dirt
setblock 39 62 -55 minecraft:dirt
setblock 39 63 -61 minecraft:grass_block
setblock 39 63 -60 minecraft:grass_block
setblock 39 63 -57 minecraft:grass_block
setblock 39 63 -56 minecraft:grass_block
setblock 39 63 -55 minecraft:grass_block
setblock 40 62 -59 minecraft:stone
setblock 40 62 -58 minecraft:dirt
setblock 40 62 -57 minecraft:dirt
setblock 40 63 -58 minecraft:grass_block
setblock 40 63 -57 minecraft:grass_block
setblock 41 62 -58 minecraft:coarse_dirt
setblock 41 63 -58 minecraft:grass_block
execute unless block 35 64 -53 minecraft:air unless block 35 64 -53 minecraft:water run setblock 35 64 -53 minecraft:air
execute unless block 36 64 -55 minecraft:air unless block 36 64 -55 minecraft:water run setblock 36 64 -55 minecraft:air
execute unless block 36 64 -54 minecraft:air unless block 36 64 -54 minecraft:water run setblock 36 64 -54 minecraft:air
execute unless block 36 64 -53 minecraft:air unless block 36 64 -53 minecraft:water run setblock 36 64 -53 minecraft:air
execute unless block 37 64 -56 minecraft:air unless block 37 64 -56 minecraft:water run setblock 37 64 -56 minecraft:air
execute unless block 37 64 -55 minecraft:air unless block 37 64 -55 minecraft:water run setblock 37 64 -55 minecraft:air
execute unless block 38 64 -57 minecraft:air unless block 38 64 -57 minecraft:water run setblock 38 64 -57 minecraft:air
execute unless block 38 64 -56 minecraft:air unless block 38 64 -56 minecraft:water run setblock 38 64 -56 minecraft:air
execute unless block 39 64 -59 minecraft:air unless block 39 64 -59 minecraft:water run setblock 39 64 -59 minecraft:air
execute unless block 39 64 -58 minecraft:air unless block 39 64 -58 minecraft:water run setblock 39 64 -58 minecraft:air
execute unless block 40 61 -60 minecraft:air unless block 40 61 -60 minecraft:water run setblock 40 61 -60 minecraft:air
execute unless block 40 62 -61 minecraft:air unless block 40 62 -61 minecraft:water run setblock 40 62 -61 minecraft:air
execute unless block 40 62 -60 minecraft:air unless block 40 62 -60 minecraft:water run setblock 40 62 -60 minecraft:air
execute unless block 40 63 -61 minecraft:air unless block 40 63 -61 minecraft:water run setblock 40 63 -61 minecraft:air
execute unless block 40 64 -60 minecraft:air unless block 40 64 -60 minecraft:water run setblock 40 64 -60 minecraft:air
execute unless block 40 64 -59 minecraft:air unless block 40 64 -59 minecraft:water run setblock 40 64 -59 minecraft:air
execute unless block 41 62 -60 minecraft:air unless block 41 62 -60 minecraft:water run setblock 41 62 -60 minecraft:air
execute unless block 41 62 -59 minecraft:air unless block 41 62 -59 minecraft:water run setblock 41 62 -59 minecraft:air
execute unless block 41 63 -60 minecraft:air unless block 41 63 -60 minecraft:water run setblock 41 63 -60 minecraft:air
execute unless block 41 63 -59 minecraft:air unless block 41 63 -59 minecraft:water run setblock 41 63 -59 minecraft:air
fill 33 62 -62 42 64 -51 minecraft:air replace minecraft:lily_pad
fill 33 62 -62 42 64 -51 minecraft:air replace minecraft:water
setblock 35 63 -53 minecraft:water
setblock 36 63 -55 minecraft:water
setblock 36 63 -54 minecraft:water
setblock 36 63 -53 minecraft:water
setblock 37 63 -56 minecraft:water
setblock 37 63 -55 minecraft:water
setblock 38 63 -57 minecraft:water
setblock 38 63 -56 minecraft:water
setblock 39 63 -59 minecraft:water
setblock 39 63 -58 minecraft:water
setblock 40 63 -60 minecraft:water
setblock 40 63 -59 minecraft:water
execute if block 33 64 -62 minecraft:air run setblock 33 64 -62 minecraft:short_grass
execute if block 33 64 -56 minecraft:air run setblock 33 64 -56 minecraft:fern
execute if block 34 64 -59 minecraft:air run setblock 34 64 -59 minecraft:short_grass
execute if block 34 64 -58 minecraft:air run setblock 34 64 -58 minecraft:short_grass
execute if block 35 64 -59 minecraft:air run setblock 35 64 -59 minecraft:pink_tulip
execute if block 35 64 -58 minecraft:air run setblock 35 64 -58 minecraft:fern
execute if block 37 64 -54 minecraft:air run setblock 37 64 -54 minecraft:short_grass
execute if block 37 64 -52 minecraft:air run setblock 37 64 -52 minecraft:short_grass
execute if block 38 64 -62 minecraft:air run setblock 38 64 -62 minecraft:short_grass
execute if block 38 64 -59 minecraft:air run setblock 38 64 -59 minecraft:short_grass
execute if block 38 64 -58 minecraft:air run setblock 38 64 -58 minecraft:blue_orchid
execute if block 38 64 -53 minecraft:air run setblock 38 64 -53 minecraft:short_grass
execute if block 38 64 -51 minecraft:air run setblock 38 64 -51 minecraft:short_grass
execute if block 39 64 -60 minecraft:air run setblock 39 64 -60 minecraft:fern
execute if block 40 64 -57 minecraft:air run setblock 40 64 -57 minecraft:short_grass
execute if block 40 64 -53 minecraft:air run setblock 40 64 -53 minecraft:short_grass
execute if block 40 64 -52 minecraft:air run setblock 40 64 -52 minecraft:short_grass
execute if block 41 64 -53 minecraft:air run setblock 41 64 -53 minecraft:short_grass
execute if block 41 64 -52 minecraft:air run setblock 41 64 -52 minecraft:short_grass
execute if block 41 64 -51 minecraft:air run setblock 41 64 -51 minecraft:pink_petals[flower_amount=4,facing=north]
execute if block 42 64 -55 minecraft:air run setblock 42 64 -55 minecraft:allium
execute if block 42 64 -53 minecraft:air run setblock 42 64 -53 minecraft:short_grass
execute if block 42 64 -52 minecraft:air run setblock 42 64 -52 minecraft:short_grass
execute if block 42 64 -51 minecraft:air run setblock 42 64 -51 minecraft:pink_petals[flower_amount=3,facing=east]
setblock 52 62 34 minecraft:dirt
setblock 52 62 35 minecraft:dirt
setblock 52 62 36 minecraft:dirt
setblock 52 62 37 minecraft:dirt
setblock 52 63 34 minecraft:dirt_path
setblock 52 63 35 minecraft:coarse_dirt
setblock 52 63 36 minecraft:dirt_path
setblock 52 63 37 minecraft:grass_block
setblock 53 62 34 minecraft:dirt
setblock 53 62 35 minecraft:stone
setblock 53 62 36 minecraft:stone
setblock 53 62 37 minecraft:dirt
setblock 53 63 34 minecraft:dirt_path
setblock 53 63 37 minecraft:grass_block
setblock 54 62 34 minecraft:dirt
setblock 54 62 35 minecraft:dirt
setblock 54 62 36 minecraft:stone
setblock 54 62 37 minecraft:dirt
setblock 54 62 38 minecraft:dirt
setblock 54 63 34 minecraft:grass_block
setblock 54 63 35 minecraft:grass_block
setblock 54 63 37 minecraft:grass_block
setblock 54 63 38 minecraft:grass_block
setblock 55 62 35 minecraft:dirt
setblock 55 62 36 minecraft:stone
setblock 55 62 37 minecraft:stone
setblock 55 62 38 minecraft:dirt
setblock 55 62 39 minecraft:dirt
setblock 55 63 35 minecraft:grass_block
setblock 55 63 38 minecraft:grass_block
setblock 55 63 39 minecraft:grass_block
setblock 56 62 35 minecraft:dirt
setblock 56 62 36 minecraft:dirt
setblock 56 62 37 minecraft:stone
setblock 56 62 38 minecraft:stone
setblock 56 62 39 minecraft:dirt
setblock 56 63 35 minecraft:grass_block
setblock 56 63 36 minecraft:grass_block
setblock 56 63 39 minecraft:grass_block
setblock 57 62 36 minecraft:dirt
setblock 57 62 37 minecraft:dirt
setblock 57 62 38 minecraft:stone
setblock 57 62 39 minecraft:dirt
setblock 57 62 40 minecraft:dirt
setblock 57 63 36 minecraft:grass_block
setblock 57 63 37 minecraft:grass_block
setblock 57 63 39 minecraft:grass_block
setblock 57 63 40 minecraft:grass_block
setblock 58 62 37 minecraft:dirt
setblock 58 62 38 minecraft:dirt
setblock 58 62 39 minecraft:stone
setblock 58 62 40 minecraft:dirt
setblock 58 62 41 minecraft:dirt
setblock 58 63 37 minecraft:grass_block
setblock 58 63 38 minecraft:grass_block
setblock 58 63 40 minecraft:grass_block
setblock 58 63 41 minecraft:grass_block
setblock 59 62 38 minecraft:dirt
setblock 59 62 39 minecraft:stone
setblock 59 62 40 minecraft:stone
setblock 59 63 38 minecraft:grass_block
setblock 60 62 38 minecraft:dirt
setblock 60 62 39 minecraft:dirt
setblock 60 63 38 minecraft:grass_block
setblock 60 63 39 minecraft:grass_block
execute unless block 53 64 35 minecraft:air unless block 53 64 35 minecraft:water run setblock 53 64 35 minecraft:air
execute unless block 53 64 36 minecraft:air unless block 53 64 36 minecraft:water run setblock 53 64 36 minecraft:air
execute unless block 54 64 36 minecraft:air unless block 54 64 36 minecraft:water run setblock 54 64 36 minecraft:air
execute unless block 55 64 36 minecraft:air unless block 55 64 36 minecraft:water run setblock 55 64 36 minecraft:air
execute unless block 55 64 37 minecraft:air unless block 55 64 37 minecraft:water run setblock 55 64 37 minecraft:air
execute unless block 56 64 37 minecraft:air unless block 56 64 37 minecraft:water run setblock 56 64 37 minecraft:air
execute unless block 56 64 38 minecraft:air unless block 56 64 38 minecraft:water run setblock 56 64 38 minecraft:air
execute unless block 57 64 38 minecraft:air unless block 57 64 38 minecraft:water run setblock 57 64 38 minecraft:air
execute unless block 58 64 39 minecraft:air unless block 58 64 39 minecraft:water run setblock 58 64 39 minecraft:air
execute unless block 59 63 41 minecraft:air unless block 59 63 41 minecraft:water run setblock 59 63 41 minecraft:air
execute unless block 59 64 39 minecraft:air unless block 59 64 39 minecraft:water run setblock 59 64 39 minecraft:air
execute unless block 59 64 40 minecraft:air unless block 59 64 40 minecraft:water run setblock 59 64 40 minecraft:air
execute unless block 60 62 41 minecraft:air unless block 60 62 41 minecraft:water run setblock 60 62 41 minecraft:air
execute unless block 60 63 41 minecraft:air unless block 60 63 41 minecraft:water run setblock 60 63 41 minecraft:air
execute unless block 60 64 40 minecraft:air unless block 60 64 40 minecraft:water run setblock 60 64 40 minecraft:air
execute unless block 61 62 40 minecraft:air unless block 61 62 40 minecraft:water run setblock 61 62 40 minecraft:air
execute unless block 61 63 40 minecraft:air unless block 61 63 40 minecraft:water run setblock 61 63 40 minecraft:air
fill 51 62 33 62 64 42 minecraft:air replace minecraft:lily_pad
fill 51 62 33 62 64 42 minecraft:air replace minecraft:water
setblock 53 63 35 minecraft:water
setblock 53 63 36 minecraft:water
setblock 54 63 36 minecraft:water
setblock 55 63 36 minecraft:water
setblock 55 63 37 minecraft:water
setblock 56 63 37 minecraft:water
setblock 56 63 38 minecraft:water
setblock 57 63 38 minecraft:water
setblock 58 63 39 minecraft:water
setblock 59 63 39 minecraft:water
setblock 59 63 40 minecraft:water
setblock 60 63 40 minecraft:water
execute if block 51 64 42 minecraft:air run setblock 51 64 42 minecraft:fern
execute if block 52 64 37 minecraft:air run setblock 52 64 37 minecraft:short_grass
execute if block 52 64 38 minecraft:air run setblock 52 64 38 minecraft:orange_tulip
execute if block 53 64 39 minecraft:air run setblock 53 64 39 minecraft:short_grass
execute if block 53 64 41 minecraft:air run setblock 53 64 41 minecraft:fern
execute if block 54 64 38 minecraft:air run setblock 54 64 38 minecraft:short_grass
execute if block 54 64 41 minecraft:air run setblock 54 64 41 minecraft:short_grass
execute if block 55 64 33 minecraft:air run setblock 55 64 33 minecraft:short_grass
execute if block 55 64 41 minecraft:air run setblock 55 64 41 minecraft:short_grass
execute if block 55 64 42 minecraft:air run setblock 55 64 42 minecraft:short_grass
execute if block 56 64 35 minecraft:air run setblock 56 64 35 minecraft:short_grass
execute if block 56 64 36 minecraft:air run setblock 56 64 36 minecraft:short_grass
execute if block 56 64 41 minecraft:air run setblock 56 64 41 minecraft:white_tulip
execute if block 56 64 42 minecraft:air run setblock 56 64 42 minecraft:short_grass
execute if block 57 64 34 minecraft:air run setblock 57 64 34 minecraft:short_grass
execute if block 57 64 35 minecraft:air run setblock 57 64 35 minecraft:short_grass
execute if block 57 64 36 minecraft:air run setblock 57 64 36 minecraft:short_grass
execute if block 57 64 41 minecraft:air run setblock 57 64 41 minecraft:red_tulip
execute if block 58 64 34 minecraft:air run setblock 58 64 34 minecraft:short_grass
execute if block 58 64 36 minecraft:air run setblock 58 64 36 minecraft:short_grass
execute if block 58 64 37 minecraft:air run setblock 58 64 37 minecraft:white_tulip
execute if block 59 64 34 minecraft:air run setblock 59 64 34 minecraft:fern
execute if block 59 64 36 minecraft:air run setblock 59 64 36 minecraft:short_grass
execute if block 59 64 38 minecraft:air run setblock 59 64 38 minecraft:short_grass
execute if block 60 64 34 minecraft:air run setblock 60 64 34 minecraft:short_grass
execute if block 60 64 35 minecraft:air run setblock 60 64 35 minecraft:short_grass
