# Laboratoire — vague 9
summon minecraft:creeper 14.5 65 9500.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper -13.5 65 9500.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper 0.5 65 9514.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper 0.5 65 9486.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper 10.5 65 9510.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper -9.5 65 9510.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:witch 10.5 65 9490.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch -9.5 65 9490.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch 14.5 65 9507.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch -13.5 65 9507.5 {Tags:["mg.mob"],PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 1 true
tag @e[tag=mg.fz] remove mg.fz
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Creeper chargé, 4× Sorcière","color":"yellow"},{"text":"  (10 monstres)","color":"dark_gray"}]
