fill 491 98 -74 501 82 -87 minecraft:dried_kelp_block replace minecraft:netherrack
fill 491 98 -74 501 82 -87 minecraft:dried_kelp_block replace minecraft:prismarine_bricks
fill 491 98 -74 501 82 -87 minecraft:verdant_froglight replace minecraft:glowstone
fill 491 98 -74 501 82 -87 minecraft:verdant_froglight replace minecraft:sea_lantern
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:weeping_vines
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:water

#secondary
fill 494 83 -74 492 87 -71 air replace water

fill 502 87 -63 506 94 -67 minecraft:dried_kelp_block replace minecraft:netherrack
fill 502 87 -63 506 94 -67 minecraft:dried_kelp_block replace minecraft:prismarine_bricks
fill 502 87 -63 506 94 -67 minecraft:verdant_froglight replace minecraft:glowstone
fill 502 87 -63 506 94 -67 minecraft:verdant_froglight replace minecraft:sea_lantern
fill 502 87 -63 506 94 -67 minecraft:air replace minecraft:weeping_vines

#Features

setblock 499 87 -78 minecraft:big_dripleaf
fill 499 86 -78 499 83 -78 minecraft:big_dripleaf_stem
setblock 499 82 -78 minecraft:moss_block

setblock 497 87 -83 minecraft:big_dripleaf
fill 497 86 -83 497 83 -83 minecraft:big_dripleaf_stem
setblock 497 82 -83 minecraft:moss_block

setblock 494 87 -81 minecraft:big_dripleaf
fill 494 86 -81 494 83 -81 minecraft:big_dripleaf_stem
setblock 494 82 -81 minecraft:moss_block

execute positioned 496 89 -81 run tellraw @a[distance=..15,tag=mg.flw] {"text":"Green is grow...","italic":true,"color":"green"}
