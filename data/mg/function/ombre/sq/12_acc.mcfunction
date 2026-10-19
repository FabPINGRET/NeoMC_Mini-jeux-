# @s accepte « La forge écarlate »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p11 mg.st
scoreboard players set @s mg.olq12 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"La forge écarlate : Mon ancien maître, devenu un forgeron calciné, hante la forge écarlate à l'est. Libère son âme.","color":"gray"}]
