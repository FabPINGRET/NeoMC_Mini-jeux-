# Hôpital : préparation (zone chargée par zmode6/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -40 80 39772 run return run schedule function mg:zmode6/prepare_b 20t
execute unless loaded 56 80 39818 run return run schedule function mg:zmode6/prepare_b 20t
execute unless loaded 8 80 39795 run return run schedule function mg:zmode6/prepare_b 20t
execute if score $game mg.st matches 235 run function mg:zm6/prepare
execute if score $game mg.st matches 236 run function mg:inf6/prepare
