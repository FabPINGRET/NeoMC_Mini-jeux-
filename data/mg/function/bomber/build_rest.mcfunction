# Filet de sécurité : termine la construction d'un coup si le départ arrive avant la fin
execute if score $bbs mg.st matches ..118 run function mg:bomber/build_step
execute if score $bbs mg.st matches ..118 run function mg:bomber/build_rest
