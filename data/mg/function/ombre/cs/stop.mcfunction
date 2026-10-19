# @s quitte Ombrelune pendant une cinématique
execute unless entity @s[tag=mg.olcine] run return 0
scoreboard players operation $own mg.st = @s mg.olpid
spectate
execute as @e[tag=mg.olcam] if score @s mg.olo = $own mg.st run kill @s
tag @s remove mg.olcine
scoreboard players set @s mg.olcs 0
gamemode adventure @s
title @s clear
