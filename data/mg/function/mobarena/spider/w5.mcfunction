# Spider — vague 5
summon minecraft:cave_spider 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run summon minecraft:spider 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"La Reine Araignée","color":"dark_green","bold":true}],CustomNameVisible:1b}
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 3
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:150,name:"{\"text\":\"La Reine Araignée\",\"color\":\"dark_green\",\"bold\":true}"}
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"La Reine Araignée","color":"dark_green"}]
execute unless score $wdup mg.st matches 1 run execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Araignée venimeuse","color":"yellow"},{"text":"  (8 monstres + boss)","color":"dark_gray"}]
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"La Reine Araignée","color":"dark_green","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
