fill 491 98 -74 501 82 -87 minecraft:prismarine_bricks replace minecraft:netherrack
fill 491 98 -74 501 82 -87 minecraft:prismarine_bricks replace minecraft:dried_kelp_block
fill 491 98 -74 501 82 -87 minecraft:sea_lantern replace minecraft:glowstone
fill 491 98 -74 501 82 -87 minecraft:sea_lantern replace minecraft:verdant_froglight
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:weeping_vines
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:big_dripleaf
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:big_dripleaf_stem


#secondary

fill 502 87 -63 506 94 -67 minecraft:prismarine_bricks replace minecraft:netherrack
fill 502 87 -63 506 94 -67 minecraft:prismarine_bricks replace minecraft:dried_kelp_block
fill 502 87 -63 506 94 -67 minecraft:sea_lantern replace minecraft:glowstone
fill 502 87 -63 506 94 -67 minecraft:sea_lantern replace minecraft:verdant_froglight
fill 502 87 -63 506 94 -67 minecraft:air replace minecraft:weeping_vines
fill 491 98 -74 501 82 -87 minecraft:prismarine_bricks replace minecraft:moss_block

#Features
fill 494 83 -77 492 83 -72 water replace air
fill 496 83 -86 497 83 -85 water
fill 493 83 -72 493 87 -72 water

execute positioned 496 89 -81 run tellraw @a[distance=..15,tag=mg.flw] {"text":"Blue is swim...","italic":true,"color":"aqua"}
