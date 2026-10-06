# Bascule caméra suivie / vue libre (@s)
execute store success score $tmp mg.st if entity @s[tag=mg.mpfree]
execute if score $tmp mg.st matches 1 run tag @s remove mg.mpfree
execute if score $tmp mg.st matches 1 run tellraw @s [{"text":"🎥 Caméra : tu tournes autour du joueur actif avec la souris.","color":"aqua"}]
execute if score $tmp mg.st matches 0 run tag @s add mg.mpfree
execute if score $tmp mg.st matches 0 run tellraw @s [{"text":"✈ Vue libre : vole où tu veux. ","color":"aqua"},{"text":"[revenir à la caméra]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.dice set 4"}}]
