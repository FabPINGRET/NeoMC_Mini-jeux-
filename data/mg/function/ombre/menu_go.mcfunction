# @s : « Aller à Ombrelune » (menu Échap, trigger mg.sv 8)
execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d'abord lancer /function mg:setup","color":"red"}
execute if entity @s[tag=mg.olw] run return run tellraw @s {"text":"Tu es déjà à Ombrelune.","color":"gray"}
execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : Ombrelune sera accessible après.","color":"red"}
execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : Ombrelune sera accessible après.","color":"red"}
execute if entity @s[tag=mg.dl] run return run tellraw @s [{"text":"⚔ Duel en cours : termine-le (ou abandonne-le) avant.","color":"red"}]
execute if entity @s[tag=mg.gtw] run function mg:gta/leave
execute if entity @s[tag=mg.tvw] run function mg:terra/leave
execute if entity @s[tag=mg.surv] run function mg:survie/leave
execute in minecraft:overworld run function mg:ombre/enter
