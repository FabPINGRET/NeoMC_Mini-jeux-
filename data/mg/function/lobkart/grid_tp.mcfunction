# Place @s (le pilote) sur une des 6 places de départ ($lgi 0..5), tourné vers la piste
execute if score $lgi mg.st matches 0 run return run tp @s -2.9 64 64.0 -90.9 0
execute if score $lgi mg.st matches 1 run return run tp @s -2.9 64 68.0 -90.9 0
execute if score $lgi mg.st matches 2 run return run tp @s -7.1 64 64.2 -95.5 0
execute if score $lgi mg.st matches 3 run return run tp @s -6.7 64 68.2 -95.5 0
execute if score $lgi mg.st matches 4 run return run tp @s -11.3 64 65.0 -104.0 0
execute if score $lgi mg.st matches 5 run return run tp @s -10.3 64 68.8 -104.0 0
