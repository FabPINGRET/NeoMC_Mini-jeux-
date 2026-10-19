# @s accepte « Le cidre des cryptes »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p1 mg.st
scoreboard players set @s mg.olq2 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"Le cidre des cryptes : Des goules ont emporté mon meilleur tonneau dans les cryptes sous la chapelle de Valdor. Vide les cryptes !","color":"gray"}]
