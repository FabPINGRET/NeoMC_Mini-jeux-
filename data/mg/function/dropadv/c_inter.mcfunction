# Pause de 3 s entre deux manches, puis nouveau niveau
execute if score $dct mg.st matches 60.. run function mg:dropadv/c_pick
execute if score $dct mg.st matches 60.. run function mg:dropadv/c_round
