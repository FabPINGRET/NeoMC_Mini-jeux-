# Retire le décor saisonnier en place ($theme) et rétablit le spawn d'origine
function mg:lobby/theme/sync
execute unless score $theme mg.st matches 1.. run return run tellraw @s {"text":"Aucun décor saisonnier en place.","color":"gray"}
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/off
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/off
scoreboard players set $theme mg.st 0
data remove storage mg:lobby theme
scoreboard players reset $thw mg.st
scoreboard players reset $thd mg.st
scoreboard players reset $thi mg.st
function mg:lobby/theme/clear
# $thsw (bascule d'un thème à l'autre) : le place du nouveau thème remet l'eau d'aplomb, une seule fois pour les deux
execute unless score $thsw mg.st matches 1 run function mg:lobby/theme/water_fix
function mg:lobby/deco
function mg:lobby/food_skin
execute unless score $thsw mg.st matches 1 run tellraw @a[tag=mg.admin] {"text":"Décor saisonnier retiré, spawn d'origine rétabli.","color":"gray"}
