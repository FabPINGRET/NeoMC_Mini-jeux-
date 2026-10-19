# @s accepte « Cordes d'arc »
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}
scoreboard players operation @s mg.olsa += #p2 mg.st
scoreboard players set @s mg.olq3 0
tellraw @s [{"text":"❗ Quête secondaire : ","color":"yellow","bold":true},{"text":"Cordes d'arc : Nos arcs manquent de cordes. Rapporte-moi 8 soies d'araignée.","color":"gray"}]
