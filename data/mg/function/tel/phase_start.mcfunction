# Début de l'étape $tp+1 (0 écrire, 1 construire, 2 deviner, 3 construire, 4 deviner, 5 révélation)
scoreboard players add $tp mg.st 1
scoreboard players set $tt mg.st 0
tag @a remove mg.tdone
execute if score $tp mg.st matches 5 run return run function mg:tel/reveal_start
clear @a[tag=mg.play,scores={mg.ti=0..}]
execute if score $tp mg.st matches 0 run scoreboard players set $tlim mg.st 1200
execute if score $tp mg.st matches 1 run scoreboard players set $tlim mg.st 3000
execute if score $tp mg.st matches 2 run scoreboard players set $tlim mg.st 1200
execute if score $tp mg.st matches 3 run scoreboard players set $tlim mg.st 3000
execute if score $tp mg.st matches 4 run scoreboard players set $tlim mg.st 1200
execute if score $tp mg.st matches 0 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/start_write
execute if score $tp mg.st matches 1 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/start_build
execute if score $tp mg.st matches 3 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/start_build
execute if score $tp mg.st matches 2 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/start_guess
execute if score $tp mg.st matches 4 as @a[tag=mg.play,scores={mg.ti=0..}] run function mg:tel/start_guess
execute as @a[tag=mg.play,scores={mg.ti=0..}] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.2
