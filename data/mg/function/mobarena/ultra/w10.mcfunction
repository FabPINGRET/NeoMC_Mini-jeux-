# Ultra — vague 10
summon minecraft:ravager 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:ravager -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:diamond_helmet",count:1},chest:{id:"minecraft:diamond_chestplate",count:1},legs:{id:"minecraft:diamond_leggings",count:1},mainhand:{id:"minecraft:diamond_sword",count:1}}}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:diamond_helmet",count:1},chest:{id:"minecraft:diamond_chestplate",count:1},legs:{id:"minecraft:diamond_leggings",count:1},mainhand:{id:"minecraft:diamond_sword",count:1}}}
summon minecraft:zombie 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:diamond_helmet",count:1},chest:{id:"minecraft:diamond_chestplate",count:1},legs:{id:"minecraft:diamond_leggings",count:1},mainhand:{id:"minecraft:diamond_sword",count:1}}}
summon minecraft:zombie 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:diamond_helmet",count:1},chest:{id:"minecraft:diamond_chestplate",count:1},legs:{id:"minecraft:diamond_leggings",count:1},mainhand:{id:"minecraft:diamond_sword",count:1}}}
summon minecraft:zombie 11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:diamond_helmet",count:1},chest:{id:"minecraft:diamond_chestplate",count:1},legs:{id:"minecraft:diamond_leggings",count:1},mainhand:{id:"minecraft:diamond_sword",count:1}}}
summon minecraft:zombie -11.5 64 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:diamond_helmet",count:1},chest:{id:"minecraft:diamond_chestplate",count:1},legs:{id:"minecraft:diamond_leggings",count:1},mainhand:{id:"minecraft:diamond_sword",count:1}}}
summon minecraft:warden 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Warden","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:500,name:"{\"text\":\"Le Warden\",\"color\":\"dark_aqua\",\"bold\":true}"}
title @a title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a subtitle [{"text":"Le Warden","color":"dark_aqua"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"2× Ravageur, 6× Zombie en diamant","color":"yellow"},{"text":"  (8 monstres + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Warden","color":"dark_aqua","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
