# survival2 : préparation (zone chargée par survival2/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -42 80 34358 run return run schedule function mg:survival2/prepare_b 20t
execute unless loaded 42 80 34442 run return run schedule function mg:survival2/prepare_b 20t
execute unless loaded 0 80 34400 run return run schedule function mg:survival2/prepare_b 20t
execute unless loaded -52 80 34548 run return run schedule function mg:survival2/prepare_b 20t
execute unless loaded 52 80 34652 run return run schedule function mg:survival2/prepare_b 20t
execute unless loaded 0 80 34600 run return run schedule function mg:survival2/prepare_b 20t
execute if score $game mg.st matches 202 run function mg:uhc2/prepare
execute if score $game mg.st matches 203 run function mg:hg2/prepare
