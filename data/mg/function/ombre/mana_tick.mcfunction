# @s : +2 mana par seconde (+1 tous les 3 points d'Esprit, +2 mage), barre d'XP
scoreboard players operation $e mg.st = @s mg.ols4
scoreboard players operation $e mg.st /= #3 mg.st
scoreboard players add $e mg.st 2
execute if score @s mg.olcl matches 3 run scoreboard players add $e mg.st 2
scoreboard players operation @s mg.olmp += $e mg.st
execute if score @s mg.olmp > @s mg.olmm run scoreboard players operation @s mg.olmp = @s mg.olmm
function mg:ombre/mana_bar
