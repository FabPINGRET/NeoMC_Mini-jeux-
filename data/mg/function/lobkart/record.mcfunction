# Nouveau record du circuit du spawn (@s ; $s / $d déjà calculés)
scoreboard players operation $klrec mg.st = @s mg.klt
tellraw @a[tag=!mg.surv] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record du circuit du spawn : ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"gold","bold":true},{"text":".","color":"gold"},{"score":{"name":"$d","objective":"mg.st"},"color":"gold"},{"text":" s !","color":"gold"}]
execute store result storage mg:lk s int 1 run scoreboard players get $s mg.st
execute store result storage mg:lk d int 1 run scoreboard players get $d mg.st
function mg:lobkart/board with storage mg:lk
