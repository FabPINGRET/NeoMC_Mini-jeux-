# Nether — vague 10
summon minecraft:wither_skeleton 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:wither_skeleton -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:wither_skeleton 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:wither_skeleton -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:blaze 0.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 11.5 65 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:piglin_brute 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Roi Piglin","color":"gold","bold":true}],CustomNameVisible:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}},IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1},head:{id:"minecraft:golden_helmet",count:1},chest:{id:"minecraft:golden_chestplate",count:1},legs:{id:"minecraft:golden_leggings",count:1},feet:{id:"minecraft:golden_boots",count:1}}}
execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 1.5
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:400,name:"{\"text\":\"Le Roi Piglin\",\"color\":\"gold\",\"bold\":true}"}
title @a title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a subtitle [{"text":"Le Roi Piglin","color":"gold"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Wither squelette, 3× Blaze","color":"yellow"},{"text":"  (7 monstres + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Roi Piglin","color":"gold","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
