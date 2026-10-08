# Spleef : un seul joueur reste sur l'étage occupé le plus haut (les autres sont en dessous) → cet étage disparaît après 5 s
# (évite les parties bloquées). Appelé chaque tick après le calcul de mg.t (hauteur des joueurs). $tff = étage visé (0 = aucun), $tfc = ticks restants
execute if score $ar mg.st matches 1.. run return run function mg:var/floor/top_check
scoreboard players set $tfn mg.st 0
scoreboard players set #tf20 mg.st 20
execute store result score $tf1 mg.st if entity @a[tag=mg.play,scores={mg.t=81..}]
execute store result score $tf2 mg.st if entity @a[tag=mg.play,scores={mg.t=74..}]
execute store result score $tf3 mg.st if entity @a[tag=mg.play,scores={mg.t=67..}]
execute if score $tf1 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 1
execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 2
execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 0 if score $tf3 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 3
execute if score $tfn mg.st matches 0 run return run scoreboard players set $tff mg.st 0
# Nouvelle situation → compte à rebours de 5 s
execute unless score $tfn mg.st = $tff mg.st run tellraw @a[tag=!mg.surv] [{"text":"⚠ ","color":"gold"},{"text":"Un joueur est seul en haut : l'étage disparaît dans 5 secondes !","color":"gold"}]
execute unless score $tfn mg.st = $tff mg.st run scoreboard players set $tfc mg.st 100
scoreboard players operation $tff mg.st = $tfn mg.st
scoreboard players remove $tfc mg.st 1
scoreboard players operation $tfs mg.st = $tfc mg.st
scoreboard players add $tfs mg.st 19
scoreboard players operation $tfs mg.st /= #tf20 mg.st
title @a[tag=!mg.surv,tag=!mg.lk] actionbar [{"text":"⚠ L'étage du haut disparaît dans ","color":"gold"},{"score":{"name":"$tfs","objective":"mg.st"},"color":"red","bold":true},{"text":" s","color":"gold"}]
execute if score $tfc mg.st matches 80 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1
execute if score $tfc mg.st matches 60 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.2
execute if score $tfc mg.st matches 40 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.4
execute if score $tfc mg.st matches 20 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.6
execute if score $tfc mg.st matches 1.. run return 0
execute if score $tff mg.st matches 1 run fill -14 80 286 14 80 314 minecraft:air replace minecraft:snow_block
execute if score $tff mg.st matches 2 run fill -12 73 288 12 73 312 minecraft:air replace minecraft:snow_block
execute if score $tff mg.st matches 3 run fill -10 66 290 10 66 310 minecraft:air replace minecraft:snow_block
tellraw @a[tag=!mg.surv] [{"text":"💥 L'étage du haut a disparu !","color":"red","bold":true}]
execute as @a[tag=mg.play] at @s run playsound minecraft:block.snow.break master @s ~ ~ ~ 1 0.5
scoreboard players set $tff mg.st 0
