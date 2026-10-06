# Nouveau record du lobby (@s = coureur ; $s/$d déjà calculés)
scoreboard players operation $pkrec mg.st = @s mg.ppt
tellraw @a [{"text":"NOUVEAU RECORD DU PARKOUR !","color":"gold","bold":true}]
execute store result storage mg:pk s int 1 run scoreboard players get $s mg.st
execute store result storage mg:pk d int 1 run scoreboard players get $d mg.st
function mg:parkour/board with storage mg:pk
