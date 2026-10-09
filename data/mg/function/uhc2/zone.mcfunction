# Zone carrée de demi-côté $zr centrée en (0, 34400) : 2 dégâts/s dehors, particules sur les bords
execute as @a[tag=mg.play] store result score @s mg.tx run data get entity @s Pos[0]
execute as @a[tag=mg.play] store result score @s mg.tz run data get entity @s Pos[2]
scoreboard players remove @a[tag=mg.play] mg.tz 34400
execute as @a[tag=mg.play,scores={mg.tx=..-1}] run scoreboard players operation @s mg.tx *= #-1 mg.st
execute as @a[tag=mg.play,scores={mg.tz=..-1}] run scoreboard players operation @s mg.tz *= #-1 mg.st
execute as @a[tag=mg.play] if score @s mg.tx > $zr mg.st run tag @s add mg.zout
execute as @a[tag=mg.play] if score @s mg.tz > $zr mg.st run tag @s add mg.zout
execute as @a[tag=mg.zout] run damage @s 2 minecraft:outside_border
title @a[tag=mg.zout] actionbar {"text":"⚠ Hors de la zone ! Reviens vers le centre","color":"red","bold":true}
tag @a remove mg.zout
execute store result storage mg:zone r int 1 run scoreboard players get $zr mg.st
scoreboard players operation $zn mg.st = $zr mg.st
scoreboard players operation $zn mg.st *= #-1 mg.st
execute store result storage mg:zone n int 1 run scoreboard players get $zn mg.st
data modify storage mg:zone z set value 34400
scoreboard players set $zp mg.st 34400
scoreboard players operation $zp mg.st += $zr mg.st
scoreboard players set $zm mg.st 34400
scoreboard players operation $zm mg.st -= $zr mg.st
execute store result storage mg:zone zp int 1 run scoreboard players get $zp mg.st
execute store result storage mg:zone zm int 1 run scoreboard players get $zm mg.st
function mg:uhc2/zone_fx with storage mg:zone
