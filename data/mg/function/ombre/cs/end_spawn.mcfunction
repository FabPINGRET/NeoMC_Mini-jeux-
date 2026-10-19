# fin de cinématique : sur la place de Havreclair
scoreboard players operation $own mg.st = @s mg.olpid
spectate
execute as @e[tag=mg.olcam] if score @s mg.olo = $own mg.st run kill @s
tag @s remove mg.olcine
scoreboard players set @s mg.olcs 0
gamemode adventure @s
title @s clear
execute in mg:ombrelune run tp @s 0.5 65 9.5 180 0
function mg:ombre/q/say
