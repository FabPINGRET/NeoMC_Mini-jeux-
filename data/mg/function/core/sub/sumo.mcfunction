# Sous-menu ✊ Sumo (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_sumo
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n✊ Sumo — choisis une version","color":"gold","bold":true}]
tellraw @s ["",{"text":" [✊ Sumo]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 22"},"hover_event":{"action":"show_text","value":"Éjecte les autres de la plateforme avec un bâton Knockback"}}]
tellraw @s ["",{"text":" [✊ Sumo : arène complexe]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 24"},"hover_event":{"action":"show_text","value":"Grande arène avec douve, ponts, piliers et bumpers : pour beaucoup de joueurs"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
