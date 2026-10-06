execute if score $sg mg.st matches 1 run return run function mg:dropper/to_top_s
# Téléporte @s en haut de son couloir (sur le sol de départ en verre)
scoreboard players operation $tx mg.st = @s mg.ln
scoreboard players operation $tx mg.st *= $c8 mg.st
scoreboard players add $tx mg.st 3
execute store result storage mg:d x int 1 run scoreboard players get $tx mg.st
function mg:dropper/tp_top with storage mg:d
scoreboard players set @s mg.cd 10
effect clear @s minecraft:slow_falling
