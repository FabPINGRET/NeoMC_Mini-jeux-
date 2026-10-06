# Rattrapage : joueur hors-jeu tombé dans le vide (@s = joueur, position exécutée)
execute store result score @s mg.t run data get entity @s Pos[1]
execute if score @s mg.t matches ..-10 run tp @s 0.5 64 0.5
execute if score @s mg.t matches ..-10 run tellraw @s [{"text":"Ouf ! Rattrapé de justesse.","color":"aqua","italic":true}]
execute if score @s mg.t matches ..-10 run function mg:core/fall_heal
