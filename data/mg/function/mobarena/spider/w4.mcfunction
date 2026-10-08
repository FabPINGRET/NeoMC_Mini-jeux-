# Spider — vague 4
summon minecraft:spider 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Jockey (araignée + squelette)","color":"yellow"},{"text":"  (8 monstres)","color":"dark_gray"}]
