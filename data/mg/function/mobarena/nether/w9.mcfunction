# Nether — vague 9
summon minecraft:hoglin 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b}
summon minecraft:hoglin -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b}
summon minecraft:hoglin 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b}
summon minecraft:hoglin -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b}
summon minecraft:blaze 0.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 11.5 65 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -11.5 65 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:piglin_brute 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Hoglin, 4× Blaze, 3× Piglin brute","color":"yellow"},{"text":"  (11 monstres)","color":"dark_gray"}]
