# 🎯 TDM sniper — préparation : arène du duel libre au hasard, réservée par $tma
scoreboard players set $tma mg.st 0
execute unless data storage mg:duel {built:1b} run return run function mg:tdm/no_map
function mg:duel/pick
execute if score $dli mg.st matches 0 run return run function mg:tdm/no_map
scoreboard players operation $tma mg.st = $dli mg.st
# point de reconnexion (spectateur) : au-dessus du centre de l'arène
scoreboard players set $px mg.st 0
execute if score $tma mg.st matches 1 run scoreboard players set $py mg.st 109
execute if score $tma mg.st matches 2 run scoreboard players set $py mg.st 101
execute if score $tma mg.st matches 3 run scoreboard players set $py mg.st 101
execute if score $tma mg.st matches 1 run scoreboard players set $pz mg.st 40000
execute if score $tma mg.st matches 2 run scoreboard players set $pz mg.st 40400
execute if score $tma mg.st matches 3 run scoreboard players set $pz mg.st 40800
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
tag @a remove mg.tmp
scoreboard players set $nt mg.st 2
function mg:core/assign_teams
scoreboard players reset * mg.tmk
# premiers départs : un par rang dans l'équipe (pas de tirage : deux coéquipiers ne partagent pas un départ)
scoreboard players set $tmri mg.st 0
scoreboard players set $tmbi mg.st 0
scoreboard players set #tm12 mg.st 12
execute as @a[tag=mg.play] run function mg:tdm/spawn_first
execute if score $tma mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🎯 Carte : ","color":"gray"},{"text":"Canyon","color":"gold","bold":true}]
execute if score $tma mg.st matches 2 run tellraw @a[tag=mg.play] [{"text":"🎯 Carte : ","color":"gray"},{"text":"Ville","color":"gold","bold":true}]
execute if score $tma mg.st matches 3 run tellraw @a[tag=mg.play] [{"text":"🎯 Carte : ","color":"gray"},{"text":"Glacier","color":"gold","bold":true}]
