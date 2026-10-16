# L'adversaire est parti (@s = le joueur resté) : victoire par forfait
scoreboard players operation $dli mg.st = @s mg.dli
tellraw @s [{"text":"⚔ Ton adversaire a quitté le duel : victoire par forfait.","color":"green"}]
tag @s add mg.dlwn
function mg:duel/end
