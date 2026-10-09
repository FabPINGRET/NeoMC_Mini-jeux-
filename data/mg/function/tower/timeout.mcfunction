# 10 min : le plus de points gagne
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🏰 Fin de l'entraînement.","color":"yellow"}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
execute if score Rouge mg.tw > Bleu mg.tw run return run function mg:core/win_red
execute if score Bleu mg.tw > Rouge mg.tw run return run function mg:core/win_blue
function mg:core/draw
