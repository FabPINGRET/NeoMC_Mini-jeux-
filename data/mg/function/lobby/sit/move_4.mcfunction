# @s at @s : commandes de l'image mg.lse du mouvement de l'emote Étourdi : la tête décrit deux cercles (32 ticks)
execute if score @s mg.lse matches 0 run rotate @s ~12 ~-6
execute if score @s mg.lse matches 4 run rotate @s ~12 ~6
execute if score @s mg.lse matches 8 run rotate @s ~-12 ~6
execute if score @s mg.lse matches 12 run rotate @s ~-12 ~-6
execute if score @s mg.lse matches 16 run rotate @s ~12 ~-6
execute if score @s mg.lse matches 20 run rotate @s ~12 ~6
execute if score @s mg.lse matches 24 run rotate @s ~-12 ~6
execute if score @s mg.lse matches 28 run rotate @s ~-12 ~-6
execute if score @s mg.lse matches 32.. run function mg:lobby/sit/move_stop
