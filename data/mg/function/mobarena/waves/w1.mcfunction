# Vague 1 — 5 zombies
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"5× Zombie","color":"yellow"},{"text":"  (5 monstres)","color":"dark_gray"}]
