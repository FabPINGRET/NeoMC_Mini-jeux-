# @s accepte « Remèdes du marais »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.trsa += #p0 mg.st
tellraw @s [{"text":"📜 Quête secondaire : ","color":"yellow","bold":true},{"text":"Remèdes du marais — Le venin des dilophosaures, bien dosé, soigne les fièvres de la colonie.","color":"gray"}]
