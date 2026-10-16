# Trigger mg.duel (@s = joueur) : 1 = liste des adversaires, 2 = accepter, 3 = refuser, 4 = annuler son invitation (sans effet pendant un duel),
# 5 = abandonner le duel (sans effet hors duel),
# 1000 + id = défier le joueur d'id mg.dlid (liste cliquable). Remis à zéro d'abord (core/tick le réactive)
scoreboard players operation #dlv mg.st = @s mg.duel
scoreboard players reset @s mg.duel
execute if score #dlv mg.st matches 1 run function mg:duel/list
execute if score #dlv mg.st matches 2 run function mg:duel/accept
execute if score #dlv mg.st matches 3 run function mg:duel/refuse
execute if score #dlv mg.st matches 4 run function mg:duel/cancel
execute if score #dlv mg.st matches 5 if entity @s[tag=mg.dl] run function mg:duel/forfeit
execute if score #dlv mg.st matches 1000.. run function mg:duel/challenge
