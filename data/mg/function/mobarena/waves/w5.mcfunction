# Vague 5 — 4 vindicateurs + 6 zombies
summon minecraft:vindicator 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Vindicateur, 6× Zombie","color":"yellow"},{"text":"  (10 monstres)","color":"dark_gray"}]
