# @s accepte « Chevaliers noirs »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p14 mg.st
scoreboard players set @s mg.olq15 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"Chevaliers noirs : Les chevaliers noirs patrouillent autour du camp. Abats-en 6.","color":"gray"}]
