# Forge — vague 1
summon minecraft:piglin_brute 12.6 66 10303.3 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 9.2 66 10309.2 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 3.4 66 10312.6 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -3.3 66 10312.6 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin -9.2 66 10309.2 {Tags:["mg.mob","mg.fz1"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_sword",count:1}}}
summon minecraft:piglin -12.6 66 10303.4 {Tags:["mg.mob","mg.fz1"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_sword",count:1}}}
effect give @e[tag=mg.fz] minecraft:speed infinite 0 true
effect give @e[tag=mg.fs] minecraft:strength infinite 0 true
effect give @e[tag=mg.fz1] minecraft:speed infinite 0 true
tag @e[tag=mg.fz] remove mg.fz
tag @e[tag=mg.fs] remove mg.fs
tag @e[tag=mg.fz1] remove mg.fz1
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Piglin furieux, 2× Piglin","color":"yellow"},{"text":"  (6 monstres)","color":"dark_gray"}]
