# L'invité apprend l'annulation (@s = invité ; le défieur porte mg.dlca)
tellraw @s [{"selector":"@a[tag=mg.dlca,limit=1]","color":"white"},{"text":" a annulé son invitation au duel.","color":"gray"}]
execute if entity @s[tag=mg.dlui] run dialog clear @s
tag @s remove mg.dlui
scoreboard players reset @s mg.dlto
scoreboard players reset @s mg.dlx
