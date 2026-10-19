# @s accepte « Le puits des âmes »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p15 mg.st
scoreboard players set @s mg.olq16 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"Le puits des âmes : Le puits des âmes, à l'ouest, nourrit l'armée de Malveth. Tue son gardien.","color":"gray"}]
