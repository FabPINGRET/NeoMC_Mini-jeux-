# Thermes : préparation (zone chargée par zmode9/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -26 80 42468 run return run schedule function mg:zmode9/prepare_b 20t
execute unless loaded 26 80 42528 run return run schedule function mg:zmode9/prepare_b 20t
execute unless loaded 0 80 42498 run return run schedule function mg:zmode9/prepare_b 20t
execute if score $game mg.st matches 249 run function mg:zm9/prepare
execute if score $game mg.st matches 250 run function mg:inf9/prepare
