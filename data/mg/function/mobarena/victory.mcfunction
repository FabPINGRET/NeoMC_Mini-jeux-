# Mob Arena — VICTOIRE collective
tag @a[tag=mg.play] add mg.win
scoreboard players add @a[tag=mg.play] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 140
title @a[tag=!mg.surv] title [{"text":"VICTOIRE !","color":"gold","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"Les ","color":"yellow"},{"score":{"name":"$wmax","objective":"mg.st"},"color":"yellow"},{"text":" vagues ont été repoussées !","color":"yellow"}]
tellraw @a [{"text":"★ L'arène est nettoyée — bravo aux survivants !","color":"gold"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
