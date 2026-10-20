# @s a quitté Ombrelune autrement (mort hors dimension, /tp…) : retour au lobby complet, sauf s'il est déjà dans une partie
tag @s remove mg.olw
tag @s remove mg.surv
function mg:ombre/untag
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] in minecraft:overworld run function mg:core/reset_player
attribute @s minecraft:fall_damage_multiplier base set 0
