# Lit ROUGE détruit
scoreboard players set $bed_red mg.st 0
execute as @a[team=mg_red] run spawnpoint @s 0 85 1200
title @a title [{"text":"⚠","color":"red","bold":true}]
title @a subtitle [{"text":"Le lit ROUGE a été détruit !","color":"red"}]
tellraw @a [{"text":"⚠ Le lit de l'équipe ","color":"gray"},{"text":"ROUGE","color":"red","bold":true},{"text":" est détruit — plus de réapparition pour eux !","color":"gray"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.6 1
particle minecraft:explosion_emitter -34.5 65 1200.5 0 0 0 0 1
