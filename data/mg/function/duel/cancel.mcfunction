# Annuler son invitation (@s = défieur) ; ignoré pendant un duel (bouton périmé : l'abandon est le trigger 5)
execute if entity @s[tag=mg.dl] run return 0
execute unless entity @s[tag=mg.dlrq] run return run tellraw @s [{"text":"Tu n'as aucune invitation à annuler.","color":"gray"}]
scoreboard players operation $dlt mg.st = @s mg.dlid
tag @s add mg.dlca
execute as @a[scores={mg.dlto=1..}] if score @s mg.dlto = $dlt mg.st run function mg:duel/cancel_t
tag @s remove mg.dlca
tag @s remove mg.dlrq
tellraw @s [{"text":"⚔ Invitation annulée.","color":"gray"}]
