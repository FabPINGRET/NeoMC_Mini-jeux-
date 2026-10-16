# Mine : préparation (zone chargée par zmode7/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -36 80 40164 run return run schedule function mg:zmode7/prepare_b 20t
execute unless loaded 54 80 40236 run return run schedule function mg:zmode7/prepare_b 20t
execute unless loaded 9 80 40200 run return run schedule function mg:zmode7/prepare_b 20t
execute if score $game mg.st matches 237 run function mg:zm7/prepare
execute if score $game mg.st matches 238 run function mg:inf7/prepare
