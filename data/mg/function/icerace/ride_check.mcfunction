# @s = joueur : toujours dans son bateau
scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 0 run function mg:icerace/remount
