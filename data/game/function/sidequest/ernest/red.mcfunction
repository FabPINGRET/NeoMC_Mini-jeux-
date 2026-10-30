fill 491 98 -74 501 82 -87 minecraft:netherrack replace minecraft:dried_kelp_block
fill 491 98 -74 501 82 -87 minecraft:netherrack replace minecraft:prismarine_bricks
fill 491 98 -74 501 82 -87 minecraft:glowstone replace minecraft:verdant_froglight
fill 491 98 -74 501 82 -87 minecraft:glowstone replace minecraft:sea_lantern
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:big_dripleaf
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:big_dripleaf_stem
fill 491 98 -74 501 82 -87 minecraft:air replace minecraft:water
fill 491 98 -74 501 82 -87 minecraft:netherrack replace minecraft:moss_block


#secondary
fill 494 83 -74 492 87 -71 air replace water

fill 502 87 -63 506 94 -67 minecraft:netherrack replace minecraft:dried_kelp_block
fill 502 87 -63 506 94 -67 minecraft:netherrack replace minecraft:prismarine_bricks
fill 502 87 -63 506 94 -67 minecraft:glowstone replace minecraft:verdant_froglight
fill 502 87 -63 506 94 -67 minecraft:glowstone replace minecraft:sea_lantern

#Features

fill 493 89 -81 493 97 -81 minecraft:weeping_vines
setblock 493 88 -81 minecraft:weeping_vines[age=25]

fill 493 89 -83 493 97 -83 minecraft:weeping_vines
setblock 493 88 -83 minecraft:weeping_vines[age=25]

fill 494 89 -85 494 97 -85 minecraft:weeping_vines
setblock 494 88 -85 minecraft:weeping_vines[age=25]

fill 497 93 -76 497 97 -76 minecraft:weeping_vines
setblock 497 92 -76 minecraft:weeping_vines[age=25]

fill 499 94 -82 499 97 -82 minecraft:weeping_vines
setblock 499 93 -82 minecraft:weeping_vines[age=25]

fill 504 88 -65 504 93 -65 minecraft:weeping_vines

execute positioned 496 89 -81 run tellraw @a[distance=..15,tag=mg.flw] {"text":"Red is climb...","italic":true,"color":"red"}
