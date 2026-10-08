# Cathédrale — vague 20 : BOSS Le Comte de Sang
summon minecraft:skeleton -11.5 70 9084.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9084.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton -11.5 70 9088.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9088.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton -11.5 70 9092.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9092.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
effect give @e[tag=mg.fz] minecraft:speed infinite 1 true
tag @e[tag=mg.fz] remove mg.fz
execute unless score $wdup mg.st matches 1 run summon minecraft:wither_skeleton 0.5 65 9110.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Comte de Sang","color":"dark_red","bold":true}],CustomNameVisible:1b,equipment:{}}
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 2.5
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:700,name:"{\"text\":\"Le Comte de Sang\",\"color\":\"dark_red\",\"bold\":true}"}
execute unless score $wdup mg.st matches 1 run function mg:mobarena/cathedral/boss_init
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"Le Comte de Sang","color":"dark_red"}]
execute unless score $wdup mg.st matches 1 run execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Squelette archer","color":"yellow"},{"text":"  (sbires + boss)","color":"dark_gray"}]
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Comte de Sang","color":"dark_red","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
