# @s a quitté Terra Nova autrement (téléportation…) : retour au lobby complet, sauf s'il est déjà dans une partie
tag @s remove mg.tvw
tag @s remove mg.surv
function mg:terra/mis_clear
function mg:terra/traps_clear
function mg:terra/untag
function mg:terra/rpg/leave
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] in minecraft:overworld run function mg:core/reset_player
attribute @s minecraft:fall_damage_multiplier base set 0
