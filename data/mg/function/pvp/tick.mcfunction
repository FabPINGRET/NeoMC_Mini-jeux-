# Arène PvP — tick de jeu

# KILL → récompense (soin + repas), seule source de soin avec les pommes d'or
execute as @a[tag=mg.play,scores={mg.pk=1..}] run function mg:pvp/kill_reward

# Mort → éliminé (respawn instantané au perchoir, puis spectateur)
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate

# Sécurité : projeté hors de l'arène
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..55}] run function mg:core/eliminate
execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:core/eliminate

# Victoire
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
