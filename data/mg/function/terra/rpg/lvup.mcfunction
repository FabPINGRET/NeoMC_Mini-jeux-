# @s monte de niveau : annonce, effets, statistiques, soin
title @s times 5 50 15
title @s title [{"text":"⭐ NIVEAU ","color":"gold","bold":true},{"score":{"name":"@s","objective":"mg.trlv"},"color":"yellow","bold":true}]
title @s subtitle {"text":"Plus robuste : +1 cœur tous les 2 niveaux","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.8 0.4 0.4 40
tellraw @a[tag=mg.tvw] [{"text":"⭐ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" atteint le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.trlv"},"color":"gold","bold":true}]
function mg:terra/rpg/stats
function mg:core/heal
scoreboard players add @s mg.trsp 1
