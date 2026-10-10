# @s pendant le feu rouge : bougé de plus de 0,08 bloc (ou sauté) → éliminé
execute store result score $a mg.st run data get entity @s Pos[0] 100
scoreboard players operation $a mg.st -= @s mg.sqx
execute unless score $a mg.st matches -8..8 run return run function mg:soleil/shot
execute store result score $a mg.st run data get entity @s Pos[2] 100
scoreboard players operation $a mg.st -= @s mg.sqz
execute unless score $a mg.st matches -8..8 run return run function mg:soleil/shot
execute store result score $a mg.st run data get entity @s Pos[1] 100
scoreboard players operation $a mg.st -= @s mg.sqy
execute unless score $a mg.st matches -15..15 run return run function mg:soleil/shot
