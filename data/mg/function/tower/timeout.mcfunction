# 10 min : le plus de points gagne
execute if score Rouge mg.tw > Bleu mg.tw run return run function mg:core/win_red
execute if score Bleu mg.tw > Rouge mg.tw run return run function mg:core/win_blue
function mg:core/draw
