# @s : balle sortie de la zone sans être reprise (rebond valable avant : point au frappeur, sinon faute)
execute if score @s mg.tnb matches 1.. run scoreboard players set $tnwhy mg.st 5
execute if score @s mg.tnb matches 1.. run return run function mg:tennis/pt_hitter
scoreboard players set $tnwhy mg.st 2
function mg:tennis/pt_recv
