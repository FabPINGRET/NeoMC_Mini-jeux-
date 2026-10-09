# Achat de $gpt : désormais disponible gratuitement à la villa, pour tout le monde
execute if score $gpt mg.st matches 2 run data modify storage mg:gta unl.t2 set value 1b
execute if score $gpt mg.st matches 3 run data modify storage mg:gta unl.t3 set value 1b
execute if score $gpt mg.st matches 4 run data modify storage mg:gta unl.t4 set value 1b
execute if score $gpt mg.st matches 5 run data modify storage mg:gta unl.t5 set value 1b
execute if score $gpt mg.st matches 6 run data modify storage mg:gta unl.t6 set value 1b
execute if score $gpt mg.st matches 7 run data modify storage mg:gta unl.t7 set value 1b
execute if score $gpt mg.st matches 9 run data modify storage mg:gta unl.t9 set value 1b
execute if score $gpt mg.st matches 21 run data modify storage mg:gta unl.t21 set value 1b
execute if score $gpt mg.st matches 22 run data modify storage mg:gta unl.t22 set value 1b
execute if score $gpt mg.st matches 23 run data modify storage mg:gta unl.t23 set value 1b
execute if score $gpt mg.st matches 24 run data modify storage mg:gta unl.t24 set value 1b
execute if score $gpt mg.st matches 25 run data modify storage mg:gta unl.t25 set value 1b
execute if score $gpt mg.st matches 2..9 run tellraw @s {"text":"🏠 Débloqué : il est aussi au râtelier de la villa, gratuit pour tous.","color":"aqua"}
execute if score $gpt mg.st matches 21..25 run tellraw @s {"text":"🏠 Débloqué : il est aussi au garage de la villa, gratuit pour tous.","color":"aqua"}
