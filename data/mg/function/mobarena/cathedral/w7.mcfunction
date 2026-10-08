# Cathédrale — vague 7
summon minecraft:skeleton -11.5 70 9084.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9084.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton -11.5 70 9088.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9088.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton -11.5 70 9092.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:skeleton 11.5 70 9092.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1},head:{id:"minecraft:iron_helmet",count:1}}}
summon minecraft:zombie -7.5 65 9116.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},legs:{id:"minecraft:iron_leggings",count:1},feet:{id:"minecraft:iron_boots",count:1},mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:zombie -3.5 65 9116.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},legs:{id:"minecraft:iron_leggings",count:1},feet:{id:"minecraft:iron_boots",count:1},mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:zombie 0.5 65 9116.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},legs:{id:"minecraft:iron_leggings",count:1},feet:{id:"minecraft:iron_boots",count:1},mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:zombie 4.5 65 9116.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},legs:{id:"minecraft:iron_leggings",count:1},feet:{id:"minecraft:iron_boots",count:1},mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:zombie 8.5 65 9116.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},legs:{id:"minecraft:iron_leggings",count:1},feet:{id:"minecraft:iron_boots",count:1},mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:zombie -7.5 65 9119.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},legs:{id:"minecraft:iron_leggings",count:1},feet:{id:"minecraft:iron_boots",count:1},mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:bat -7.5 74 9084.5 {Tags:["mg.mob","mg.swarm"],PersistenceRequired:1b}
summon minecraft:bat -3.5 74 9084.5 {Tags:["mg.mob","mg.swarm"],PersistenceRequired:1b}
summon minecraft:bat 0.5 74 9084.5 {Tags:["mg.mob","mg.swarm"],PersistenceRequired:1b}
summon minecraft:bat 4.5 74 9084.5 {Tags:["mg.mob","mg.swarm"],PersistenceRequired:1b}
summon minecraft:bat 8.5 74 9084.5 {Tags:["mg.mob","mg.swarm"],PersistenceRequired:1b}
summon minecraft:bat -7.5 74 9092.5 {Tags:["mg.mob","mg.swarm"],PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 1 true
tag @e[tag=mg.fz] remove mg.fz
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Squelette archer, 6× Zombie en armure de fer rapide, 6× Chauve-souris maudite","color":"yellow"},{"text":"  (18 monstres)","color":"dark_gray"}]
