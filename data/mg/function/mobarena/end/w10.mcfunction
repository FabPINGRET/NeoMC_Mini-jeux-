# End — vague 10
summon minecraft:enderman 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:shulker 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:shulker 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:shulker 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:shulker -11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:enderman 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"L'Ombre du Vide","color":"dark_purple","bold":true}],CustomNameVisible:1b}
execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 2
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:500,name:"{\"text\":\"L'Ombre du Vide\",\"color\":\"dark_purple\",\"bold\":true}"}
title @a title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a subtitle [{"text":"L'Ombre du Vide","color":"dark_purple"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Enderman, 4× Shulker","color":"yellow"},{"text":"  (8 monstres + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"L'Ombre du Vide","color":"dark_purple","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
