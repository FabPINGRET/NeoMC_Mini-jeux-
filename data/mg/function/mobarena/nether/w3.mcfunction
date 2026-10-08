# Nether — vague 3
summon minecraft:blaze 11.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -11.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 11.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:magma_cube -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,Size:2}
summon minecraft:magma_cube 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,Size:2}
summon minecraft:magma_cube 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,Size:2}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"3× Blaze, 3× Cube de magma","color":"yellow"},{"text":"  (6 monstres)","color":"dark_gray"}]
