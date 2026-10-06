# Vaisseau — vague 6
summon minecraft:endermite 14.5 65 10714.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -13.5 65 10714.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 14.5 65 10686.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -13.5 65 10686.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 16.5 65 10700.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -15.5 65 10700.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 65 10716.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 8.5 65 10716.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -7.5 65 10716.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 16.5 65 10708.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:phantom -13.5 76 10686.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 14.5 76 10686.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -13.5 76 10714.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 14.5 76 10714.5 {Tags:["mg.mob"],PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 2 true
tag @e[tag=mg.fz] remove mg.fz
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"10× Endermite rapide, 4× Phantom","color":"yellow"},{"text":"  (14 monstres)","color":"dark_gray"}]
