# Passes complètes : la vague est rejouée une fois par tranche de 4 joueurs en plus (récursif, 5 passes max = 24 joueurs)
execute unless score $mex mg.st matches 4.. run return 0
function mg:mobarena/wave with storage mg:mw
scoreboard players remove $mex mg.st 4
function mg:mobarena/scale_pass
