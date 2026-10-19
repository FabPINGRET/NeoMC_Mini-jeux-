# fin de cinématique : retour à l'endroit de départ
scoreboard players operation $own mg.st = @s mg.olpid
spectate
execute as @e[tag=mg.olcam] if score @s mg.olo = $own mg.st run kill @s
tag @s remove mg.olcine
scoreboard players set @s mg.olcs 0
gamemode adventure @s
title @s clear
execute store result storage mg:ombre d.x int 1 run scoreboard players get @s mg.olsx
execute store result storage mg:ombre d.y int 1 run scoreboard players get @s mg.olsy
execute store result storage mg:ombre d.z int 1 run scoreboard players get @s mg.olsz
function mg:ombre/back with storage mg:ombre d
