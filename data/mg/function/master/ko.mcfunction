# @s a raté
tag @s remove mg.msk
execute if score $msv mg.st matches 0 run tellraw @a[tag=!mg.surv] [{"text":"👑 ","color":"gold"},{"selector":"@s","color":"red"},{"text":" est tombé dans le piège !","color":"gray"}]
execute if score $msv mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"👑 ","color":"gold"},{"selector":"@s","color":"red"},{"text":" a été trop lent !","color":"gray"}]
scoreboard players add @s mg.msm 1
execute if score $n0 mg.st matches 2.. run return run function mg:core/eliminate
title @s actionbar {"text":"✖ Raté ! (entraînement)","color":"red"}
