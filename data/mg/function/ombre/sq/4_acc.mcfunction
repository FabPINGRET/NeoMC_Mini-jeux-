# @s accepte « Le nid des tisseuses »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p3 mg.st
scoreboard players set @s mg.olq4 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"Le nid des tisseuses : Un nid de tisseuses grouille dans une caverne à l'ouest. Purge-le jusqu'à son alpha.","color":"gray"}]
