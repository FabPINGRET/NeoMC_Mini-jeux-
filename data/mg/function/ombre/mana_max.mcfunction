# @s : mana max = 50 + 4 × niveau + 8 × Esprit (+40 mage, +20 clerc)
scoreboard players operation @s mg.olmm = @s mg.ollv
scoreboard players operation @s mg.olmm *= #4 mg.st
scoreboard players add @s mg.olmm 50
scoreboard players operation $e mg.st = @s mg.ols4
scoreboard players operation $e mg.st *= #8 mg.st
scoreboard players operation @s mg.olmm += $e mg.st
execute if score @s mg.olcl matches 3 run scoreboard players add @s mg.olmm 40
execute if score @s mg.olcl matches 4 run scoreboard players add @s mg.olmm 20
execute if score @s mg.olmp > @s mg.olmm run scoreboard players operation @s mg.olmp = @s mg.olmm
