# Roulette 3 s : un nom toutes les 4 ticks, le dernier tirage est lancé
scoreboard players remove $mpw mg.st 1
scoreboard players operation $q mg.st = $mpw mg.st
scoreboard players operation $q mg.st %= #4 mg.st
execute if score $mpw mg.st matches 1.. if score $q mg.st matches 0 run function mg:party/pick
execute if score $mpw mg.st matches ..0 run function mg:party/launch
