# Élytra — tick de partie (état 2)
scoreboard players add $skt mg.st 1
scoreboard players operation $skp mg.st = $skt mg.st
scoreboard players operation $skp mg.st %= #2 mg.st
execute if score $elm mg.st matches 1..2 run function mg:sky/t_race
execute if score $elm mg.st matches 3 run function mg:sky/t_surv
