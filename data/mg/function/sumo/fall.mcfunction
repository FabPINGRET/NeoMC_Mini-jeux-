# Un joueur est tombé (@s = joueur) : une vie en moins, retour sur la plateforme ou élimination
scoreboard players remove @s mg.lv 1
execute if score @s mg.lv matches ..0 run return run function mg:core/eliminate
tellraw @a [{"selector":"@s","color":"red"},{"text":" est éjecté ! Vies restantes : ","color":"gray"},{"score":{"name":"@s","objective":"mg.lv"},"color":"gold"}]
title @s actionbar [{"text":"♥ Vies restantes : ","color":"red"},{"score":{"name":"@s","objective":"mg.lv"},"color":"gold"}]
playsound minecraft:entity.player.hurt master @a ~ ~ ~ 1 0.8
execute if score $sr2 mg.st matches 16 run spreadplayers 0 5500 2 13 under 90 false @s
execute if score $sr2 mg.st matches 10 run spreadplayers 0 4900 3 9 under 85 false @s
execute if score $sr2 mg.st matches 8 run spreadplayers 0 4900 3 7 under 85 false @s
execute if score $sr2 mg.st matches 6 run spreadplayers 0 4900 2 5 under 85 false @s
effect give @s minecraft:slow_falling 1 0 true
