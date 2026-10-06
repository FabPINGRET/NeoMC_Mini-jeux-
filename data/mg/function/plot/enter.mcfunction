# Aller sur son plot (@s = joueur) : attribué au premier passage, créatif uniquement à l'intérieur
execute unless score $setup mg.st matches 1 run return run tellraw @s [{"text":"⚠ Installation manquante : un OP doit d'abord lancer ","color":"red"},{"text":"/function mg:setup","color":"yellow"}]
execute if entity @s[tag=mg.play] run return run tellraw @s [{"text":"⚠ Tu participes à la partie en cours : plot accessible après.","color":"red"}]
execute if entity @s[tag=mg.out] run return run tellraw @s [{"text":"⚠ Partie en cours : plot accessible après.","color":"red"}]
execute if entity @s[tag=mg.inplot] run return run function mg:plot/tp_home
tag @s remove mg.visit
execute unless score @s mg.plot matches 1.. run function mg:plot/claim
execute unless score @s mg.plot matches 1.. run return 0

function mg:parkour/quit
function mg:plot/coords
clear @s
effect clear @s
gamemode creative @s
tag @s add mg.inplot
tag @s add mg.plabel
function mg:plot/tp_home
tellraw @s [{"text":"Bienvenue sur ton plot n°","color":"green"},{"score":{"name":"@s","objective":"mg.plot"},"color":"gold"},{"text":" : construis librement ici. ","color":"green"},{"text":"[retour au spawn]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.pl set 2"},"hover_event":{"action":"show_text","value":"/trigger mg.pl set 2"}}]
