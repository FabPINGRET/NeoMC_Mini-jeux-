# Splegg — tick de jeu

# Nouveaux œufs : on recharge la main du tireur (munitions infinies)
execute as @e[distance=0..,type=minecraft:egg,tag=!mg.eg] at @s run function mg:splegg/egg_new
# Œufs en vol : traînée de neige + rayon court devant l'œuf (la neige se casse là où l'œuf passe)
execute as @e[distance=0..,type=minecraft:egg,tag=mg.eg] at @s run function mg:splegg/egg_tick

# Pas de poussins quand un œuf éclate
kill @e[distance=0..,type=minecraft:chicken]

# Chute dans le vide → éliminé
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play] if score @s mg.t <= $yd mg.st run function mg:core/eliminate

# Mort accidentelle → éliminé
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate

# Victoire
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw

# Un seul joueur reste sur l'étage du haut → il disparaît après 5 s
execute if score $state mg.st matches 2 run function mg:splegg/top_check
