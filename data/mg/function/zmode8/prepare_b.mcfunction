# Catacombes : préparation (zone chargée par zmode8/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -27 80 42068 run return run schedule function mg:zmode8/prepare_b 20t
execute unless loaded 27 80 42132 run return run schedule function mg:zmode8/prepare_b 20t
execute unless loaded 0 80 42100 run return run schedule function mg:zmode8/prepare_b 20t
execute if score $game mg.st matches 247 run function mg:zm8/prepare
execute if score $game mg.st matches 248 run function mg:inf8/prepare
