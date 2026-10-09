# Manoir : préparation (zone chargée par zmode3/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -17 80 36061 run return run schedule function mg:zmode3/prepare_b 20t
execute unless loaded 39 80 36117 run return run schedule function mg:zmode3/prepare_b 20t
execute unless loaded 11 80 36089 run return run schedule function mg:zmode3/prepare_b 20t
execute if score $game mg.st matches 212 run function mg:zm3/prepare
execute if score $game mg.st matches 213 run function mg:inf3/prepare
