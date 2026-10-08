# @s : sa chaîne pour l'étape $tp = (indice + étape) mod N, centre de sa parcelle dans mg.tx / mg.tz
scoreboard players operation @s mg.tc = @s mg.ti
scoreboard players operation @s mg.tc += $tp mg.st
scoreboard players operation @s mg.tc %= $tn mg.st
scoreboard players set #64 mg.st 64
scoreboard players operation @s mg.tx = @s mg.tc
scoreboard players operation @s mg.tx *= #64 mg.st
scoreboard players remove @s mg.tx 352
scoreboard players set @s mg.tz 19500
execute if score $tp mg.st matches 3..4 run scoreboard players add @s mg.tz 64
execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc
execute store result storage mg:tel p.x int 1 run scoreboard players get @s mg.tx
execute store result storage mg:tel p.z int 1 run scoreboard players get @s mg.tz
scoreboard players operation $tvz mg.st = @s mg.tz
scoreboard players remove $tvz mg.st 14
execute store result storage mg:tel p.vz int 1 run scoreboard players get $tvz mg.st
