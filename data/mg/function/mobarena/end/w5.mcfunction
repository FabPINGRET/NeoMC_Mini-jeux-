# End — vague 5
summon minecraft:endermite 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:endermite 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Veilleur","color":"light_purple","bold":true}],CustomNameVisible:1b}
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:150,name:'{"text":"Le Veilleur","color":"light_purple","bold":true}'}
title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"Le Veilleur","color":"light_purple"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Endermite","color":"yellow"},{"text":"  (6 monstres + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Veilleur","color":"light_purple","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
