# Construction / effacement : une étape par tick (attente du chargement des tronçons)
scoreboard players set $skok mg.st 0
execute if score $skbm mg.st matches 1 store result score $skok mg.st run function mg:sky/b_step
execute if score $skbm mg.st matches 2 store result score $skok mg.st run function mg:sky/w_step
execute if score $skok mg.st matches 1 run scoreboard players set $skw mg.st 0
execute if score $skok mg.st matches 1 run scoreboard players add $skbs mg.st 1
execute if score $skok mg.st matches 0 run scoreboard players add $skw mg.st 1
execute if score $skw mg.st matches 400.. run return run function mg:sky/b_fail
execute if score $skbs mg.st >= $skbn mg.st run return run function mg:sky/b_done
schedule function mg:sky/b_next 1t
