# Départ : portillon ouvert
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 1.4
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 0.8 1.4
title @a[tag=mg.play] title [{"text":"GO !","color":"green","bold":true}]
function mg:kart/gate_off
scoreboard players set $ktime mg.st 0
scoreboard players set @a[tag=mg.play] mg.ksp 0
execute if score $kbat mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🎈 ","color":"red"},{"text":"BATAILLE","color":"red","bold":true},{"text":" : chaque pilote a 3 ballons. Un coup (objet, Chomp, chute dans les douves) en crève un ; plus de ballon = éliminé. Dernier en lice ou le plus de ballons au bout de 3 minutes ! Boîtes ? = objets (dans toute la barre), clic droit pour les utiliser.","color":"gray"}]
execute unless score $kbat mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"KART","color":"gold","bold":true},{"text":" : Z avancer, S freiner / reculer, Q / D tourner, ","color":"gray"},{"text":"ESPACE en tournant = dérapage","color":"yellow"},{"text":" (relâche après les étincelles bleues, orange ou violettes pour un mini-turbo). Boîtes ? = objets (dans toute la barre), clic droit pour les utiliser (F5 = vue 3e personne). 3 tours !","color":"gray"}]
