# Vague 4 — 8 zombies + 4 squelettes
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:skeleton 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Zombie, 4× Squelette archer","color":"yellow"},{"text":"  (12 monstres)","color":"dark_gray"}]
