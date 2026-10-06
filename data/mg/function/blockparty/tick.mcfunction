# Block Party — tick de jeu

# Chute (sol disparu) → éliminé
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:core/eliminate
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate

# Phase 1 : course vers la couleur ; phase 2 : sol réduit, pause avant la manche suivante
execute if score $bp mg.st matches 1 run function mg:blockparty/run_tick
execute if score $bp mg.st matches 2 run function mg:blockparty/pause_tick

# Victoire
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
