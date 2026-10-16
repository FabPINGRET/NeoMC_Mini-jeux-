# @s parle à nyla : dialogue selon l'étape de la campagne
execute if score @s mg.trch matches 52 run return run function mg:terra/rpg/d/nyla_52
execute if score @s mg.trch matches 58 run return run function mg:terra/rpg/d/nyla_58
return run function mg:terra/rpg/d/nyla_gen
