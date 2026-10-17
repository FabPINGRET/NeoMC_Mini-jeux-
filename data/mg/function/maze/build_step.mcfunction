# Étape $jbs de la construction
execute if score $jbs mg.st matches 1 run function mg:maze/build_1
execute if score $jbs mg.st matches 2 run function mg:maze/build_2
execute if score $jbs mg.st matches 3 run function mg:maze/build_3
execute if score $jbs mg.st matches 4 run function mg:maze/build_4
execute if score $jbs mg.st matches 5 run function mg:maze/build_5
execute if score $jbs mg.st matches 6 run function mg:maze/build_6
scoreboard players add $jbs mg.st 1
execute if score $jbs mg.st matches ..6 run schedule function mg:maze/build_step 2t
