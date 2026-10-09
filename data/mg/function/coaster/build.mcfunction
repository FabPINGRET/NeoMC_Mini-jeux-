# 🎢 Montagne russe : gare + voie
fill -188 62 -46 -109 69 2 minecraft:air strict
fill -188 70 -46 -109 77 2 minecraft:air strict
fill -188 78 -46 -109 85 2 minecraft:air strict
fill -188 86 -46 -109 93 2 minecraft:air strict
fill -188 94 -46 -109 101 2 minecraft:air strict
fill -188 102 -46 -109 102 2 minecraft:air strict
fill -124 62 -9 -109 70 3 minecraft:air
fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:spruce_fence
fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:spruce_log
fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:spruce_slab
fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:lantern
fill -108 62 -9 -104 62 3 minecraft:air replace minecraft:stripped_spruce_log
fill -107 63 -9 -107 63 3 minecraft:stone_bricks replace minecraft:spruce_planks
fill -106 63 -9 -104 63 3 minecraft:grass_block replace minecraft:spruce_planks
fill -108 63 -9 -108 63 3 minecraft:stone_bricks replace minecraft:spruce_planks
function mg:plot/walls {x1:-108,x2:-84,z1:-12,z2:12}
fill -130 63 -9 -110 63 3 minecraft:spruce_planks
fill -130 62 -9 -110 62 3 minecraft:stripped_spruce_log
fill -130 64 -9 -110 64 -9 minecraft:spruce_fence
fill -130 64 3 -110 64 3 minecraft:spruce_fence
fill -110 64 -8 -110 64 2 minecraft:spruce_fence
fill -130 64 -8 -130 64 2 minecraft:spruce_fence
fill -130 64 0 -130 64 0 minecraft:air
fill -130 64 -6 -130 64 -6 minecraft:air
fill -115 64 3 -114 64 3 minecraft:air
fill -129 68 -9 -111 68 3 minecraft:spruce_slab[type=bottom]
fill -129 64 -9 -129 67 -9 minecraft:spruce_log
fill -111 64 -9 -111 67 -9 minecraft:spruce_log
fill -129 64 3 -129 67 3 minecraft:spruce_log
fill -111 64 3 -111 67 3 minecraft:spruce_log
setblock -116 67 -3 minecraft:lantern[hanging=true]
setblock -124 67 -3 minecraft:lantern[hanging=true]
fill -117 63 1 -115 63 1 minecraft:gold_block
setblock -116 64 1 minecraft:light_weighted_pressure_plate
fill -115 63 16 -71 63 17 minecraft:spruce_planks
fill -115 62 16 -71 62 17 minecraft:stripped_spruce_log
fill -115 64 15 -73 64 15 minecraft:spruce_fence
fill -115 64 18 -73 64 18 minecraft:spruce_fence
fill -115 63 4 -114 63 15 minecraft:spruce_planks
fill -115 62 4 -114 62 15 minecraft:stripped_spruce_log
fill -116 64 4 -116 64 18 minecraft:spruce_fence
fill -113 64 4 -113 64 14 minecraft:spruce_fence
fill -114 64 15 -114 64 15 minecraft:air
fill -115 64 15 -115 64 15 minecraft:air
setblock -116 65 16 minecraft:lantern
setblock -92 65 15 minecraft:lantern
setblock -92 65 18 minecraft:lantern
setblock -73 65 15 minecraft:lantern
setblock -73 65 18 minecraft:lantern
setblock -113 65 8 minecraft:lantern
function mg:coaster/track
kill @e[tag=mg.cst]
kill @e[tag=mg.csd]
summon minecraft:text_display -116 66.6 1.5 {Tags:["mg.csd"],billboard:"center",text:[{"text":"🎢 Montagne russe","color":"gold","bold":true},{"text":"\nmarche sur la plaque dorée","color":"gray"}]}
summon minecraft:text_display -70.5 66 16.9 {Tags:["mg.csd"],billboard:"center",text:{"text":"🎢 Montagne russe →","color":"gold","bold":true}}
forceload remove -188 -46 -116 2
data modify storage mg:lobby coaster1 set value 1b
data modify storage mg:lobby coaster2 set value 1b
tellraw @a[tag=mg.admin] {"text":"🎢 Montagne russe construite (gare à l'ouest du spawn).","color":"gold"}
