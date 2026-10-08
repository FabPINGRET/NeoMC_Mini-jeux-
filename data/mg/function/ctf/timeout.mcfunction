# 10 min : le plus de captures gagne
execute if score Rouge mg.cf > Bleu mg.cf run return run function mg:core/win_red
execute if score Bleu mg.cf > Rouge mg.cf run return run function mg:core/win_blue
function mg:core/draw
