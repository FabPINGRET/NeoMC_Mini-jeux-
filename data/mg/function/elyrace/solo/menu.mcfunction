# @s = joueur : fenêtre du contre-la-montre solo (ouverte à tous), sinon menu texte
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_elyrace_solo
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n⏱ Contre-la-montre solo (ouvert à tous : /trigger mg.xs)","color":"aqua","bold":true}]
tellraw @s ["",{"text":" [⏱ Au hasard]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.xs set 10"},"hover_event":{"action":"show_text","value":"Contre-la-montre : seul en piste, ton meilleur temps est enregistré (30 s d'attente entre deux solos)."}}]
tellraw @s ["",{"text":" [⏱ Canyon du Couchant ","color":"gold","click_event":{"action":"run_command","command":"trigger mg.xs set 11"},"hover_event":{"action":"show_text","value":"Contre-la-montre : seul en piste, ton meilleur temps est enregistré (30 s d'attente entre deux solos)."}},{"text":"★★★","color":"gold"},{"text":"☆]","color":"dark_gray"}]
tellraw @s ["",{"text":" [⏱ Pic Blanc ","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.xs set 12"},"hover_event":{"action":"show_text","value":"Contre-la-montre : seul en piste, ton meilleur temps est enregistré (30 s d'attente entre deux solos)."}},{"text":"★★★★","color":"gold"},{"text":"]","color":"dark_gray"}]
tellraw @s ["",{"text":" [📊 Records]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.xs set 3"},"hover_event":{"action":"show_text","value":"Tes meilleurs temps et les records du serveur."}}]
tellraw @s ["",{"text":" [« Retour]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu set 1"}}]
