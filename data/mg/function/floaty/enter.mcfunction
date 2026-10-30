# @s entre dans Scourge of the Floaty Isles (contexte : monde des mini-jeux)
execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d'abord lancer /function mg:setup","color":"red"}
execute if entity @s[tag=mg.flw] run return 0
execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : la carte sera accessible après.","color":"red"}
# emplacement du coffre Floaty : celui de la survie (numéro mg.svid / colonne mg.svvx)
execute unless score @s mg.svid matches 1.. in minecraft:overworld run function mg:survie/assign
execute unless score @s mg.svid matches 1.. run return run tellraw @s {"text":"⚠ Aucun emplacement de coffre libre : Floaty indisponible.","color":"red"}
function mg:lobkart/leave
function mg:parkour/quit
tag @s remove mg.inplot
tag @s remove mg.plabel
tag @s remove mg.visit
# état de la carte (objectifs, équipes, barres, scores) : créé une seule fois (garde dans floaty:install)
function floaty:install
tag @s add mg.surv
tag @s add mg.flw
execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
team leave @s
effect clear @s
clear @s
xp set @s 0 levels
xp set @s 0 points
gamemode adventure @s
function mg:core/attr_reset
function mg:floaty/attrs
attribute @s minecraft:fall_damage_multiplier base set 1
function mg:floaty/reset_scores
execute store result storage mg:floaty v.x int 1 run scoreboard players get @s mg.svvx
execute in minecraft:overworld run function mg:floaty/vault_make with storage mg:floaty v
execute in minecraft:overworld run function mg:floaty/vault_load with storage mg:floaty v
function mg:floaty/cu/run
function mg:floaty/cu/tp
function mg:core/heal
title @s times 10 60 20
title @s title {"text":"SCOURGE OF THE FLOATY ISLES","color":"aqua","bold":true}
title @s subtitle {"text":"Une seule partie pour tout le serveur","color":"gray"}
tellraw @s [{"text":"🏝 FLOATY ISLES","color":"aqua","bold":true},{"text":" : la partie est commune à tous les joueurs de la carte. Ton inventaire de la carte est gardé d'une visite à l'autre.","color":"yellow"}]
tellraw @s [{"text":" ⌂ Sortir : menu Échap → ≡ Menu → Retour au lobby (ou /trigger mg.sv set 2).","color":"gray"}]
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6
