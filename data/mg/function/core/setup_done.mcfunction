# Toute la génération est terminée
tellraw @a [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"✔ Génération terminée ","color":"green","bold":true},{"text":"(spawn, arènes, circuits, parcours, hall…). Le serveur est prêt !","color":"gray"}]
title @a[tag=mg.admin] title {"text":"✔ Génération terminée","color":"green","bold":true}
title @a[tag=mg.admin] subtitle {"text":"le serveur est prêt","color":"gray"}
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
