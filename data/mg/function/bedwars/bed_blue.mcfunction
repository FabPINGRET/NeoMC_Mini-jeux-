# Lit BLEU détruit
scoreboard players set $bed_blue mg.st 0
execute as @a[team=mg_blue] run spawnpoint @s 0 85 1200
title @a title [{"text":"⚠","color":"blue","bold":true}]
title @a subtitle [{"text":"Le lit BLEU a été détruit !","color":"blue"}]
tellraw @a [{"text":"⚠ Le lit de l'équipe ","color":"gray"},{"text":"BLEUE","color":"blue","bold":true},{"text":" est détruit — plus de réapparition pour eux !","color":"gray"}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.6 1
particle minecraft:explosion_emitter 35.5 65 1200.5 0 0 0 0 1
