# @s entre au Filon (contexte : monde des mini-jeux)
execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : le Filon sera accessible après.","color":"red"}
function mg:lobkart/leave
function mg:parkour/quit
tag @s remove mg.inplot
tag @s remove mg.plabel
tag @s remove mg.visit
tag @s add mg.surv
tag @s add mg.fnw
execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
team leave @s
effect clear @s
clear @s
gamemode adventure @s
function mg:core/attr_reset
attribute @s minecraft:fall_damage_multiplier base set 0
function mg:filon/join
function mg:core/heal
team join mg_fn @s
spawnpoint @s 8 100 45991
tp @s 8.5 100 45991.5 0 0
function mg:filon/kit
function mg:filon/bag_load
execute if entity @s[tag=mg.fnnew] run give @s minecraft:bread 16
tag @s remove mg.fnnew
function mg:filon/effects
title @s times 10 60 20
title @s title {"text":"⛏ FILON","color":"gold","bold":true}
title @s subtitle {"text":"Un chunk, de la chance, et des pioches","color":"gray"}
tellraw @s [{"text":"⛏ FILON","color":"gold","bold":true},{"text":" : saute dans le chunk au centre de l'île et mine. Vends au ","color":"yellow"},{"text":"💰 Comptoir","color":"gold"},{"text":" (le cours change toutes les 15 min), améliore-toi au ","color":"yellow"},{"text":"🛒 Magasin","color":"aqua"},{"text":".","color":"yellow"}]
tellraw @s [{"text":" ⏳ Régénération du chunk toutes les 45 min — ","color":"gray"},{"text":"⚔ PvP seulement dans la mine, pendant les phases annoncées","color":"red"},{"text":" (tué : la moitié de ton sac part au tueur).","color":"gray"}]
tellraw @s [{"text":" 🪢 Corde (case 9) : remonter (recharge 120 s). Ta progression est gardée jusqu'à la fin de la saison.","color":"gray"}]
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6
