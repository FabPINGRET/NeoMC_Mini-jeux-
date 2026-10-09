# @s : voiture PNJ bloquée depuis 15 s : elle disparaît (une autre apparaîtra ailleurs)
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[type=minecraft:block_display,tag=mg.gtrd] if score @s mg.gvid = $gv mg.st run kill @s
kill @s
