# @s : choix au tableau (trigger mg.tvms)
execute if score @s mg.tvms matches 9 run function mg:terra/abandon
execute if score @s mg.tvms matches 1..4 if score @s mg.tvm matches 1.. run tellraw @s {"text":"Tu as déjà une mission : termine-la ou abandonne-la au tableau.","color":"yellow"}
execute if score @s mg.tvms matches 1 unless score @s mg.tvm matches 1.. run function mg:terra/m1
execute if score @s mg.tvms matches 2 unless score @s mg.tvm matches 1.. run function mg:terra/m2
execute if score @s mg.tvms matches 3 unless score @s mg.tvm matches 1.. run function mg:terra/m3
execute if score @s mg.tvms matches 4 unless score @s mg.tvm matches 1.. run function mg:terra/m4
scoreboard players reset @s mg.tvms
scoreboard players enable @s mg.tvms
