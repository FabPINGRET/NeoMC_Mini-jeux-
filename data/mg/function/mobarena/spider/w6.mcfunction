# Spider — vague 6
summon minecraft:spider 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider -11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Araignée, 3× Jockey (araignée + squelette)","color":"yellow"},{"text":"  (14 monstres)","color":"dark_gray"}]
