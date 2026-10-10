# @s = joueur qui abandonne (mg.xs 2, lien du message de lancement)
execute unless entity @s[tag=mg.xso] run return run tellraw @s [{"text":"⚠ Tu n'as pas de contre-la-montre en cours.","color":"red"}]
# phase 4 (après l'arrivée) : retour au lobby sans message d'abandon (le temps est déjà enregistré)
execute if score @s mg.xph matches 4 run return run function mg:elyrace/solo/stop
tellraw @a [{"selector":"@s","color":"yellow"},{"text":" abandonne le contre-la-montre.","color":"gray"}]
function mg:elyrace/solo/stop
