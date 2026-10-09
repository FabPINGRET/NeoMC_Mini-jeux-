# @s : calage (angle droit le plus proche ; en pose « bloc », centre du bloc)
execute store result score $cmr mg.st run data get entity @s Rotation[0]
scoreboard players add $cmr mg.st 405
scoreboard players set #90 mg.st 90
scoreboard players set #360 mg.st 360
scoreboard players operation $cmr mg.st /= #90 mg.st
scoreboard players operation $cmr mg.st *= #90 mg.st
scoreboard players operation $cmr mg.st %= #360 mg.st
execute store result storage mg:cham s.y int 1 run scoreboard players get $cmr mg.st
execute if score @s mg.cmpo matches 6 align xz positioned ~0.5 ~ ~0.5 run function mg:cham/snap_at with storage mg:cham s
execute unless score @s mg.cmpo matches 6 run function mg:cham/snap_at with storage mg:cham s
title @s actionbar {"text":"🔒 Calé : ne bouge plus !","color":"green"}
execute at @s run playsound minecraft:block.wool.place player @s ~ ~ ~ 0.5 0.8
