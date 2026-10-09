# 🎢 Montagne russe : guichet + voie autour du spawn
execute unless data storage mg:lobby coaster3 run function mg:coaster/clear_old
fill -47 63 39 -43 63 43 minecraft:spruce_planks
fill -47 64 39 -43 67 43 minecraft:air
setblock -47 64 39 minecraft:spruce_log
setblock -43 64 39 minecraft:spruce_log
setblock -47 64 43 minecraft:spruce_log
setblock -43 64 43 minecraft:spruce_log
fill -47 65 39 -47 66 39 minecraft:spruce_log
fill -43 65 39 -43 66 39 minecraft:spruce_log
fill -47 65 43 -47 66 43 minecraft:spruce_log
fill -43 65 43 -43 66 43 minecraft:spruce_log
fill -47 67 39 -43 67 43 minecraft:spruce_slab[type=bottom]
setblock -45 66 41 minecraft:lantern[hanging=true]
setblock -45 63 41 minecraft:gold_block
setblock -45 64 41 minecraft:light_weighted_pressure_plate
function mg:coaster/track
kill @e[tag=mg.cst]
kill @e[tag=mg.csd]
summon minecraft:text_display -44.5 66.2 41.5 {Tags:["mg.csd"],billboard:"center",text:[{"text":"🎢 Montagne russe","color":"gold","bold":true},{"text":"\nle tour du spawn — marche sur la plaque dorée","color":"gray"}]}
forceload remove -66 -66 66 66
forceload remove -130 -12 -71 20
function mg:core/forceloads
data modify storage mg:lobby coaster1 set value 1b
data modify storage mg:lobby coaster2 set value 1b
data modify storage mg:lobby coaster3 set value 1b
tellraw @a[tag=mg.admin] {"text":"🎢 Montagne russe construite : tour du spawn, guichet au sud-ouest.","color":"gold"}
