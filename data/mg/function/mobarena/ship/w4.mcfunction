# Vaisseau — vague 4
summon minecraft:endermite 14.5 65 10714.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -13.5 65 10714.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 14.5 65 10686.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -13.5 65 10686.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 16.5 65 10700.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -15.5 65 10700.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 65 10716.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 8.5 65 10716.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10688.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10694.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10700.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 2 true
tag @e[tag=mg.fz] remove mg.fz
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Endermite rapide, 3× Shulker","color":"yellow"},{"text":"  (11 monstres)","color":"dark_gray"}]
