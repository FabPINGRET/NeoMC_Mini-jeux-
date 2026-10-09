# @s : dernier frame (jusqu'à 3 lancers : strike ou spare donnent les lancers bonus)
execute if score @s mg.brl matches 1 run return run function mg:bowl/l1
execute if score @s mg.brl matches 2 run return run function mg:bowl/l2
function mg:bowl/l3
