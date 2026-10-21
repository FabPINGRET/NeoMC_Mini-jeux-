# Joueur reconnecté (core/reconnect, @s = joueur) : duel périmé et invitations effacés
execute if entity @s[tag=mg.dl] run function mg:duel/stop
tag @s remove mg.dlrq
tag @s remove mg.dlui
scoreboard players reset @s mg.dlto
scoreboard players reset @s mg.dlx
