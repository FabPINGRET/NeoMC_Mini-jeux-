# Volant — vague 10
summon minecraft:vex 11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:phantom 11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 0.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 11.5 68 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run summon minecraft:ghast 0.5 72 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Seigneur des Cieux","color":"aqua","bold":true}],CustomNameVisible:1b}
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 1.5
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:300,name:"{\"text\":\"Le Seigneur des Cieux\",\"color\":\"aqua\",\"bold\":true}"}
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"Le Seigneur des Cieux","color":"aqua"}]
execute unless score $wdup mg.st matches 1 run execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Vex, 8× Phantom","color":"yellow"},{"text":"  (16 monstres + boss)","color":"dark_gray"}]
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Seigneur des Cieux","color":"aqua","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
