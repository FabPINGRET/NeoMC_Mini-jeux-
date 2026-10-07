# Nether — vague 5
summon minecraft:blaze 11.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -11.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:piglin_brute 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:wither_skeleton 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Capitaine Calciné","color":"gold","bold":true}],CustomNameVisible:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}},equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 1.3
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:120,name:"{\"text\":\"Capitaine Calciné\",\"color\":\"gold\",\"bold\":true}"}
title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"Capitaine Calciné","color":"gold"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"2× Blaze, 2× Piglin brute","color":"yellow"},{"text":"  (4 monstres + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Capitaine Calciné","color":"gold","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
