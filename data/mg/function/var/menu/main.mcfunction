# Menu des variantes (@s = admin) — fenêtre, sinon menu texte. Généré.
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:var_menu
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n★ VARIANTES ★ ","color":"gold","bold":true},{"text":"(choisis un mode)","color":"gray"}]
tellraw @s ["",{"text":" [⚔ Arène PvP ▸]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set 33"}}]
tellraw @s ["",{"text":" [➶ One in the Chamber ▸]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.opt set 34"}}]
tellraw @s ["",{"text":" [⚡ Quakecraft ▸]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.opt set 35"}}]
tellraw @s ["",{"text":" [✹ TNT Tag ▸]","color":"red","click_event":{"action":"run_command","command":"trigger mg.opt set 36"}}]
tellraw @s ["",{"text":" [❄ Spleef ▸]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.opt set 37"}}]
tellraw @s ["",{"text":" [✷ TNT Run ▸]","color":"red","click_event":{"action":"run_command","command":"trigger mg.opt set 38"}}]
tellraw @s ["",{"text":" [❍ Splegg ▸]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set 39"}}]
