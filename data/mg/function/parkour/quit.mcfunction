# Abandon du parkour (@s = joueur)
execute unless entity @s[tag=mg.pkr] run return 0
tag @s remove mg.pkr
tp @s 0.5 64 0.5 facing 0.5 64 8.5
function mg:core/heal
tellraw @s [{"text":"Parkour abandonné.","color":"gray"}]
