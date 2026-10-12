# @s : zombie tué par une arme (à sa position)
execute store result score $zx2 mg.st if entity @e[type=minecraft:item_display,tag=mg.zpu]
execute if score $zx2 mg.st matches 2.. run return 0
execute store result score $zx2 mg.st run random value 1..100
execute if score $zx2 mg.st matches ..4 run function mg:zx/drop
