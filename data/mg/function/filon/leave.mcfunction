# @s retourne au lobby (contexte : monde des mini-jeux) : sac mis de côté
execute unless entity @s[tag=mg.fnw] run return 0
function mg:filon/bag_save
tag @s remove mg.fnw
tag @s remove mg.surv
tag @s remove mg.fnin
team leave @s
bossbar set mg:filon players @a[tag=mg.fnw]
effect clear @s
function mg:core/reset_player
attribute @s minecraft:fall_damage_multiplier base set 0
tellraw @s [{"text":"⌂ Retour au lobby. Ta progression reste au Filon (solde ","color":"gold"},{"score":{"name":"@s","objective":"mg.fnp"},"color":"yellow"},{"text":" pts, saison ","color":"gold"},{"score":{"name":"@s","objective":"mg.fns"},"color":"yellow"},{"text":" pts).","color":"gold"}]
