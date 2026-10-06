# Bedwars — placement APRÈS réapparition (@s = joueur revenu en vie, tag mg.rsp)
tag @s remove mg.rsp

# Éliminé (lit détruit) → perchoir central, spectateur
execute unless entity @s[tag=mg.play] run return run tp @s 0.5 85 1200.5

# Encore en jeu → île de son équipe
execute if entity @s[team=mg_red] run tp @s -31.5 64 1200.5 facing 0 64 1200
execute if entity @s[team=mg_blue] run tp @s 31.5 64 1200.5 facing 0 64 1200
execute if entity @s[team=mg_green] run tp @s 0.5 64 1168.5 facing 0 64 1200
execute if entity @s[team=mg_yellow] run tp @s 0.5 64 1232.5 facing 0 64 1200
