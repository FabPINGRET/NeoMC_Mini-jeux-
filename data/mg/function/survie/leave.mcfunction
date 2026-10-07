# Retour au lobby des mini-jeux (@s) : tout est sauvegardé, puis remise à zéro façon lobby
execute unless entity @s[tag=mg.surv] run return run tellraw @s [{"text":"Tu n'es pas en survie.","color":"gray"}]
execute store result storage mg:survie id.id int 1 run scoreboard players get @s mg.svid
execute store result storage mg:survie id.x int 1 run scoreboard players get @s mg.svvx
function mg:survie/save with storage mg:survie id
function mg:survie/vault_save with storage mg:survie id
xp set @s 0 levels
xp set @s 0 points
tag @s remove mg.surv
tag @s add mg.init
function mg:core/reset_player
tellraw @s [{"text":"⌂ Retour au lobby. Ton inventaire de survie est mis de côté.","color":"gold"}]
