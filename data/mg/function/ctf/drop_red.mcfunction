# Le porteur du drapeau ROUGE est tombé : le drapeau reste là (ou rentre s'il est tombé dans le vide)
tag @a remove mg.cfcr
execute as @e[type=minecraft:marker,tag=mg.cfpr,limit=1] at @s unless entity @s[y=-64,dy=141] run return run function mg:ctf/drop_here_red
function mg:ctf/return_red
