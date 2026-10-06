# Choix de classe (@s = joueur) : fenêtre, sinon liste cliquable dans le chat
scoreboard players set $dlg mg.st 0
function mg:pvp2/dialog
execute unless score $dlg mg.st matches 1 run function mg:pvp2/chat
