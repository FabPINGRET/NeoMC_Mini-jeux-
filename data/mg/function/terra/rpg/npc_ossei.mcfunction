# @s parle à ossei : dialogue selon l'étape de la campagne
execute if score @s mg.trch matches 20 run return run function mg:terra/rpg/d/ossei_20
execute if score @s mg.trch matches 28 run return run function mg:terra/rpg/d/ossei_28
execute if score @s mg.trch matches 35 run return run function mg:terra/rpg/d/ossei_35
execute if score @s mg.trch matches 70 run return run function mg:terra/rpg/d/ossei_70
return run function mg:terra/rpg/d/ossei_gen
