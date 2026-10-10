# @s a-t-il bougé (> 0,1 bloc) depuis la marque ?
execute store result score $a mg.st run data get entity @s Pos[0] 100
scoreboard players operation $a mg.st -= @s mg.msx
execute unless score $a mg.st matches -10..10 run return run tag @s add mg.msf
execute store result score $a mg.st run data get entity @s Pos[2] 100
scoreboard players operation $a mg.st -= @s mg.msz
execute unless score $a mg.st matches -10..10 run tag @s add mg.msf
