# @s at @s : commandes de l'image mg.lse du mouvement de l'emote Salut : bras qui s'agite quatre fois, petit hochement de tête (24 ticks)
execute if score @s mg.lse matches 0 run swing @s mainhand
execute if score @s mg.lse matches 0 run rotate @s ~ ~-10
execute if score @s mg.lse matches 5 run swing @s mainhand
execute if score @s mg.lse matches 10 run swing @s mainhand
execute if score @s mg.lse matches 12 run rotate @s ~ ~10
execute if score @s mg.lse matches 15 run swing @s mainhand
execute if score @s mg.lse matches 24.. run function mg:lobby/sit/move_stop
