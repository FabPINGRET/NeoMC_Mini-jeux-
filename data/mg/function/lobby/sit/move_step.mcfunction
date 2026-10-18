# @s at @s (move_tick) : une image de plus du mouvement de l'emote ; refus de sit/ok (spawn quitté, partie, admin) : arrêt
execute unless function mg:lobby/sit/ok run return run function mg:lobby/sit/move_stop
execute unless score @s mg.lsk matches 1..4 run return run function mg:lobby/sit/move_stop
scoreboard players add @s mg.lse 1
execute if score @s mg.lsk matches 1 run return run function mg:lobby/sit/move_1
execute if score @s mg.lsk matches 2 run return run function mg:lobby/sit/move_2
execute if score @s mg.lsk matches 3 run return run function mg:lobby/sit/move_3
execute if score @s mg.lsk matches 4 run return run function mg:lobby/sit/move_4
