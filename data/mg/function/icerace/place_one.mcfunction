# Course de glace — place le joueur (@s) sur la grille et le met dans un bateau
scoreboard players add $ri mg.st 1
scoreboard players operation @s mg.ri = $ri mg.st
execute if score $ri mg.st matches 1 run tp @s -20.5 81 13226.5 270 0
execute if score $ri mg.st matches 2 run tp @s -20.5 81 13229.5 270 0
execute if score $ri mg.st matches 3 run tp @s -20.5 81 13232.5 270 0
execute if score $ri mg.st matches 4 run tp @s -23.5 81 13226.5 270 0
execute if score $ri mg.st matches 5 run tp @s -23.5 81 13229.5 270 0
execute if score $ri mg.st matches 6 run tp @s -23.5 81 13232.5 270 0
execute if score $ri mg.st matches 7 run tp @s -26.5 81 13226.5 270 0
execute if score $ri mg.st matches 8 run tp @s -26.5 81 13229.5 270 0
execute if score $ri mg.st matches 9 run tp @s -26.5 81 13232.5 270 0
execute if score $ri mg.st matches 10 run tp @s -29.5 81 13226.5 270 0
execute if score $ri mg.st matches 11 run tp @s -29.5 81 13229.5 270 0
execute if score $ri mg.st matches 12 run tp @s -29.5 81 13232.5 270 0
execute if score $ri mg.st matches 13 run tp @s -32.5 81 13226.5 270 0
execute if score $ri mg.st matches 14 run tp @s -32.5 81 13229.5 270 0
execute if score $ri mg.st matches 15 run tp @s -32.5 81 13232.5 270 0
execute if score $ri mg.st matches 16 run tp @s -35.5 81 13226.5 270 0
execute if score $ri mg.st matches 17 run tp @s -35.5 81 13229.5 270 0
execute if score $ri mg.st matches 18 run tp @s -35.5 81 13232.5 270 0
execute if score $ri mg.st matches 19 run tp @s -38.5 81 13226.5 270 0
execute if score $ri mg.st matches 20 run tp @s -38.5 81 13229.5 270 0
execute if score $ri mg.st matches 21 run tp @s -38.5 81 13232.5 270 0
execute if score $ri mg.st matches 22 run tp @s -41.5 81 13226.5 270 0
execute if score $ri mg.st matches 23 run tp @s -41.5 81 13229.5 270 0
execute if score $ri mg.st matches 24.. run tp @s -41.5 81 13232.5 270 0
execute at @s run summon minecraft:birch_boat ~ ~ ~ {Invulnerable:1b,Rotation:[270.0f,0.0f],Tags:["mg.ib","mg.mine"]}
scoreboard players operation @e[tag=mg.mine,limit=1] mg.ri = @s mg.ri
ride @s mount @e[tag=mg.mine,limit=1]
tag @e[tag=mg.ib] remove mg.mine
