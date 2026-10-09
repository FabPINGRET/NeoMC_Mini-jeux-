# @s (quille tombée) : position, hauteur (fosse / gouttière / piste)
function mg:bowl/pos
execute if score @s mg.bz matches 19600.. run return run data modify entity @s Pos[1] set value 63.0d
execute unless score @s mg.bx matches -1600..1600 run return run data modify entity @s Pos[1] set value 64.0d
data modify entity @s Pos[1] set value 65.0d
