# Après la 2e manche : rouges = manche 1, bleus = manche 2
execute if score $cvs1 mg.st > $cvs2 mg.st run return run function mg:core/win_red
execute if score $cvs2 mg.st > $cvs1 mg.st run return run function mg:core/win_blue
function mg:core/draw
