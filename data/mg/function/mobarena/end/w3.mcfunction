# End — vague 3
summon minecraft:shulker 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:shulker -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"2× Shulker, 4× Endermite","color":"yellow"},{"text":"  (6 monstres)","color":"dark_gray"}]
