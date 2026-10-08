# Forge — vague 20 : BOSS Le Golem de Basalte
summon minecraft:piglin_brute 12.6 66 10303.3 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 9.2 66 10309.2 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute 3.4 66 10312.6 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:piglin_brute -3.3 66 10312.6 {Tags:["mg.mob","mg.fz","mg.fs"],PersistenceRequired:1b,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}}}
summon minecraft:blaze 24.5 74 10300.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -23.5 74 10300.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 74 10324.5 {Tags:["mg.mob"],PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 0 true
effect give @e[tag=mg.fs] minecraft:strength infinite 0 true
effect give @e[tag=mg.fz1] minecraft:speed infinite 0 true
tag @e[tag=mg.fz] remove mg.fz
tag @e[tag=mg.fs] remove mg.fs
tag @e[tag=mg.fz1] remove mg.fz1
execute unless score $wdup mg.st matches 1 run summon minecraft:iron_golem 0.5 66 10300.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Golem de Basalte","color":"gold","bold":true}],CustomNameVisible:1b}
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 3
execute unless score $wdup mg.st matches 1 run execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:1000,name:"{\"text\":\"Le Golem de Basalte\",\"color\":\"gold\",\"bold\":true}"}
execute unless score $wdup mg.st matches 1 run function mg:mobarena/forge/boss_init
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
execute unless score $wdup mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"Le Golem de Basalte","color":"gold"}]
execute unless score $wdup mg.st matches 1 run execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Piglin furieux, 3× Blaze (tourelle)","color":"yellow"},{"text":"  (sbires + boss)","color":"dark_gray"}]
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Golem de Basalte","color":"gold","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
