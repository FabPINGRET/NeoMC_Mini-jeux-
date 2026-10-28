# Trigger mg.sv (@s) : 1 = aller en survie, 2 = retour au lobby des mini-jeux, 3 = aide, 4 = Neo GTA, 7 = Terra Nova, 8 = Ombrelune, 9 = Filon,
# 5 = menu admin (admins), 6 = menu Échap (lanceur esc_menu : version admin ou joueur)
execute if score @s mg.sv matches 1 run function mg:survie/enter
execute if score @s mg.sv matches 2 run function mg:survie/leave
execute if score @s mg.sv matches 3 run function mg:aide
execute if score @s mg.sv matches 4 run function mg:gta/menu_go
execute if score @s mg.sv matches 7 run function mg:terra/menu_go
execute if score @s mg.sv matches 8 run function mg:ombre/menu_go
execute if score @s mg.sv matches 9 run function mg:filon/menu_go
execute if score @s mg.sv matches 5 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Réservé aux admins.","color":"red"}
execute if score @s mg.sv matches 5 if entity @s[tag=mg.admin] run function mg:core/menu_use
execute if score @s mg.sv matches 6 if entity @s[tag=mg.admin] run function mg:rate/d/main_menu_admin
execute if score @s mg.sv matches 6 unless entity @s[tag=mg.admin] run function mg:rate/d/main_menu
scoreboard players reset @s mg.sv
