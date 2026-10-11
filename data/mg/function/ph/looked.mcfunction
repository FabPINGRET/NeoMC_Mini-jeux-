# @s : objet d'un cacheur regardé par un chercheur
tag @s remove mg.phlk
scoreboard players operation $pid mg.st = @s mg.pid
execute as @a[tag=mg.phh] if score @s mg.pid = $pid mg.st run scoreboard players add @s mg.phpt 2
