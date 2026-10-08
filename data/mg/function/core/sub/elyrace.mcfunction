# Sous-menu 🪽 Course d'élytres (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_elyrace
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n🪽 Course d'élytres — choisis un parcours","color":"aqua","bold":true}]
tellraw @s ["",{"text":" [🎲 Au hasard]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.go set 66"},"hover_event":{"action":"show_text","value":"Un parcours tiré au hasard parmi ceux qui sont construits."}}]
tellraw @s ["",{"text":" [🏜 Canyon du Couchant ","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 81"},"hover_event":{"action":"show_text","value":"Parcours 1 (Far West, ~1000 blocs) : slalom entre cheminées de fée, arches, viaduc ferroviaire, gorge en S, crête, ville fantôme. 18 anneaux, 3 anneaux d'or, 4 points de reprise, 3 cœurs."}},{"text":"★★★","color":"gold"},{"text":"☆]","color":"dark_gray"}]
tellraw @s ["",{"text":" [🏔 Pic Blanc ","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 82"},"hover_event":{"action":"show_text","value":"Parcours 2 (haute montagne, ~1100 blocs) : pylônes de téléphérique, col, glacier, crevasse de glace, grotte éclairée, village d'arrivée. 20 anneaux, 3 anneaux d'or, 4 points de reprise, 3 cœurs."}},{"text":"★★★★","color":"gold"},{"text":"]","color":"dark_gray"}]
tellraw @s ["",{"text":" [« Retour]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set 42"}}]
