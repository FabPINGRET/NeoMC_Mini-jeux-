# Phase 1 : toutes les 20 s, la gravité s'inverse pendant 5 s
scoreboard players operation $m1 mg.st = $bc mg.st
scoreboard players operation $m1 mg.st %= $k400 mg.st
execute if score $m1 mg.st matches 300 run function mg:mobarena/ship/invert_on
execute if score $m1 mg.st matches 0 run function mg:mobarena/ship/invert_off
