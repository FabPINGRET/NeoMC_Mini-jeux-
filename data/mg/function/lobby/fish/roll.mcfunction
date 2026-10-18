# @s : tirage de la prise (1..1000, dans #lfr) : un seuil cumulé par prise, la première qui correspond termine
execute store result score #lfr mg.st run random value 1..1000
execute if score #lfr mg.st matches ..160 run return run function mg:lobby/fish/c_gardon
execute if score #lfr mg.st matches ..320 run return run function mg:lobby/fish/c_truite
execute if score #lfr mg.st matches ..460 run return run function mg:lobby/fish/c_perche
execute if score #lfr mg.st matches ..600 run return run function mg:lobby/fish/c_carpe
execute if score #lfr mg.st matches ..660 run return run function mg:lobby/fish/c_brochet
execute if score #lfr mg.st matches ..700 run return run function mg:lobby/fish/c_esturgeon
execute if score #lfr mg.st matches ..730 run return run function mg:lobby/fish/c_dore
execute if score #lfr mg.st matches ..820 run return run function mg:lobby/fish/c_botte
execute if score #lfr mg.st matches ..890 run return run function mg:lobby/fish/c_canard
execute if score #lfr mg.st matches ..950 run return run function mg:lobby/fish/c_chaussette
execute if score #lfr mg.st matches ..1000 run return run function mg:lobby/fish/c_bidon
