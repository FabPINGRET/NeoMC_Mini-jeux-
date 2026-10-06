# Nouvelle manche : nouvelle disposition, tout le monde en haut, décompte 3 s
scoreboard players add $rd mg.st 1
function mg:dropper/build_round
execute as @a[tag=mg.play] run function mg:dropper/to_top
scoreboard players set $dph mg.st 3
scoreboard players set $dtm mg.st 60
title @a[tag=mg.play] title [{"text":"Manche ","color":"aqua"},{"score":{"name":"$rd","objective":"mg.st"},"color":"aqua"}]
title @a[tag=mg.play] subtitle [{"text":"Nouvelle disposition d'obstacles !","color":"gray"}]
