# @s = joueur en phase 4 (choix ; appelée par step avant toute règle de course) : à 600 ticks (30 s) sans clic, retour au lobby ;
# sinon compte à rebours dans la barre d'action, une fois par seconde (mg.xst = ticks depuis le début du choix)
execute if score @s mg.xst matches 600.. run tellraw @s [{"text":"⌂ Pas de réponse : retour au lobby.","color":"gray"}]
execute if score @s mg.xst matches 600.. run return run function mg:elyrace/solo/stop
scoreboard players operation #xm mg.st = @s mg.xst
scoreboard players operation #xm mg.st %= #k20 mg.st
execute unless score #xm mg.st matches 0 run return 0
scoreboard players set #xw mg.st 600
scoreboard players operation #xw mg.st -= @s mg.xst
scoreboard players operation #xw mg.st /= #k20 mg.st
title @s actionbar [{"text":"⟲ Rejouer ou retour au lobby : ","color":"gray"},{"score":{"name":"#xw","objective":"mg.st"},"color":"white"},{"text":" s","color":"gray"}]
