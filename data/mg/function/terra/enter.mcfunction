# @s entre dans le portail de Terra Nova (contexte : monde des mini-jeux)
execute unless data storage mg:terra built run return run function mg:terra/not_ready
execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Terra Nova sera accessible après.","color":"red"}
function mg:lobkart/leave
function mg:parkour/quit
tag @s remove mg.inplot
tag @s remove mg.plabel
tag @s remove mg.visit
tag @s add mg.surv
tag @s add mg.tvw
execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
team leave @s
effect clear @s
clear @s
gamemode adventure @s
function mg:core/attr_reset
attribute @s minecraft:fall_damage_multiplier base set 1
function mg:terra/join
function mg:core/heal
execute in mg:terranova run spawnpoint @s 16 65 17
execute in mg:terranova run tp @s 0.5 65 4.5 180 0
function mg:terra/kit
title @s times 10 60 20
title @s title {"text":"TERRA NOVA","color":"green","bold":true}
function mg:terra/rpg/enter
title @s subtitle {"text":"Il y a 85 millions d'années…","color":"gray"}
tellraw @s [{"text":"🦖 TERRA NOVA","color":"green","bold":true},{"text":" : bienvenue dans la colonie, colon !","color":"yellow"}]
tellraw @s [{"text":" 📋 Missions : ","color":"gold"},{"text":"tableau sur le mur du QG (nord-est de la place), récompenses en crédits ₵","color":"gray"}]
tellraw @s [{"text":" 🛒 Équipement : ","color":"aqua"},{"text":"dépôt au nord-ouest (canon sonique, filets, pièges, armure…)","color":"gray"}]
tellraw @s [{"text":" 🔫 Armes : ","color":"yellow"},{"text":"bâton électrique (étourdit), fusil à impulsions (clic droit, gare à la surchauffe)","color":"gray"}]
tellraw @s [{"text":" ✚ Infirmerie : ","color":"red"},{"text":"au sud-est, soigne. Mort = -10 % de tes crédits","color":"gray"}]
tellraw @s [{"text":" 🚪 Sortir : ","color":"light_purple"},{"text":"portail du temps (sud-ouest) ou Échap → ≡ Menu","color":"gray"}]
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.8
