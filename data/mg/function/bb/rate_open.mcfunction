# @s = joueur : fenêtre de notation, sinon boutons dans le chat
scoreboard players set $bbdl mg.st 0
function mg:bb/rate_dialog
execute unless score $bbdl mg.st matches 1 run function mg:bb/rate_chat
