# @s accepte « Les gardiens de cendre »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.trsq
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trsa += #p3 mg.st
tellraw @s [{"text":"📜 Quête secondaire : ","color":"yellow","bold":true},{"text":"Les gardiens de cendre — Les carnotaures du Mont Cendre m'empêchent de prendre mes mesures.","color":"gray"}]
scoreboard players set @s mg.trq4 0
