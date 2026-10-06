# Cathédrale — vague 20 : BOSS Le Comte de Sang
summon minecraft:skeleton -11.5 70 9084.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9084.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton -11.5 70 9088.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9088.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton -11.5 70 9092.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9092.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
effect give @e[tag=mg.fz] minecraft:speed infinite 1 true
tag @e[tag=mg.fz] remove mg.fz
summon minecraft:wither_skeleton 0.5 65 9110.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Comte de Sang","color":"dark_red","bold":true}],CustomNameVisible:1b,equipment:{}}
execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 2.5
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:700,name:"{\"text\":\"Le Comte de Sang\",\"color\":\"dark_red\",\"bold\":true}"}
function mg:mobarena/cathedral/boss_init
title @a title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a subtitle [{"text":"Le Comte de Sang","color":"dark_red"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Squelette archer","color":"yellow"},{"text":"  (sbires + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Comte de Sang","color":"dark_red","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
