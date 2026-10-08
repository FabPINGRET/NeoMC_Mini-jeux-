# 🎢 Montagne russe : gare + voie
fill -182 62 -46 -110 102 2 minecraft:air strict
fill -124 63 -9 -104 63 3 minecraft:spruce_planks
fill -124 62 -9 -104 62 3 minecraft:stripped_spruce_log
fill -124 64 -9 -104 64 -9 minecraft:spruce_fence
fill -124 64 3 -104 64 3 minecraft:spruce_fence
fill -104 64 -8 -104 64 2 minecraft:air
fill -124 64 -8 -124 64 2 minecraft:spruce_fence
fill -124 64 0 -124 64 0 minecraft:air
fill -124 64 -6 -124 64 -6 minecraft:air
fill -123 68 -9 -105 68 3 minecraft:spruce_slab[type=bottom]
fill -123 64 -9 -123 67 -9 minecraft:spruce_log
fill -105 64 -9 -105 67 -9 minecraft:spruce_log
fill -123 64 3 -123 67 3 minecraft:spruce_log
fill -105 64 3 -105 67 3 minecraft:spruce_log
setblock -110 67 -3 minecraft:lantern[hanging=true]
setblock -118 67 -3 minecraft:lantern[hanging=true]
fill -111 63 1 -109 63 1 minecraft:gold_block
setblock -110 64 1 minecraft:light_weighted_pressure_plate
function mg:coaster/track
kill @e[tag=mg.cst]
kill @e[tag=mg.csd]
summon minecraft:text_display -110 66.6 1.5 {Tags:["mg.csd"],billboard:"center",text:[{"text":"🎢 Montagne russe","color":"gold","bold":true},{"text":"\nmarche sur la plaque dorée","color":"gray"}]}
summon minecraft:text_display -106.5 65.8 0.5 {Tags:["mg.csd"],billboard:"center",text:{"text":"🎢 ← Montagne russe","color":"gold","bold":true}}
forceload remove -182 -46 -110 2
data modify storage mg:lobby coaster1 set value 1b
tellraw @a[tag=mg.admin] {"text":"🎢 Montagne russe construite (gare à l'ouest du spawn).","color":"gold"}
