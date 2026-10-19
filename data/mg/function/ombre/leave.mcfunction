# @s retourne au lobby (contexte : monde des mini-jeux)
execute unless entity @s[tag=mg.olw] run return 0
tag @s remove mg.olw
tag @s remove mg.surv
function mg:ombre/untag
function mg:core/reset_player
attribute @s minecraft:fall_damage_multiplier base set 0
tellraw @s [{"text":"⌂ Retour au lobby. Ta progression reste à Ombrelune (niveau ","color":"gold"},{"score":{"name":"@s","objective":"mg.ollv"},"color":"yellow"},{"text":", ","color":"gold"},{"score":{"name":"@s","objective":"mg.olg"},"color":"yellow"},{"text":" 💰).","color":"gold"}]
