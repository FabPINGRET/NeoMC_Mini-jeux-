# Sous-menu ❍ Splegg (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_splegg
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n❍ Splegg — choisis une version","color":"yellow","bold":true}]
tellraw @s ["",{"text":" [❍ Splegg]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.go set 20"},"hover_event":{"action":"show_text","value":"Spleef aux œufs : tire pour détruire la neige"}}]
tellraw @s ["",{"text":" [❍ Splegg XXL]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 21"},"hover_event":{"action":"show_text","value":"3 étages géants, œufs qui cassent 3x3"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
