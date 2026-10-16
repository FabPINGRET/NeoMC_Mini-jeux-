# @s quitte Terra Nova pendant une cinématique
execute unless entity @s[tag=mg.trcine] run return 0
scoreboard players operation $own mg.st = @s mg.tvpid
spectate
execute as @e[tag=mg.trcam] if score @s mg.tvo = $own mg.st run kill @s
tag @s remove mg.trcine
scoreboard players set @s mg.trcs 0
gamemode adventure @s
title @s clear
