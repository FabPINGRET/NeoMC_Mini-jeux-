# Temps écoulé
execute unless score $ym mg.st matches 1 run return run function mg:core/draw
execute if score $yar mg.st > $yab mg.st run return run function mg:core/win_red
execute if score $yab mg.st > $yar mg.st run return run function mg:core/win_blue
function mg:core/draw
