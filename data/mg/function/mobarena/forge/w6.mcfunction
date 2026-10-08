# Forge — vague 6
summon minecraft:piglin_brute 12.6 66 10303.3 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 9.2 66 10309.2 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 3.4 66 10312.6 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -3.3 66 10312.6 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -9.2 66 10309.2 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -12.6 66 10303.4 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -12.6 66 10296.7 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -9.2 66 10290.8 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:blaze 24.5 74 10300.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -23.5 74 10300.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 74 10324.5 {Tags:["mg.mob"],PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 0 true
effect give @e[tag=mg.fs] minecraft:strength infinite 0 true
effect give @e[tag=mg.fz1] minecraft:speed infinite 0 true
tag @e[tag=mg.fz] remove mg.fz
tag @e[tag=mg.fs] remove mg.fs
tag @e[tag=mg.fz1] remove mg.fz1
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Piglin furieux, 3× Blaze (tourelle)","color":"yellow"},{"text":"  (11 monstres)","color":"dark_gray"}]
