# @s (dinosaure à modèle 3D) : état (0 repos, 1 marche, 2 attaque, 3 rugissement) et image suivante -> mg.tvak
scoreboard players set $tvas mg.st 0
execute if predicate mg:tv_moving run scoreboard players set $tvas mg.st 1
execute if score @s mg.tvat matches 1.. run scoreboard players set $tvas mg.st 2
execute if score @s mg.tvat matches 1.. if entity @s[tag=mg.tvroar] run scoreboard players set $tvas mg.st 3
scoreboard players remove @s[scores={mg.tvat=1..}] mg.tvat 2
execute if score @s mg.tvat matches ..0 run tag @s remove mg.tvroar
# au repos : une image sur deux (balancement lent)
# rythme indépendant de la fréquence des mises à jour : une image toutes les 2 ticks (4 au repos)
execute unless score $tvas mg.st matches 0 if score $tvq2b mg.st matches 0 run scoreboard players add @s mg.tvaf 1
execute if score $tvas mg.st matches 0 if score $tvq4b mg.st matches 0 run scoreboard players add @s mg.tvaf 1
execute if score @s mg.tvaf matches 8.. run scoreboard players set @s mg.tvaf 0
scoreboard players operation @s mg.tvak = $tvas mg.st
scoreboard players operation @s mg.tvak *= #8 mg.st
scoreboard players operation @s mg.tvak += @s mg.tvaf
