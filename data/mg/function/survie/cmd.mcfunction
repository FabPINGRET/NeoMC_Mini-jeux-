# Trigger mg.sv (@s) : 1 = aller en survie, 2 = retour au lobby des mini-jeux
execute if score @s mg.sv matches 1 run function mg:survie/enter
execute if score @s mg.sv matches 2 run function mg:survie/leave
execute if score @s mg.sv matches 3 run function mg:aide
execute if score @s mg.sv matches 4 run function mg:gta/menu_go
scoreboard players reset @s mg.sv
