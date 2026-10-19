# @s (créature à modèle 3D) : état (0 repos, 1 marche, 2 attaque, 3 rugissement) et image suivante -> mg.olak
scoreboard players set $olas mg.st 0
execute if predicate mg:tv_moving run scoreboard players set $olas mg.st 1
execute if score @s mg.olat matches 1.. run scoreboard players set $olas mg.st 2
execute if score @s mg.olat matches 1.. if entity @s[tag=mg.olroar] run scoreboard players set $olas mg.st 3
scoreboard players remove @s[scores={mg.olat=1..}] mg.olat 2
execute if score @s mg.olat matches ..0 run tag @s remove mg.olroar
execute unless score $olas mg.st matches 0 if score $olq2 mg.st matches 0 run scoreboard players add @s mg.olaf 1
execute if score $olas mg.st matches 0 if score $olq4 mg.st matches 0 run scoreboard players add @s mg.olaf 1
execute if score @s mg.olaf matches 8.. run scoreboard players set @s mg.olaf 0
scoreboard players operation @s mg.olak = $olas mg.st
scoreboard players operation @s mg.olak *= #8 mg.st
scoreboard players operation @s mg.olak += @s mg.olaf
