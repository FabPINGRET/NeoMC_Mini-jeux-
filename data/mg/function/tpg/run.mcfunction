# mg.opt 62.. : TP général (@s = joueur)
execute unless entity @s[tag=mg.admin] run return run tellraw @s {"text":"⚠ Réservé aux admins.","color":"red"}
execute if score @s mg.opt matches 62 run return run function mg:tpg/open
execute if score @s mg.opt matches 63 run function mg:tpg/survie
execute if score @s mg.opt matches 64 run function mg:tpg/gta
execute if score @s mg.opt matches 65 run function mg:tpg/lobby
