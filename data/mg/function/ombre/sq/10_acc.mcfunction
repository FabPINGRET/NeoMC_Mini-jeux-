# @s accepte « Les tombeaux d'Azhar »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p9 mg.st
scoreboard players set @s mg.olq10 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"Les tombeaux d'Azhar : Des pillards ont réveillé une momie royale dans les tombeaux au sud-est. Arrête-la.","color":"gray"}]
