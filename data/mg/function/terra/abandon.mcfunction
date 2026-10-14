# @s abandonne sa mission
execute unless score @s mg.tvm matches 1.. run return run tellraw @s {"text":"Pas de mission en cours.","color":"gray"}
function mg:terra/mis_clear
tellraw @s {"text":"✖ Mission abandonnée.","color":"gray"}
