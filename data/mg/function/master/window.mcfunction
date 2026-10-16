# Pendant le délai : on note qui fait l'action (mg.mso) ou qui tombe dans le piège / bouge (mg.msf)
scoreboard players operation $e mg.st = $msw mg.st
scoreboard players operation $e mg.st -= $mst mg.st
execute as @a[tag=mg.play,scores={mg.mo=1,mg.mv=1}] if predicate mg:ms_jump run tag @s add mg.mso
execute as @a[tag=mg.play,scores={mg.mo=2,mg.mv=1}] if predicate mg:sneak run tag @s add mg.mso
execute as @a[tag=mg.play,scores={mg.mo=3,mg.mv=1}] if predicate mg:ms_sprint run tag @s add mg.mso
execute as @a[tag=mg.play,scores={mg.mo=4..5}] run function mg:master/pitch
execute as @a[tag=mg.play,scores={mg.mo=4,mg.t=..-50}] run tag @s add mg.mso
execute as @a[tag=mg.play,scores={mg.mo=5,mg.t=50..}] run tag @s add mg.mso
execute if score $e mg.st matches 12 as @a[tag=mg.play,scores={mg.mo=6}] run function mg:master/mark
execute if score $e mg.st matches 13.. as @a[tag=mg.play,scores={mg.mo=6}] run function mg:master/moved
execute if score $e mg.st matches 6.. as @a[tag=mg.play,scores={mg.mo=1,mg.mv=0}] if predicate mg:ms_jump run tag @s add mg.msf
execute if score $e mg.st matches 6.. as @a[tag=mg.play,scores={mg.mo=2,mg.mv=0}] if predicate mg:sneak run tag @s add mg.msf
execute if score $e mg.st matches 6.. as @a[tag=mg.play,scores={mg.mo=3,mg.mv=0}] if predicate mg:ms_sprint run tag @s add mg.msf
