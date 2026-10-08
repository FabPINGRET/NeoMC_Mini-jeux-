# Nether — vague 7
summon minecraft:blaze 11.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -11.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 11.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -11.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:magma_cube 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,Size:3}
summon minecraft:magma_cube 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,Size:3}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"5× Blaze, 2× Cube de magma","color":"yellow"},{"text":"  (7 monstres)","color":"dark_gray"}]
