# Spider — vague 1
summon minecraft:spider 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Araignée","color":"yellow"},{"text":"  (6 monstres)","color":"dark_gray"}]
