# @s = joueur qui abandonne (mg.xs 2, lien du message de lancement)
execute unless entity @s[tag=mg.xso] run return run tellraw @s [{"text":"⚠ Tu n'as pas de contre-la-montre en cours.","color":"red"}]
tellraw @a [{"selector":"@s","color":"yellow"},{"text":" abandonne le contre-la-montre.","color":"gray"}]
function mg:elyrace/solo/stop
