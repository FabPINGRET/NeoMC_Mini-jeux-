# @s monte de niveau
title @s times 5 50 15
title @s title [{"text":"⭐ NIVEAU ","color":"gold","bold":true},{"score":{"name":"@s","objective":"mg.ollv"},"color":"yellow","bold":true}]
title @s subtitle {"text":"+1 point de caractéristique (journal, case 8)","color":"gray"}
scoreboard players add @s mg.olsp 1
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.8 0.4 0.4 40
tellraw @a[tag=mg.olw] [{"text":"⭐ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" atteint le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.ollv"},"color":"gold","bold":true}]
function mg:ombre/stats
function mg:core/heal
function mg:ombre/kit_ab
execute if score @s mg.ollv matches 5 run tellraw @s {"text":"✨ Nouvelle compétence débloquée (case 4) !","color":"light_purple"}
execute if score @s mg.ollv matches 10 run tellraw @s {"text":"✨ Nouvelle compétence débloquée (case 5) !","color":"light_purple"}
execute if score @s mg.ollv matches 18 run tellraw @s {"text":"✨ Compétence ultime débloquée (case 6) !","color":"gold"}
