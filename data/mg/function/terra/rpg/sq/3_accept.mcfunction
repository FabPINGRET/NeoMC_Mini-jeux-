# @s accepte « La mine maudite »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.trsq
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trsa += #p2 mg.st
tellraw @s [{"text":"📜 Quête secondaire : ","color":"yellow","bold":true},{"text":"La mine maudite — Ma mine, à l'ouest de l'arche, grouille de slashers et d'un alpha énorme.","color":"gray"}]
