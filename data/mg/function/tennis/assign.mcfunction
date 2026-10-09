# @s : joueur suivant (ordre aléatoire) → court $tni/2 + 1, côté $tni%2 + 1 ; au-delà de 8 : spectateur
execute if score $tni mg.st matches 8.. run tellraw @s {"text":"🎾 Tous les courts sont pris : tu regardes ce tournoi.","color":"gray"}
execute if score $tni mg.st matches 8.. run return run function mg:core/eliminate
scoreboard players operation @s mg.tnc = $tni mg.st
scoreboard players operation @s mg.tnc /= #tn2 mg.st
scoreboard players add @s mg.tnc 1
scoreboard players operation @s mg.tns = $tni mg.st
scoreboard players operation @s mg.tns %= #tn2 mg.st
scoreboard players add @s mg.tns 1
scoreboard players add $tni mg.st 1
