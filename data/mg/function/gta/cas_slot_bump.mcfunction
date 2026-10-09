# @s : trois symboles pareils sur un tirage perdant → le troisième change
scoreboard players add @s mg.gs3 1
execute if score @s mg.gs3 matches 6.. run scoreboard players set @s mg.gs3 0
execute if score @s mg.gs1 matches 0 if score @s mg.gs3 matches 0 run scoreboard players set @s mg.gs3 1
