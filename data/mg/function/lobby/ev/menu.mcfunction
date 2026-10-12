# Admin : fenêtre des événements du lobby, sinon menu texte
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run function mg:rate/d/lobby_events
execute unless score $dlg mg.st matches 1 run function mg:lobby/ev/menu_chat
