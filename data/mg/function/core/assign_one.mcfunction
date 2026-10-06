# Affecte @s à une équipe (rotation)
execute if score $ti mg.st matches 0 run team join mg_red @s
execute if score $ti mg.st matches 1 run team join mg_blue @s
execute if score $ti mg.st matches 2 run team join mg_green @s
execute if score $ti mg.st matches 3 run team join mg_yellow @s
scoreboard players add $ti mg.st 1
execute if score $ti mg.st >= $nt mg.st run scoreboard players set $ti mg.st 0
