# @s accepte « Runite pour la forge »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p12 mg.st
scoreboard players set @s mg.olq13 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"Runite pour la forge : Il nous faut de la runite pour reforger nos armes. Rapporte-m'en 8.","color":"gray"}]
