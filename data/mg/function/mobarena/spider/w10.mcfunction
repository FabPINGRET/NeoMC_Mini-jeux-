# Spider — vague 10
summon minecraft:cave_spider 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:cave_spider -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:spider 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
summon minecraft:spider -11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:skeleton",Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}]}
execute unless score $wdup mg.st matches 1 run summon minecraft:spider 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"L'Arachnarque","color":"dark_red","bold":true}],CustomNameVisible:1b}
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 4
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:450,name:"{\"text\":\"L'Arachnarque\",\"color\":\"dark_red\",\"bold\":true}"}
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"L'Arachnarque","color":"dark_red"}]
execute unless score $wdup mg.st matches 1 run execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"12× Araignée venimeuse, 4× Jockey (araignée + squelette)","color":"yellow"},{"text":"  (20 monstres + boss)","color":"dark_gray"}]
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"L'Arachnarque","color":"dark_red","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
