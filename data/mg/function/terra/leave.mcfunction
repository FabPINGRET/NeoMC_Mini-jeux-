# @s retourne au lobby (appelé dans le monde des mini-jeux : execute in minecraft:overworld)
execute unless entity @s[tag=mg.tvw] run return 0
tag @s remove mg.tvw
tag @s remove mg.surv
function mg:terra/mis_clear
function mg:terra/traps_clear
function mg:terra/untag
function mg:terra/rpg/leave
function mg:core/reset_player
attribute @s minecraft:fall_damage_multiplier base set 0
tellraw @s [{"text":"⌂ Retour au lobby. Tes crédits restent à Terra Nova : ","color":"gold"},{"score":{"name":"@s","objective":"mg.tvc"},"color":"green","bold":true},{"text":" ₵","color":"green"}]
