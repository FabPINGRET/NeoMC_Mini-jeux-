# fin de cinématique : sur la place de la colonie
scoreboard players operation $own mg.st = @s mg.tvpid
spectate
execute as @e[type=minecraft:item_display,tag=mg.trcam] if score @s mg.tvo = $own mg.st run kill @s
tag @s remove mg.trcine
scoreboard players set @s mg.trcs 0
gamemode adventure @s
title @s clear
execute in mg:terranova run tp @s 0.5 65 4.5 180 0
