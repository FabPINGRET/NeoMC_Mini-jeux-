# Chaque seconde, @s : étapes de la campagne qui se valident en arrivant quelque part
execute if score @s mg.trch matches 30 positioned -62 64 -168 if entity @s[distance=..14] run function mg:terra/rpg/ch {n:32}
execute if score @s mg.trch matches 50 positioned 128 71 6 if entity @s[distance=..9] run function mg:terra/rpg/ch {n:52}
execute if score @s mg.trch matches 60 positioned -200 65 4 if entity @s[distance=..30] run function mg:terra/rpg/ch {n:62}
execute if score @s mg.trch matches 72 positioned 58 86 176 if entity @s[distance=..9] run function mg:terra/rpg/ch {n:75}
execute if score @s mg.trch matches 75 positioned 0 99 186 if entity @s[distance=..15] run function mg:terra/rpg/ch {n:80}
execute if score @s mg.trch matches 85 positioned 0.5 99 177.5 if entity @s[distance=..3.5] run function mg:terra/rpg/rift
