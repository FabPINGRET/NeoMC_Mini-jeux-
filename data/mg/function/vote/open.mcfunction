# Menu de vote (@s = joueur) : fenêtre, sinon chat cliquable
scoreboard players set $dlg mg.st 0
function mg:vote/dialog
execute unless score $dlg mg.st matches 1 run function mg:vote/chat
