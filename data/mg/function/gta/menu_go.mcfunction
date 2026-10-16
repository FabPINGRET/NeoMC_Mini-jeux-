# @s : « Aller dans Neo GTA » du menu Échap (trigger mg.sv 4), d'où qu'on soit hors partie
execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d'abord lancer /function mg:setup","color":"red"}
execute if entity @s[tag=mg.gtw] run return run tellraw @s {"text":"Tu es déjà dans Neo GTA.","color":"gray"}
execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : Neo GTA sera accessible après.","color":"red"}
execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : Neo GTA sera accessible après.","color":"red"}
execute if entity @s[tag=mg.dl] run return run tellraw @s [{"text":"⚔ Duel en cours : termine-le (ou abandonne-le) avant.","color":"red"}]
execute if entity @s[tag=mg.surv] run function mg:survie/leave
execute in minecraft:overworld run function mg:gta/enter
