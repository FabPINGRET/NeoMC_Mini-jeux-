# Demande de lancement d'un jeu (@s = demandeur, mg.go = id du jeu)

# Valeur invalide ?
execute unless score @s mg.go matches 1..85 unless score @s mg.go matches 100..196 run return run scoreboard players reset @s mg.go

# Réservé aux admins
execute unless entity @s[tag=mg.admin] unless entity @s[tag=mg.vauto] run tellraw @s [{"text":"⚠ Seul un admin peut lancer un jeu.","color":"red"}]
execute unless entity @s[tag=mg.admin] unless entity @s[tag=mg.vauto] run return run scoreboard players reset @s mg.go

# Setup pas fait ?
execute if score $setup mg.st matches 0 run tellraw @s [{"text":"⚠ Installation manquante : un OP doit d'abord lancer ","color":"red"},{"text":"/function mg:setup","color":"yellow"}]
execute if score $setup mg.st matches 0 run return run scoreboard players reset @s mg.go

# Déjà une partie en cours ?
execute unless score $state mg.st matches 0 run tellraw @s [{"text":"⚠ Une partie est déjà en cours ! (menu → Arrêter la partie)","color":"red"}]
execute unless score $state mg.st matches 0 run return run scoreboard players reset @s mg.go

function mg:core/request
