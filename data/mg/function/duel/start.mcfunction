# Départ du duel (@s = invité = départ sud ; le défieur porte mg.dlca = départ nord ; $dli = arène)
tag @a[tag=mg.dlca] add mg.dla
# l'invitation est fermée AVANT setup (elle remet mg.dlx à zéro, que spawn utilise pour la protection)
function mg:duel/inv_end
execute as @a[tag=mg.dlca] run function mg:duel/setup
function mg:duel/setup
execute if score $dli mg.st matches 1 run tellraw @a[tag=mg.dl,scores={mg.dli=1}] [{"text":"⚔ Duel sniper : ","color":"gold"},{"selector":"@a[tag=mg.dla,scores={mg.dli=1}]","color":"white"},{"text":" contre ","color":"gray"},{"selector":"@a[tag=mg.dl,tag=!mg.dla,scores={mg.dli=1}]","color":"white"},{"text":" - Canyon - premier à 3 manches. Tête = élimination, corps = 2 touches. Accroupi = lunette. Abandon : trigger mg.duel 5.","color":"gray"}]
execute if score $dli mg.st matches 2 run tellraw @a[tag=mg.dl,scores={mg.dli=2}] [{"text":"⚔ Duel sniper : ","color":"gold"},{"selector":"@a[tag=mg.dla,scores={mg.dli=2}]","color":"white"},{"text":" contre ","color":"gray"},{"selector":"@a[tag=mg.dl,tag=!mg.dla,scores={mg.dli=2}]","color":"white"},{"text":" - Ville - premier à 3 manches. Tête = élimination, corps = 2 touches. Accroupi = lunette. Abandon : trigger mg.duel 5.","color":"gray"}]
execute if score $dli mg.st matches 3 run tellraw @a[tag=mg.dl,scores={mg.dli=3}] [{"text":"⚔ Duel sniper : ","color":"gold"},{"selector":"@a[tag=mg.dla,scores={mg.dli=3}]","color":"white"},{"text":" contre ","color":"gray"},{"selector":"@a[tag=mg.dl,tag=!mg.dla,scores={mg.dli=3}]","color":"white"},{"text":" - Glacier - premier à 3 manches. Tête = élimination, corps = 2 touches. Accroupi = lunette. Abandon : trigger mg.duel 5.","color":"gray"}]
