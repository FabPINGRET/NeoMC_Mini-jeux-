# @s = bateau : vitesse (|dx| + |dz|, centièmes de bloc par tick) depuis le tick précédent
execute store result score $x mg.st run data get entity @s Pos[0] 100
execute store result score $z mg.st run data get entity @s Pos[2] 100
scoreboard players operation $dx mg.st = $x mg.st
scoreboard players operation $dx mg.st -= @s mg.atx
scoreboard players operation $dz mg.st = $z mg.st
scoreboard players operation $dz mg.st -= @s mg.atz
execute if score $dx mg.st matches ..-1 run scoreboard players operation $dx mg.st *= #m1 mg.st
execute if score $dz mg.st matches ..-1 run scoreboard players operation $dz mg.st *= #m1 mg.st
scoreboard players operation @s mg.atv = $dx mg.st
scoreboard players operation @s mg.atv += $dz mg.st
execute unless score @s mg.atx matches -2147483648.. run scoreboard players set @s mg.atv 0
scoreboard players operation @s mg.atx = $x mg.st
scoreboard players operation @s mg.atz = $z mg.st
execute if score @s mg.atc matches 1.. run scoreboard players remove @s mg.atc 1
