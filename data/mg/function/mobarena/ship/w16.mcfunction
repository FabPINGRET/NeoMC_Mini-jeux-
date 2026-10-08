# Vaisseau — vague 16
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
summon minecraft:endermite -15.5 65 10708.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 16.5 65 10692.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -15.5 65 10692.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 65 10684.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 12.5 65 10705.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 65 10705.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 12.5 65 10695.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 65 10695.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10688.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10694.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10700.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10706.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10712.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker -19.5 67 10688.5 {Tags:["mg.mob"],AttachFace:4b,PersistenceRequired:1b}
summon minecraft:shulker -19.5 67 10694.5 {Tags:["mg.mob"],AttachFace:4b,PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 2 true
tag @e[tag=mg.fz] remove mg.fz
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"18× Endermite rapide, 7× Shulker","color":"yellow"},{"text":"  (25 monstres)","color":"dark_gray"}]
