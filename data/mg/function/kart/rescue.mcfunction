# Tombé à l'eau ou dans le vide : remis au point de passage précédent (@s = pilote)
scoreboard players operation $ki mg.st = @s mg.kcp
scoreboard players remove $ki mg.st 1
execute if score $ki mg.st matches ..-1 run scoreboard players operation $ki mg.st = $kK mg.st
execute if score $ki mg.st = $kK mg.st run scoreboard players remove $ki mg.st 1
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] run function mg:kart/cp_tp
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s on passengers run rotate @s ~ 0
scoreboard players set @s mg.ksp 0
scoreboard players set @s mg.kvy 0
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
scoreboard players set @s mg.khi 0
title @s actionbar [{"text":"☁ Remis en piste !","color":"aqua"}]
execute at @s run playsound minecraft:entity.chicken.egg master @s ~ ~ ~ 1 1
