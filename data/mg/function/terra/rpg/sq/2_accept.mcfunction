# @s accepte « Le ciel des Aiguilles »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.trsa += #p1 mg.st
tellraw @s [{"text":"📜 Quête secondaire : ","color":"yellow","bold":true},{"text":"Le ciel des Aiguilles — Les ptéranodons attaquent nos patrouilles.","color":"gray"}]
