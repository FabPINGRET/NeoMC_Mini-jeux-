# @s parle à varga : dialogue selon l'étape de la campagne
execute if score @s mg.trch matches 0 run return run function mg:terra/rpg/d/varga_0
execute if score @s mg.trch matches 15 run return run function mg:terra/rpg/d/varga_15
execute if score @s mg.trch matches 45 run return run function mg:terra/rpg/d/varga_45
execute if score @s mg.trch matches 66 run return run function mg:terra/rpg/d/varga_66
execute if score @s mg.trch matches 90 run return run function mg:terra/rpg/d/varga_90
execute if score @s mg.trch matches 100 run return run function mg:terra/rpg/d/varga_100
return run function mg:terra/rpg/d/varga_gen
