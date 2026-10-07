# Lit JAUNE détruit
scoreboard players set $bed_yellow mg.st 0
execute as @a[team=mg_yellow] run spawnpoint @s 0 85 1200
title @a[tag=!mg.surv] title [{"text":"⚠","color":"yellow","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"Le lit JAUNE a été détruit !","color":"yellow"}]
tellraw @a [{"text":"⚠ Le lit de l'équipe ","color":"gray"},{"text":"JAUNE","color":"yellow","bold":true},{"text":" est détruit — plus de réapparition pour eux !","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.6 1
particle minecraft:explosion_emitter 0.5 65 1236.5 0 0 0 0 1
