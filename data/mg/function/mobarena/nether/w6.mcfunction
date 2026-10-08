# Nether — vague 6
summon minecraft:piglin_brute 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:hoglin 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b}
summon minecraft:hoglin 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b}
summon minecraft:hoglin 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Piglin brute, 3× Hoglin","color":"yellow"},{"text":"  (7 monstres)","color":"dark_gray"}]
