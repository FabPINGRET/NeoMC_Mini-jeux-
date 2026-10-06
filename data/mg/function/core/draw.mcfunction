# Fin sans vainqueur
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 60
title @a title [{"text":"Partie terminée","color":"gray"}]
tellraw @a [{"text":"Partie terminée — pas de vainqueur cette fois.","color":"gray"}]
