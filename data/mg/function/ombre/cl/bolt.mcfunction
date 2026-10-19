# Trait magique du bâton (gratuit)
execute if score @s mg.olc0 matches 1.. run return 0
scoreboard players set @s mg.olc0 12
function mg:ombre/cl/pow
scoreboard players operation $d mg.st = $pw mg.st
scoreboard players add $d mg.st 4
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
playsound minecraft:entity.illusioner.cast_spell player @a ~ ~ ~ 0.6 1.6
scoreboard players set $olr mg.st 0
execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/boltr
function mg:ombre/cl/end
