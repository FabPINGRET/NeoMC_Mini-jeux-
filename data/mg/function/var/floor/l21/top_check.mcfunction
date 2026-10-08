# Sol 21 : un seul joueur reste sur l’étage occupé le plus haut → il disparaît après 15 s. Généré.
scoreboard players set $tfn mg.st 0
scoreboard players set #tf20 mg.st 20
execute store result score $tf1 mg.st if entity @a[tag=mg.play,scores={mg.t=81..}]
execute store result score $tf2 mg.st if entity @a[tag=mg.play,scores={mg.t=77..}]
execute store result score $tf3 mg.st if entity @a[tag=mg.play,scores={mg.t=73..}]
execute if score $tf1 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 1
execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 2
execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 0 if score $tf3 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 3
execute if score $tfn mg.st matches 0 run return run scoreboard players set $tff mg.st 0
execute unless score $tfn mg.st = $tff mg.st run tellraw @a[tag=!mg.surv] [{"text":"⚠ ","color":"gold"},{"text":"Un joueur est seul en haut : l'étage disparaît dans 15 secondes !","color":"gold"}]
execute unless score $tfn mg.st = $tff mg.st run scoreboard players set $tfc mg.st 300
scoreboard players operation $tff mg.st = $tfn mg.st
scoreboard players remove $tfc mg.st 1
scoreboard players operation $tfs mg.st = $tfc mg.st
scoreboard players add $tfs mg.st 19
scoreboard players operation $tfs mg.st /= #tf20 mg.st
title @a[tag=!mg.surv,tag=!mg.lk] actionbar [{"text":"⚠ L'étage du haut disparaît dans ","color":"gold"},{"score":{"name":"$tfs","objective":"mg.st"},"color":"red","bold":true},{"text":" s","color":"gold"}]
execute if score $tfc mg.st matches 1.. run return 0
execute if score $tff mg.st matches 1 run fill -14 80 24286 14 80 24314 minecraft:air replace minecraft:snow_block
execute if score $tff mg.st matches 2 run fill -12 76 24288 12 76 24312 minecraft:air replace minecraft:snow_block
execute if score $tff mg.st matches 3 run fill -10 72 24290 10 72 24310 minecraft:air replace minecraft:snow_block
tellraw @a[tag=!mg.surv] [{"text":"💥 L'étage du haut a disparu !","color":"red","bold":true}]
execute as @a[tag=mg.play] at @s run playsound minecraft:block.snow.break master @s ~ ~ ~ 1 0.5
scoreboard players set $tff mg.st 0
