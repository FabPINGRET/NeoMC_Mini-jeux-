# Laboratoire — vague 20 : BOSS L'Abomination Toxique
summon minecraft:zombie 14.5 65 9500.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie -13.5 65 9500.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 0.5 65 9514.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 0.5 65 9486.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:witch 10.5 65 9510.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch -9.5 65 9510.5 {Tags:["mg.mob"],PersistenceRequired:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 1 true
tag @e[tag=mg.fz] remove mg.fz
summon minecraft:iron_golem 0.5 65 9506.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"L'Abomination Toxique","color":"green","bold":true}],CustomNameVisible:1b}
execute as @e[tag=mg.bossn] run attribute @s minecraft:scale base set 2.6
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:800,name:"{\"text\":\"L\'Abomination Toxique\",\"color\":\"green\",\"bold\":true}"}
function mg:mobarena/lab/boss_init
title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"L'Abomination Toxique","color":"green"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Zombie de laboratoire (Speed II), 2× Sorcière","color":"yellow"},{"text":"  (sbires + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"L'Abomination Toxique","color":"green","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
