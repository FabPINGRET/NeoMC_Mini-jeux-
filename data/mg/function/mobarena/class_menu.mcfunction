# Mob Arena — choix de classe (@s = joueur) : fenêtre, sinon liste cliquable dans le chat
scoreboard players set $dlg mg.st 0
function mg:mobarena/class_dialog
execute unless score $dlg mg.st matches 1 run function mg:mobarena/class_chat
