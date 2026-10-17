# @s a fait un clic droit avec l'objet : 1er clic = demande de confirmation (3 s), 2e clic = on passe le niveau
scoreboard players reset @s mg.qs
execute unless score $state mg.st matches 2 run return 0
# bouton maintenu : l'utilisation se répète toutes les 4 ticks, mg.dku l'absorbe (seul un vrai nouveau clic confirme)
execute if score @s mg.dku matches 1.. run return run scoreboard players set @s mg.dku 6
scoreboard players set @s mg.dku 6
execute if score @s mg.dkc matches 1.. run return run function mg:dropadv/k_skip
scoreboard players set @s mg.dkc 60
title @s actionbar "⏭ Clic droit encore pour passer (ne comptera pas)"
execute at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2
