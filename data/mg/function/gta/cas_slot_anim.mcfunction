# @s (tag mg.gslot) : une image de l'animation de la machine à sous
scoreboard players add @s mg.gsa 1
scoreboard players set #6 mg.st 6
scoreboard players set #2 mg.st 2
scoreboard players operation $ga mg.st = @s mg.gsa
scoreboard players operation $ga mg.st /= #2 mg.st
scoreboard players operation $gi1 mg.st = $ga mg.st
scoreboard players add $gi1 mg.st 0
scoreboard players operation $gi1 mg.st %= #6 mg.st
execute if score @s mg.gsa matches 20.. run scoreboard players operation $gi1 mg.st = @s mg.gs1
execute store result storage mg:gta sl.i1 int 1 run scoreboard players get $gi1 mg.st
scoreboard players operation $gi2 mg.st = $ga mg.st
scoreboard players add $gi2 mg.st 2
scoreboard players operation $gi2 mg.st %= #6 mg.st
execute if score @s mg.gsa matches 30.. run scoreboard players operation $gi2 mg.st = @s mg.gs2
execute store result storage mg:gta sl.i2 int 1 run scoreboard players get $gi2 mg.st
scoreboard players operation $gi3 mg.st = $ga mg.st
scoreboard players add $gi3 mg.st 4
scoreboard players operation $gi3 mg.st %= #6 mg.st
execute if score @s mg.gsa matches 42.. run scoreboard players operation $gi3 mg.st = @s mg.gs3
execute store result storage mg:gta sl.i3 int 1 run scoreboard players get $gi3 mg.st
function mg:gta/cas_slot_pick with storage mg:gta sl
execute if score @s mg.gsa matches ..41 run function mg:gta/cas_slot_show with storage mg:gta sl
scoreboard players operation $gp mg.st = @s mg.gsa
scoreboard players operation $gp mg.st %= #2 mg.st
execute if score @s mg.gsa matches ..41 if score $gp mg.st matches 0 run playsound minecraft:block.note_block.hat player @a ~ ~ ~ 0.35 1.8
execute if score @s mg.gsa matches 20 run playsound minecraft:block.note_block.basedrum player @a ~ ~ ~ 0.9 0.8
execute if score @s mg.gsa matches 30 run playsound minecraft:block.note_block.basedrum player @a ~ ~ ~ 0.9 1.0
execute if score @s mg.gsa matches 42 run playsound minecraft:block.note_block.basedrum player @a ~ ~ ~ 0.9 1.2
execute if score @s mg.gsa matches 42.. run function mg:gta/cas_slot_final with storage mg:gta sl
execute if score @s mg.gsa matches 42.. run function mg:gta/cas_slot_end
execute if score @s mg.gsa matches 42.. run function mg:gta/cas_reopen {d:"slot"}
execute if score @s mg.gsa matches 42.. run tag @s remove mg.gslot
