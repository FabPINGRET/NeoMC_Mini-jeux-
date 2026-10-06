# Mouton spécial — applique l'apparence/le type selon $ty (1..8), @s = le mouton qui vient d'être lancé
execute if score $ty mg.st matches 1 run function mg:sheepwar/sp_space
execute if score $ty mg.st matches 2 run function mg:sheepwar/sp_nausea
execute if score $ty mg.st matches 3 run function mg:sheepwar/sp_freeze
execute if score $ty mg.st matches 4 run function mg:sheepwar/sp_blind
execute if score $ty mg.st matches 5 run function mg:sheepwar/sp_fire
execute if score $ty mg.st matches 6 run function mg:sheepwar/sp_super
execute if score $ty mg.st matches 7 run function mg:sheepwar/sp_ultra
execute if score $ty mg.st matches 8 run function mg:sheepwar/sp_mitra
