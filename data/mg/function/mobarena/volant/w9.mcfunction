# Volant — vague 9
summon minecraft:ghast 11.5 72 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:ghast -11.5 72 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 11.5 68 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 11.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -11.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"2× Ghast, 8× Phantom, 4× Blaze","color":"yellow"},{"text":"  (14 monstres)","color":"dark_gray"}]
