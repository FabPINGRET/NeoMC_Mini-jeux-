# Invité en attente (@s, appelé chaque tick par duel/tick) : devenu occupé, son invitation expire ;
# sa fenêtre a été remplacée par une autre : mg.dlui est retiré sans dialog clear
function mg:duel/busy
execute if score $dlb mg.st matches 1 run tag @s remove mg.dlui
execute if score $dlb mg.st matches 1 run function mg:duel/expire
