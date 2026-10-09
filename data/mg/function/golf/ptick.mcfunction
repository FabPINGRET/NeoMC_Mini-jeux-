# @s : joueur, chaque tick
execute if entity @s[y=-64,dy=110] run function mg:golf/rescue
execute if score @s mg.gfs matches 0 run function mg:golf/aim
