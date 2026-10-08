# Le convoi est arrivé
execute if score $cvm mg.st matches 1 run return run function mg:convoy/coop_win
tellraw @a[tag=mg.play] {"text":"🚚 Le convoi est arrivé !","color":"gold","bold":true}
function mg:convoy/round_end
