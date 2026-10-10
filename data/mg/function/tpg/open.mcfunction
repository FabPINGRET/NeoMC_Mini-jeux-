# Fenêtre du TP général (@s = admin), sinon liens dans le chat
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:tp_general
execute unless score $dlg mg.st matches 1 run tellraw @s [{"text": "🌍 TP général : ", "color": "gold", "bold": true}, {"text": "[🌲 Tout le monde → Survie] ", "color": "green", "bold": false, "click_event": {"action": "run_command", "command": "trigger mg.opt set 63"}}, {"text": "[🚓 Tout le monde → Neo GTA] ", "color": "gold", "bold": false, "click_event": {"action": "run_command", "command": "trigger mg.opt set 64"}}, {"text": "[🏠 Tout le monde → Lobby] ", "color": "yellow", "bold": false, "click_event": {"action": "run_command", "command": "trigger mg.opt set 65"}}]
