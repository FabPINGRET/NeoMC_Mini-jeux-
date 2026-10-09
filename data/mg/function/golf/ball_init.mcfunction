# @s : balle neuve ($cur = numéro du joueur) : position en scores, couleur du joueur
tag @s remove mg.gfnew
scoreboard players operation @s mg.gfi = $cur mg.st
execute store result score @s mg.gfx run data get entity @s Pos[0] 1000
execute store result score @s mg.gfy run data get entity @s Pos[1] 1000
execute store result score @s mg.gfz run data get entity @s Pos[2] 1000
scoreboard players operation @s mg.gflx = @s mg.gfx
scoreboard players operation @s mg.gfly = @s mg.gfy
scoreboard players operation @s mg.gflz = @s mg.gfz
scoreboard players set @s mg.gfu 0
scoreboard players set @s mg.gfv 0
scoreboard players set @s mg.gfw 0
tag @s add mg.gfg
scoreboard players operation $gfcol mg.st = $cur mg.st
scoreboard players operation $gfcol mg.st %= #gf8 mg.st
execute if score $gfcol mg.st matches 0 run data modify entity @s glow_color_override set value 16777215
execute if score $gfcol mg.st matches 1 run data modify entity @s glow_color_override set value 16733525
execute if score $gfcol mg.st matches 2 run data modify entity @s glow_color_override set value 5592575
execute if score $gfcol mg.st matches 3 run data modify entity @s glow_color_override set value 5635925
execute if score $gfcol mg.st matches 4 run data modify entity @s glow_color_override set value 16777045
execute if score $gfcol mg.st matches 5 run data modify entity @s glow_color_override set value 16733695
execute if score $gfcol mg.st matches 6 run data modify entity @s glow_color_override set value 5636095
execute if score $gfcol mg.st matches 7 run data modify entity @s glow_color_override set value 16755200
