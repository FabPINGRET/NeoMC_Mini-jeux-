# Retire le décor saisonnier en place ($theme) et rétablit le spawn d'origine
execute unless score $theme mg.st matches 1.. run return run tellraw @s {"text":"Aucun décor saisonnier en place.","color":"gray"}
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/off
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/off
scoreboard players set $theme mg.st 0
function mg:lobby/theme/clear
function mg:lobby/theme/water_fix
function mg:lobby/deco
tellraw @a[tag=mg.admin] {"text":"Décor saisonnier retiré, spawn d'origine rétabli.","color":"gray"}
