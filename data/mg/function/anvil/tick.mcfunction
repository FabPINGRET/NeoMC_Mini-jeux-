# Pluie d'Enclumes — tick de jeu

# Génération d'enclumes
scoreboard players remove $ac mg.st 1
execute if score $ac mg.st matches ..0 run function mg:anvil/spawn_event

# Montée en intensité toutes les 8 s
scoreboard players remove $lt mg.st 1
execute if score $lt mg.st matches ..0 run function mg:anvil/level_up

# Variante sol troué
execute if score $sg mg.st matches 2 run function mg:anvil/hole_tick

# Ombres d'avertissement
execute as @e[type=minecraft:marker,tag=mg.sh] at @s run function mg:anvil/shadow_tick

# Nettoyage des enclumes posées (toutes les 0,5 s)
scoreboard players remove $cl mg.st 1
execute if score $cl mg.st matches ..0 run function mg:anvil/cleanup

# Mort (enclume) ou chute → éliminé
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:core/eliminate

# Victoire
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
