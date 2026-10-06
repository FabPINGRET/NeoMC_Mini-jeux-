# Fin de la roulette : le dernier jeu tiré est confirmé
function mg:party/pick
title @a[tag=mg.mpp] times 0 50 10
title @a[tag=mg.mpp] subtitle [{"text":"C'est parti !","color":"green","bold":true}]
execute as @a[tag=mg.mpp] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.4
