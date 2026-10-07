# Sous-menu ⬇ The Dropper (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_dropper
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n⬇ The Dropper — choisis une version","color":"aqua","bold":true}]
tellraw @s ["",{"text":" [⬇ The Dropper]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 23"},"hover_event":{"action":"show_text","value":"Chute libre dans un puits d'obstacles : atterris dans l'unique bloc d'eau"}}]
tellraw @s ["",{"text":" [⬇ Dropper : tube commun]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 25"},"hover_event":{"action":"show_text","value":"Tous dans le même puits : le premier dans l'eau gagne la manche"}}]
tellraw @s ["",{"text":" [⬇ Dropper : Aventure (10 niveaux)]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 64"},"hover_event":{"action":"show_text","value":"10 grands niveaux à thème enchaînés : le premier qui les finit gagne"}}]
tellraw @s ["",{"text":" [⬇ Dropper : Défi]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 65"},"hover_event":{"action":"show_text","value":"Compétitif : tout le monde dans le même niveau de l'Aventure tiré au hasard, le premier dans l'eau gagne la manche"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
