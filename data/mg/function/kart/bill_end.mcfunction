scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] on passengers if entity @s[tag=mg.kbillm] run kill @s
title @s actionbar [{"text":"Fin du Bill Balle","color":"gray"}]
