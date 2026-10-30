# Fin d'une partie jouée seul : entraînement, aucune victoire créditée (appelé par core/win_* quand $n0 < 2)
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 60
title @a[tag=!mg.surv] title [{"text":"Fin de l'entraînement","color":"gray"}]
tellraw @a [{"text":"Partie terminée — seul, pas de victoire comptée (il faut au moins 2 participants).","color":"gray"}]
