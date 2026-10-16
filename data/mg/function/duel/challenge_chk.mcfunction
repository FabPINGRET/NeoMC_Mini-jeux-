# Contrôles puis invitation (@s = défieur ; l'adversaire porte mg.dltg)
execute if entity @s[tag=mg.dlrq] run function mg:duel/rq_check
execute if entity @s[tag=mg.dlrq] run return run tellraw @s [{"text":"Tu as déjà une invitation en cours : ","color":"gray"},{"text":"[Annuler]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 4"},"hover_event":{"action":"show_text","value":"Annuler l'invitation"}}]
execute if score @s mg.dlto matches 1.. run return run tellraw @s [{"text":"Tu as reçu une invitation de duel : ","color":"gray"},{"text":"[✔ Accepter]","color":"green","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 2"},"hover_event":{"action":"show_text","value":"Relever le défi"}},{"text":" ","color":"gray"},{"text":"[✘ Refuser]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 3"},"hover_event":{"action":"show_text","value":"Refuser le défi"}},{"text":" avant d'en lancer une.","color":"gray"}]
function mg:duel/busy
execute if score $dlb mg.st matches 1 run return run tellraw @s [{"text":"Tu ne peux pas défier maintenant (partie ou activité en cours).","color":"gray"}]
execute unless entity @a[tag=mg.dltg] run return run tellraw @s [{"text":"Ce joueur n'est plus là.","color":"gray"}]
execute if entity @s[tag=mg.dltg] run return run tellraw @s [{"text":"Tu ne peux pas te défier toi-même.","color":"gray"}]
execute as @a[tag=mg.dltg,limit=1] run function mg:duel/busy
execute if score $dlb mg.st matches 1 run return run tellraw @s [{"selector":"@a[tag=mg.dltg,limit=1]","color":"white"},{"text":" est occupé (partie ou activité en cours).","color":"gray"}]
execute if entity @a[tag=mg.dltg,tag=mg.dlrq] run return run tellraw @s [{"selector":"@a[tag=mg.dltg,limit=1]","color":"white"},{"text":" a déjà une invitation en cours.","color":"gray"}]
execute if entity @a[tag=mg.dltg,scores={mg.dlto=1..}] run return run tellraw @s [{"selector":"@a[tag=mg.dltg,limit=1]","color":"white"},{"text":" a déjà reçu une invitation.","color":"gray"}]
function mg:duel/pick
execute if score $dli mg.st matches 0 run return run tellraw @s [{"text":"Aucune arène n'est libre pour le moment (ou elles sont en construction).","color":"gray"}]
execute unless score @s mg.dlid matches 1.. run function mg:duel/new_id
scoreboard players operation @a[tag=mg.dltg,limit=1] mg.dlto = @s mg.dlid
scoreboard players set @a[tag=mg.dltg,limit=1] mg.dlx 600
tag @s add mg.dlrq
tellraw @a[tag=mg.dltg,limit=1] [{"selector":"@s","color":"yellow","bold":true},{"text":" te défie en duel sniper 1v1 (30 s) : ","color":"gray"},{"text":"[✔ Accepter]","color":"green","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 2"},"hover_event":{"action":"show_text","value":"Relever le défi"}},{"text":" ","color":"gray"},{"text":"[✘ Refuser]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 3"},"hover_event":{"action":"show_text","value":"Refuser le défi"}}]
tellraw @s [{"text":"⚔ Défi envoyé à ","color":"gray"},{"selector":"@a[tag=mg.dltg,limit=1]","color":"white"},{"text":" (30 s) ","color":"gray"},{"text":"[Annuler]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.duel set 4"},"hover_event":{"action":"show_text","value":"Annuler l'invitation"}}]
