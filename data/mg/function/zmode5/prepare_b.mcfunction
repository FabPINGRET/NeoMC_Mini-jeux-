# Station : préparation (zone chargée par zmode5/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -51 80 39364 run return run schedule function mg:zmode5/prepare_b 20t
execute unless loaded 51 80 39435 run return run schedule function mg:zmode5/prepare_b 20t
execute unless loaded 0 80 39399 run return run schedule function mg:zmode5/prepare_b 20t
execute if score $game mg.st matches 231 run function mg:zm5/prepare
execute if score $game mg.st matches 232 run function mg:inf5/prepare
