# Vaisseau — vague 20 : BOSS Le Cœur I.A. Corrompu
summon minecraft:shulker 20.5 67 10688.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10694.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10700.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:shulker 20.5 67 10706.5 {Tags:["mg.mob"],AttachFace:5b,PersistenceRequired:1b}
summon minecraft:endermite 14.5 65 10714.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -13.5 65 10714.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 14.5 65 10686.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -13.5 65 10686.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite 16.5 65 10700.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
summon minecraft:endermite -15.5 65 10700.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 2 true
tag @e[tag=mg.fz] remove mg.fz
summon minecraft:wither 0.5 66 10700.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Cœur I.A. Corrompu","color":"light_purple","bold":true}],CustomNameVisible:1b,NoAI:1b,Invul:0}
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:900,name:"{\"text\":\"Le Cœur I.A. Corrompu\",\"color\":\"light_purple\",\"bold\":true}"}
function mg:mobarena/ship/boss_init
title @a title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a subtitle [{"text":"Le Cœur I.A. Corrompu","color":"light_purple"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Shulker, 6× Endermite rapide","color":"yellow"},{"text":"  (sbires + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Cœur I.A. Corrompu","color":"light_purple","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
