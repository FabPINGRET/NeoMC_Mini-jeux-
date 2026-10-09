# @s : voiture PNJ bloquée depuis 15 s : elle disparaît (une autre apparaîtra ailleurs)
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[tag=mg.gta,type=!minecraft:marker] if score @s mg.gvid = $gv mg.st run kill @s
kill @s
