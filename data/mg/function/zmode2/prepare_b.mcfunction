# Laboratoire : préparation (zone chargée par zmode2/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -17 80 35761 run return run schedule function mg:zmode2/prepare_b 20t
execute unless loaded 39 80 35817 run return run schedule function mg:zmode2/prepare_b 20t
execute unless loaded 11 80 35789 run return run schedule function mg:zmode2/prepare_b 20t
execute if score $game mg.st matches 210 run function mg:zm2/prepare
execute if score $game mg.st matches 211 run function mg:inf2/prepare
