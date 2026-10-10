# Pendant le délai : on note qui fait l'action (mg.mso) ou qui tombe dans le piège / bouge (mg.msf)
scoreboard players operation $e mg.st = $msw mg.st
scoreboard players operation $e mg.st -= $mst mg.st
execute if score $msv mg.st matches 1 if score $mso mg.st matches 1 as @a[tag=mg.play] if predicate mg:ms_jump run tag @s add mg.mso
execute if score $msv mg.st matches 1 if score $mso mg.st matches 2 as @a[tag=mg.play] if predicate mg:sneak run tag @s add mg.mso
execute if score $msv mg.st matches 1 if score $mso mg.st matches 3 as @a[tag=mg.play] if predicate mg:ms_sprint run tag @s add mg.mso
execute if score $mso mg.st matches 4..5 as @a[tag=mg.play] run function mg:master/pitch
execute if score $mso mg.st matches 4 as @a[tag=mg.play,scores={mg.t=..-50}] run tag @s add mg.mso
execute if score $mso mg.st matches 5 as @a[tag=mg.play,scores={mg.t=50..}] run tag @s add mg.mso
execute if score $mso mg.st matches 6 if score $e mg.st matches 12 as @a[tag=mg.play] run function mg:master/mark
execute if score $mso mg.st matches 6 if score $e mg.st matches 13.. as @a[tag=mg.play] run function mg:master/moved
execute if score $msv mg.st matches 0 if score $e mg.st matches 6.. if score $mso mg.st matches 1 as @a[tag=mg.play] if predicate mg:ms_jump run tag @s add mg.msf
execute if score $msv mg.st matches 0 if score $e mg.st matches 6.. if score $mso mg.st matches 2 as @a[tag=mg.play] if predicate mg:sneak run tag @s add mg.msf
execute if score $msv mg.st matches 0 if score $e mg.st matches 6.. if score $mso mg.st matches 3 as @a[tag=mg.play] if predicate mg:ms_sprint run tag @s add mg.msf
