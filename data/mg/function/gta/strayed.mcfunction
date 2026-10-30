# @s a quitté Neo City autrement (téléportation…) : il n'est plus considéré comme joueur du GTA
tag @s remove mg.gtw
tag @s remove mg.surv
function mg:gta/untag
execute in minecraft:overworld run function mg:core/reset_player
attribute @s minecraft:fall_damage_multiplier base set 0
