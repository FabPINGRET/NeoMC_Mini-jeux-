# Pause : on regarde qui est tombé, puis manche suivante
scoreboard players remove $bt mg.st 1
execute if score $bt mg.st matches ..0 run function mg:blockparty/new_round
