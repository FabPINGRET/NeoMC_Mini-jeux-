# Barre du bas du pilote du spawn (@s) : tour, chrono, meilleur tour, vitesse
scoreboard players operation $kmh mg.st = @s mg.ksp
scoreboard players operation $kmh mg.st *= #kkmh mg.st
scoreboard players operation $kmh mg.st /= #k100 mg.st
execute if score $kmh mg.st matches ..-1 run scoreboard players operation $kmh mg.st *= #km1 mg.st
execute if score @s mg.klp matches 0 run return run title @s actionbar [{"text":"🏁 Passe la ligne de départ pour lancer le chrono  ","color":"gold"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]
scoreboard players operation $s mg.st = @s mg.klt
scoreboard players operation $s mg.st /= #k20 mg.st
scoreboard players operation $d mg.st = @s mg.klt
scoreboard players operation $d mg.st %= #k20 mg.st
scoreboard players operation $d mg.st /= #k2 mg.st
scoreboard players operation $bs mg.st = @s mg.klb
scoreboard players operation $bs mg.st /= #k20 mg.st
scoreboard players operation $bd mg.st = @s mg.klb
scoreboard players operation $bd mg.st %= #k20 mg.st
scoreboard players operation $bd mg.st /= #k2 mg.st
execute unless score @s mg.klb matches 1.. run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":"   ⏱ ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s   ","color":"gray"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]
execute if score @s mg.klb matches 1.. run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":"   ⏱ ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s   ★ ","color":"gold"},{"score":{"name":"$bs","objective":"mg.st"},"color":"yellow"},{"text":".","color":"yellow"},{"score":{"name":"$bd","objective":"mg.st"},"color":"yellow"},{"text":" s   ","color":"gray"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]
