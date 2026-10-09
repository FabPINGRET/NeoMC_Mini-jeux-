# @s = joueur qui abandonne (mg.xs 2, lien du message de lancement)
execute unless score $xs mg.st matches 1 run return run tellraw @s [{"text":"⚠ Aucun contre-la-montre en cours.","color":"red"}]
execute unless entity @s[tag=mg.play] run return run tellraw @s [{"text":"⚠ Ce n'est pas ton contre-la-montre.","color":"red"}]
execute unless score $state mg.st matches 1..2 run return 0
tellraw @a [{"selector":"@s","color":"yellow"},{"text":" abandonne le contre-la-montre.","color":"gray"}]
function mg:elyrace/solo/end
