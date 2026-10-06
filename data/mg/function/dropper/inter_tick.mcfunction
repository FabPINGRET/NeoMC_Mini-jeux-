# Pause entre deux manches
scoreboard players remove $dtm mg.st 1
execute if score $dtm mg.st matches ..0 run function mg:dropper/new_round
