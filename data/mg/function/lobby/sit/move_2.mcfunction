# @s at @s : commandes de l'image mg.lse du mouvement de l'emote Danse : bras en alternance, balancement gauche-droite du corps (48 ticks)
execute if score @s mg.lse matches 0 run swing @s mainhand
execute if score @s mg.lse matches 0 run rotate @s ~20 ~
execute if score @s mg.lse matches 4 run swing @s offhand
execute if score @s mg.lse matches 8 run swing @s mainhand
execute if score @s mg.lse matches 8 run rotate @s ~-40 ~
execute if score @s mg.lse matches 12 run swing @s offhand
execute if score @s mg.lse matches 16 run swing @s mainhand
execute if score @s mg.lse matches 16 run rotate @s ~40 ~
execute if score @s mg.lse matches 20 run swing @s offhand
execute if score @s mg.lse matches 24 run swing @s mainhand
execute if score @s mg.lse matches 24 run rotate @s ~-40 ~
execute if score @s mg.lse matches 28 run swing @s offhand
execute if score @s mg.lse matches 32 run swing @s mainhand
execute if score @s mg.lse matches 32 run rotate @s ~40 ~
execute if score @s mg.lse matches 36 run swing @s offhand
execute if score @s mg.lse matches 40 run swing @s mainhand
execute if score @s mg.lse matches 40 run rotate @s ~-20 ~
execute if score @s mg.lse matches 44 run swing @s offhand
execute if score @s mg.lse matches 48.. run function mg:lobby/sit/move_stop
