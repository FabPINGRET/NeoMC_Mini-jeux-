# @s (zombie) : masque qui fait peur au hasard (resource pack, objet sur la tête)
execute store result score $zx3 mg.st run random value 1..4
execute if score $zx3 mg.st matches 1 run return run function mg:zx/mask_n {n:1}
execute if score $zx3 mg.st matches 2 run return run function mg:zx/mask_n {n:2}
execute if score $zx3 mg.st matches 3 run return run function mg:zx/mask_n {n:3}
execute if score $zx3 mg.st matches 4 run return run function mg:zx/mask_n {n:4}
