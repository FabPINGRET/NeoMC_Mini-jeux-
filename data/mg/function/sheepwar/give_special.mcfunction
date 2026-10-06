# Donne un mouton spécial au hasard à @s (1..9 : 5 effets, 6-7 super, 8 ultra, 9 mitraillette)
execute store result score $r2 mg.st run random value 1..9
execute if score $r2 mg.st matches 1 run function mg:sheepwar/give_space
execute if score $r2 mg.st matches 2 run function mg:sheepwar/give_nausea
execute if score $r2 mg.st matches 3 run function mg:sheepwar/give_freeze
execute if score $r2 mg.st matches 4 run function mg:sheepwar/give_blind
execute if score $r2 mg.st matches 5 run function mg:sheepwar/give_fire
execute if score $r2 mg.st matches 6..7 run function mg:sheepwar/give_super
# Ultra explosif rare : tirage 8 puis seulement 1 chance sur 3, sinon mouton normal (≈ 1/27 des spéciaux)
execute store result score $r3 mg.st run random value 0..2
execute if score $r2 mg.st matches 8 if score $r3 mg.st matches 0 run function mg:sheepwar/give_ultra
execute if score $r2 mg.st matches 8 unless score $r3 mg.st matches 0 run function mg:sheepwar/give_ammo {n:1}
execute if score $r2 mg.st matches 9 run function mg:sheepwar/give_mitra
