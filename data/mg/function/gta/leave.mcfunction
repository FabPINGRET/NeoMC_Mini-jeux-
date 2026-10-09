# @s retourne au lobby (appelé dans le monde des mini-jeux : execute in minecraft:overworld)
execute unless entity @s[tag=mg.gtw] run return 0
tag @s remove mg.gtw
tag @s remove mg.surv
function mg:gta/untag
function mg:core/reset_player
attribute @s minecraft:fall_damage_multiplier base set 0
tellraw @s [{"text":"⌂ Retour au lobby. Tes dollars restent à Neo City : ","color":"gold"},{"score":{"name":"@s","objective":"mg.gta"},"color":"green","bold":true},{"text":" $","color":"green"}]
