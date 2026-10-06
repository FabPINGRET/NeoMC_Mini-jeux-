# Roulette du mini-jeu : défile (4 s, de plus en plus lentement), puis le jeu tiré reste affiché 2 s avant le lancement
scoreboard players remove $mpw mg.st 1
scoreboard players operation $q mg.st = $mpw mg.st
scoreboard players operation $q mg.st %= #4 mg.st
scoreboard players operation $q8 mg.st = $mpw mg.st
scoreboard players operation $q8 mg.st %= #8 mg.st
execute if score $mpw mg.st matches 71.. if score $q mg.st matches 0 run function mg:party/pick
execute if score $mpw mg.st matches 41..70 if score $q8 mg.st matches 0 run function mg:party/pick
execute if score $mpw mg.st matches 40 run function mg:party/roulette_stop
execute if score $mpw mg.st matches ..0 run function mg:party/launch
