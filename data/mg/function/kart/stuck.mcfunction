# Bouton « Je suis coincé » (@s = pilote, son kart est tagué mg.kk) : remis sur la route au point de passage précédent, recharge 5 s
tag @s remove mg.kstuck
execute if entity @s[tag=mg.kfin] run return 0
execute if score @s mg.kstk matches 1.. run return run tellraw @s [{"text":"⛑ Patiente encore un peu avant de redemander (5 s).","color":"red"}]
scoreboard players set @s mg.kstk 100
function mg:kart/rescue
