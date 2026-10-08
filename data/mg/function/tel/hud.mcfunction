# Barre d'action : étape + temps restant
scoreboard players operation $tsec mg.st = $tlim mg.st
scoreboard players operation $tsec mg.st -= $tt mg.st
scoreboard players operation $tsec mg.st /= #20 mg.st
execute if score $tp mg.st matches 0 run title @a[tag=mg.play,scores={mg.ti=0..}] actionbar [{"text":"📞 Étape 1/5 : écris un mot   ⏱ ","color":"gold"},{"score":{"name":"$tsec","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gold"}]
execute if score $tp mg.st matches 1 run title @a[tag=mg.play,scores={mg.ti=0..}] actionbar [{"text":"✎ Étape 2/5 : construis   ⏱ ","color":"gold"},{"score":{"name":"$tsec","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gold"}]
execute if score $tp mg.st matches 2 run title @a[tag=mg.play,scores={mg.ti=0..}] actionbar [{"text":"🔍 Étape 3/5 : devine   ⏱ ","color":"aqua"},{"score":{"name":"$tsec","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"aqua"}]
execute if score $tp mg.st matches 3 run title @a[tag=mg.play,scores={mg.ti=0..}] actionbar [{"text":"✎ Étape 4/5 : construis   ⏱ ","color":"gold"},{"score":{"name":"$tsec","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gold"}]
execute if score $tp mg.st matches 4 run title @a[tag=mg.play,scores={mg.ti=0..}] actionbar [{"text":"🔍 Étape 5/5 : devine   ⏱ ","color":"aqua"},{"score":{"name":"$tsec","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"aqua"}]
execute if score $tsec mg.st matches 1..5 as @a[tag=mg.play,scores={mg.ti=0..}] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
