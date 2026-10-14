# Usine : préparation (zone chargée par zmode4/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -36 80 39042 run return run schedule function mg:zmode4/prepare_b 20t
execute unless loaded 40 80 39120 run return run schedule function mg:zmode4/prepare_b 20t
execute unless loaded 2 80 39081 run return run schedule function mg:zmode4/prepare_b 20t
execute if score $game mg.st matches 229 run function mg:zm4/prepare
execute if score $game mg.st matches 230 run function mg:inf4/prepare
