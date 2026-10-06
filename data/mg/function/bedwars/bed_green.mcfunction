# Lit VERT détruit
scoreboard players set $bed_green mg.st 0
execute as @a[team=mg_green] run spawnpoint @s 0 85 1200
title @a title [{"text":"⚠","color":"green","bold":true}]
title @a subtitle [{"text":"Le lit VERT a été détruit !","color":"green"}]
tellraw @a [{"text":"⚠ Le lit de l'équipe ","color":"gray"},{"text":"VERTE","color":"green","bold":true},{"text":" est détruit — plus de réapparition pour eux !","color":"gray"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.6 1
particle minecraft:explosion_emitter 0.5 65 1164.5 0 0 0 0 1
