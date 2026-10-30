# Prime déjà touchée il y a moins d'une minute : rien de plus
scoreboard players remove @s mg.gkp 1
title @s actionbar {"text":"Joueur éliminé — prime déjà touchée il y a moins d'une minute","color":"gray"}
execute if score @s mg.gkp matches 1.. run function mg:gta/kill_player_cd
