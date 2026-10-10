# @s quitte l'arène (appelé aussi par mg:core/reset_player et au départ d'une partie) : tag, retour, chiens
execute unless entity @s[tag=mg.pvpc] run return 0
tag @s remove mg.pvpc
scoreboard players set @s mg.phc 0
scoreboard players operation $p mg.st = @s mg.pvid
execute as @e[type=minecraft:wolf,tag=mg.pdog] if score @s mg.pvid = $p mg.st run tp @s ~ -300 ~
spawnpoint @s 0 64 0
