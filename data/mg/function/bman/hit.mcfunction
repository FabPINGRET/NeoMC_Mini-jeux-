# @s est dans les flammes
execute unless score $n0 mg.st matches 2.. run return run function mg:bman/train_hit
execute at @s run particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.05 20 force
function mg:core/eliminate
