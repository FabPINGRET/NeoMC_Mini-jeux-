# Toutes les 8 s : les grilles A et B s'échangent
scoreboard players add $jg mg.st 1
execute if score $jg mg.st matches 2.. run scoreboard players set $jg mg.st 0
execute if score $jv mg.st matches 1 if score $jg mg.st matches 0 run function mg:maze/gates_a_1
execute if score $jv mg.st matches 2 if score $jg mg.st matches 0 run function mg:maze/gates_a_2
execute if score $jv mg.st matches 3 if score $jg mg.st matches 0 run function mg:maze/gates_a_3
execute if score $jv mg.st matches 1 if score $jg mg.st matches 1 run function mg:maze/gates_b_1
execute if score $jv mg.st matches 2 if score $jg mg.st matches 1 run function mg:maze/gates_b_2
execute if score $jv mg.st matches 3 if score $jg mg.st matches 1 run function mg:maze/gates_b_3
playsound minecraft:block.iron_door.close master @a[tag=mg.play] 0 65 41100 0.01 0.8
