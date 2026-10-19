# @s : $(n) matériau(x) de la région où il se trouve
$execute if score @s mg.olrg matches 1 run scoreboard players add @s mg.olm1 $(n)
$execute if score @s mg.olrg matches 1 run tellraw @s {"text":"  +$(n) peau de bête","color":"gold"}
$execute if score @s mg.olrg matches 2 run scoreboard players add @s mg.olm2 $(n)
$execute if score @s mg.olrg matches 2 run tellraw @s {"text":"  +$(n) soie d'araignée","color":"white"}
$execute if score @s mg.olrg matches 3 run scoreboard players add @s mg.olm3 $(n)
$execute if score @s mg.olrg matches 3 run tellraw @s {"text":"  +$(n) éclat de givre","color":"aqua"}
$execute if score @s mg.olrg matches 4 run scoreboard players add @s mg.olm4 $(n)
$execute if score @s mg.olrg matches 4 run tellraw @s {"text":"  +$(n) fiole de venin","color":"dark_green"}
$execute if score @s mg.olrg matches 5 run scoreboard players add @s mg.olm5 $(n)
$execute if score @s mg.olrg matches 5 run tellraw @s {"text":"  +$(n) ambre solaire","color":"yellow"}
$execute if score @s mg.olrg matches 6 run scoreboard players add @s mg.olm6 $(n)
$execute if score @s mg.olrg matches 6 run tellraw @s {"text":"  +$(n) écaille de drake","color":"red"}
$execute if score @s mg.olrg matches 7 run scoreboard players add @s mg.olm7 $(n)
$execute if score @s mg.olrg matches 7 run tellraw @s {"text":"  +$(n) minerai de runite","color":"blue"}
$execute if score @s mg.olrg matches 8 run scoreboard players add @s mg.olm8 $(n)
$execute if score @s mg.olrg matches 8 run tellraw @s {"text":"  +$(n) essence d'ombre","color":"dark_purple"}
$execute if score @s mg.olrg matches 0 run scoreboard players add @s mg.olm1 $(n)
