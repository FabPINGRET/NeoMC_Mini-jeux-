# Volant — vague 5
summon minecraft:phantom 11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run summon minecraft:ghast 0.5 72 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"La Pleureuse","color":"white","bold":true}],CustomNameVisible:1b}
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:60,name:"{\"text\":\"La Pleureuse\",\"color\":\"white\",\"bold\":true}"}
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"La Pleureuse","color":"white"}]
execute unless score $wdup mg.st matches 1 run execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Phantom","color":"yellow"},{"text":"  (6 monstres + boss)","color":"dark_gray"}]
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"La Pleureuse","color":"white","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
