# Feu vert : la poupée tourne le dos ; durée au hasard (plus courte avec le temps)
scoreboard players set $sqp mg.st 0
function mg:soleil/turn {yaw:0}
execute as @e[tag=mg.sqeye] run data merge entity @s {block_state:{Name:"minecraft:black_concrete"}}
execute store result score $sqt mg.st run random value 35..90
execute if score $sqc mg.st matches 600.. store result score $sqt mg.st run random value 25..65
execute if score $sqc mg.st matches 1200.. store result score $sqt mg.st run random value 15..45
scoreboard players operation $sqg mg.st = $sqt mg.st
scoreboard players set $sqk mg.st -1
title @a[tag=mg.play] times 0 20 4
title @a[tag=mg.play] subtitle {"text":"avance !","color":"gray"}
