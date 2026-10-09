# survival3 : préparation (zone chargée par survival3/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -42 80 34758 run return run schedule function mg:survival3/prepare_b 20t
execute unless loaded 42 80 34842 run return run schedule function mg:survival3/prepare_b 20t
execute unless loaded 0 80 34800 run return run schedule function mg:survival3/prepare_b 20t
execute unless loaded -52 80 34948 run return run schedule function mg:survival3/prepare_b 20t
execute unless loaded 52 80 35052 run return run schedule function mg:survival3/prepare_b 20t
execute unless loaded 0 80 35000 run return run schedule function mg:survival3/prepare_b 20t
execute if score $game mg.st matches 204 run function mg:uhc3/prepare
execute if score $game mg.st matches 205 run function mg:hg3/prepare
