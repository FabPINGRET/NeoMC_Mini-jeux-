# Premier départ de @s (prepare) : rang d'arrivée dans son équipe (modulo le nombre de départs)
execute if entity @s[team=mg_red] run scoreboard players operation #tms mg.st = $tmri mg.st
execute if entity @s[team=mg_red] run scoreboard players add $tmri mg.st 1
execute if entity @s[team=mg_blue] run scoreboard players operation #tms mg.st = $tmbi mg.st
execute if entity @s[team=mg_blue] run scoreboard players add $tmbi mg.st 1
scoreboard players operation #tms mg.st %= #tm12 mg.st
function mg:tdm/spawn_do
