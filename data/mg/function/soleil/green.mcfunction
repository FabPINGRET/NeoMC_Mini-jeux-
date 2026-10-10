# Feu vert : la poupée tourne le dos ; durée au hasard (plus courte avec le temps)
scoreboard players set $sqp mg.st 0
function mg:soleil/turn {yaw:0}
execute as @e[tag=mg.sqeye] run data merge entity @s {block_state:{Name:"minecraft:black_concrete"}}
execute store result score $sqt mg.st run random value 35..90
execute if score $sqc mg.st matches 600.. store result score $sqt mg.st run random value 25..65
execute if score $sqc mg.st matches 1200.. store result score $sqt mg.st run random value 15..45
title @a[tag=mg.play] times 0 30 5
title @a[tag=mg.play] title {"text":"1, 2, 3…","color":"green","bold":true}
title @a[tag=mg.play] subtitle {"text":"avance !","color":"gray"}
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.8 0.8
