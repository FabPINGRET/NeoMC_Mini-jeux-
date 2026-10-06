# Impact sur un bloc (position = bloc touché) : peint un cube 3x3x3 aux couleurs du tireur
execute if score $st mg.st matches 1 run function mg:paintball/splat_o
execute if score $st mg.st matches 2 run function mg:paintball/splat_b
