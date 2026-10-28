# @s : « Aller au Filon » (menu Échap, trigger mg.sv 9)
execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d'abord lancer /function mg:setup","color":"red"}
execute if entity @s[tag=mg.fnw] run return run tellraw @s {"text":"Tu es déjà au Filon.","color":"gray"}
execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : le Filon sera accessible après.","color":"red"}
execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : le Filon sera accessible après.","color":"red"}
execute if entity @s[tag=mg.dl] run return run tellraw @s [{"text":"⚔ Duel en cours : termine-le (ou abandonne-le) avant.","color":"red"}]
execute unless data storage mg:filon {built:1} unless score $fnb mg.st matches 1 run function mg:filon/build_start
execute unless data storage mg:filon {built:1} run return run tellraw @s {"text":"🚧 Le Filon se prépare (île en construction) : réessaie dans quelques secondes.","color":"yellow"}
execute if entity @s[tag=mg.surv] run function mg:survie/leave
execute in minecraft:overworld run function mg:filon/enter
