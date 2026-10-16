# Liste cliquable des adversaires libres (@s = joueur) : lien = trigger mg.duel 1000 + id
function mg:duel/busy
execute if score $dlb mg.st matches 1 run return run tellraw @s [{"text":"Tu ne peux pas défier maintenant (partie ou activité en cours).","color":"gray"}]
execute if entity @s[tag=mg.dlrq] run return run tellraw @s [{"text":"Tu as déjà une invitation en cours : ","color":"gray"},{"text":"[Annuler]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 4"},"hover_event":{"action":"show_text","value":"Annuler l'invitation"}}]
execute if score @s mg.dlto matches 1.. run return run tellraw @s [{"text":"Tu as reçu une invitation de duel : ","color":"gray"},{"text":"[✔ Accepter]","color":"green","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 2"},"hover_event":{"action":"show_text","value":"Relever le défi"}},{"text":" ","color":"gray"},{"text":"[✘ Refuser]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 3"},"hover_event":{"action":"show_text","value":"Refuser le défi"}},{"text":" avant d'en lancer une.","color":"gray"}]
execute unless data storage mg:duel {built:1b} run return run tellraw @s [{"text":"Les arènes sont en construction, réessaie dans quelques minutes.","color":"gray"}]
tellraw @s [{"text":"— Duel sniper 1v1 : clique sur un adversaire —","color":"gold"}]
scoreboard players set $dlc mg.st 0
tag @s add mg.dlq
execute as @a[tag=!mg.dlq,tag=mg.init] run function mg:duel/list_one
tag @s remove mg.dlq
execute if score $dlc mg.st matches 0 run tellraw @s [{"text":"Personne n'est disponible pour un duel pour le moment.","color":"gray"}]
