# Lancer trop rapproché : on rend le même mouton (@s = joueur, $ty = type)
execute if score $ty mg.st matches 0 run function mg:sheepwar/give_ammo {n:1}
execute if score $ty mg.st matches 1 run function mg:sheepwar/give_space
execute if score $ty mg.st matches 2 run function mg:sheepwar/give_nausea
execute if score $ty mg.st matches 3 run function mg:sheepwar/give_freeze
execute if score $ty mg.st matches 4 run function mg:sheepwar/give_blind
execute if score $ty mg.st matches 5 run function mg:sheepwar/give_fire
execute if score $ty mg.st matches 6 run function mg:sheepwar/give_super
execute if score $ty mg.st matches 7 run function mg:sheepwar/give_ultra
execute if score $ty mg.st matches 8 run function mg:sheepwar/give_mitra
