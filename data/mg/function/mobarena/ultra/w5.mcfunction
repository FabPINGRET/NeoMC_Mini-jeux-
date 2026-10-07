# Ultra — vague 5
summon minecraft:vindicator 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:ravager 0.5 64 1789.5 {Tags:["mg.mob","mg.bossn"],PersistenceRequired:1b,CustomName:[{"text":"Le Broyeur","color":"dark_red","bold":true}],CustomNameVisible:1b}
execute as @e[tag=mg.bossn] run function mg:mobarena/boss_make {hp:200,name:"{\"text\":\"Le Broyeur\",\"color\":\"dark_red\",\"bold\":true}"}
title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"Le Broyeur","color":"dark_red"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.8 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Vindicateur","color":"yellow"},{"text":"  (4 monstres + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"Le Broyeur","color":"dark_red","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
