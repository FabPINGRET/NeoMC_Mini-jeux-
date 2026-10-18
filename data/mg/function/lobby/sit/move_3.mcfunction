# @s at @s : commandes de l'image mg.lse du mouvement de l'emote Fête : un tour complet sur soi-même, puis bras en alternance (32 ticks)
execute if score @s mg.lse matches 0 run rotate @s ~45 ~
execute if score @s mg.lse matches 2 run rotate @s ~45 ~
execute if score @s mg.lse matches 4 run rotate @s ~45 ~
execute if score @s mg.lse matches 6 run rotate @s ~45 ~
execute if score @s mg.lse matches 8 run rotate @s ~45 ~
execute if score @s mg.lse matches 10 run rotate @s ~45 ~
execute if score @s mg.lse matches 12 run rotate @s ~45 ~
execute if score @s mg.lse matches 14 run rotate @s ~45 ~
execute if score @s mg.lse matches 16 run swing @s mainhand
execute if score @s mg.lse matches 20 run swing @s offhand
execute if score @s mg.lse matches 24 run swing @s mainhand
execute if score @s mg.lse matches 28 run swing @s offhand
execute if score @s mg.lse matches 32.. run function mg:lobby/sit/move_stop
