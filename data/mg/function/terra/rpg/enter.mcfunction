# @s arrive à Terra Nova (après le kit) : rappel de la campagne
tellraw @s [{"text":"⭐ Niveau ","color":"gold"},{"score":{"name":"@s","objective":"mg.trlv"},"color":"yellow","bold":true},{"text":"   📜 Campagne : ","color":"gold"},{"text":"[voir l'objectif]","color":"aqua","click_event":{"action":"run_command","command":"/trigger mg.trtk set 9"}}]
function mg:terra/rpg/obj_say
function mg:terra/rpg/qloc
execute if score @s mg.trcl matches 0 run tellraw @s [{"text":"🎖 Choisis ta classe auprès de la Commandante Varga (QG) : ","color":"gold"},{"text":"[choisir]","color":"yellow","click_event":{"action":"run_command","command":"/trigger mg.trtk set 600"}}]
