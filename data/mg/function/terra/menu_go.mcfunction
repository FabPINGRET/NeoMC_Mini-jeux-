# @s : « Aller à Terra Nova » du menu Échap (trigger mg.sv 7), d'où qu'on soit hors partie
execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d'abord lancer /function mg:setup","color":"red"}
execute unless data storage mg:terra built run return run tellraw @s {"text":"🚧 Terra Nova est en construction, réessaie bientôt.","color":"yellow"}
execute if entity @s[tag=mg.tvw] run return run tellraw @s {"text":"Tu es déjà à Terra Nova.","color":"gray"}
execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : Terra Nova sera accessible après.","color":"red"}
execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : Terra Nova sera accessible après.","color":"red"}
execute if entity @s[tag=mg.dl] run return run tellraw @s [{"text":"⚔ Duel en cours : termine-le (ou abandonne-le) avant.","color":"red"}]
execute if entity @s[tag=mg.surv] run function mg:survie/leave
execute in minecraft:overworld run function mg:terra/enter
