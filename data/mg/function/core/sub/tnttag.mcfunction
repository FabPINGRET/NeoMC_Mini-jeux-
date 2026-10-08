# Sous-menu ✹ TNT Tag (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_tnttag
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n✹ TNT Tag — La patate chaude : choisis la carte.","color":"red","bold":true}]
tellraw @s ["",{"text":" [🎲 Carte au hasard]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 27"},"hover_event":{"action":"show_text","value":"Une des 4 cartes, tirée au sort"}}]
tellraw @s ["",{"text":" [✹ Classique]","color":"red","click_event":{"action":"run_command","command":"trigger mg.go set 67"},"hover_event":{"action":"show_text","value":"Arène plate 31×31, piliers et murets"}}]
tellraw @s ["",{"text":" [⛰ Collines]","color":"green","click_event":{"action":"run_command","command":"trigger mg.go set 68"},"hover_event":{"action":"show_text","value":"Prairie vallonnée, rivière, moulin, kiosque"}}]
tellraw @s ["",{"text":" [🏜 Canyon]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 69"},"hover_event":{"action":"show_text","value":"Mesa à plateaux, arche, tunnel, pont suspendu"}}]
tellraw @s ["",{"text":" [🏘 Village perché]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 70"},"hover_event":{"action":"show_text","value":"Toits accessibles, passerelles, clocher"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
