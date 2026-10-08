# End — vague 7
summon minecraft:endermite 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Endermite, 3× Enderman, 3× Phantom","color":"yellow"},{"text":"  (14 monstres)","color":"dark_gray"}]
