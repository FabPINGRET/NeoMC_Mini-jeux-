# Bedwars — une seule équipe restante : laquelle ? (grâce comprise : équipe hors ligne, lit intact)
execute if score $gr_red mg.st matches 1.. run function mg:core/win_red
execute if score $gr_blue mg.st matches 1.. run function mg:core/win_blue
execute if score $gr_green mg.st matches 1.. run function mg:core/win_green
execute if score $gr_yellow mg.st matches 1.. run function mg:core/win_yellow
