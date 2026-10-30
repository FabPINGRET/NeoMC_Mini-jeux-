# @s retourne au lobby (contexte quelconque) : inventaire de la carte mis de côté, tout ce que la carte a modifié remis
execute unless entity @s[tag=mg.flw] run return 0
execute if score @s mg.svid matches 1.. store result storage mg:floaty v.x int 1 run scoreboard players get @s mg.svvx
execute if score @s mg.svid matches 1.. in minecraft:overworld run function mg:floaty/vault_make with storage mg:floaty v
execute if score @s mg.svid matches 1.. in minecraft:overworld run function mg:floaty/vault_save with storage mg:floaty v
tag @s remove mg.flw
tag @s remove mg.surv
function mg:floaty/bars
xp set @s 0 levels
xp set @s 0 points
function mg:floaty/attrs
function mg:floaty/reset_scores
execute in minecraft:overworld run function mg:core/reset_player
tellraw @s {"text":"⌂ Retour au lobby. Ton inventaire de la carte est mis de côté ; la partie continue pour les autres joueurs.","color":"gold"}
