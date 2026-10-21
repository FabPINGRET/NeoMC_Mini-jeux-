# Invitation expirée (@s = invité)
execute unless score @s mg.dlto matches 1.. run return run tellraw @s [{"text":"Tu n'as aucune invitation de duel en attente.","color":"gray"}]
scoreboard players operation $dlt mg.st = @s mg.dlto
tag @s add mg.dltg
execute as @a[tag=mg.dlrq] if score @s mg.dlid = $dlt mg.st run function mg:duel/expire_c
tag @s remove mg.dltg
tellraw @s [{"text":"⚔ L'invitation au duel a expiré.","color":"gray"}]
execute if entity @s[tag=mg.dlui] run dialog clear @s
tag @s remove mg.dlui
scoreboard players reset @s mg.dlto
scoreboard players reset @s mg.dlx
