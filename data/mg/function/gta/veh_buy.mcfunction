# @s achète un véhicule de type $(t) : l'ancien disparaît, le nouveau est livré
scoreboard players operation $gv mg.st = @s mg.gveh
execute if score @s mg.gveh matches 1.. as @e[tag=mg.gta] if score @s mg.gvid = $gv mg.st run kill @s
$function mg:gta/veh_$(t)
scoreboard players operation @s mg.gveh = $gvid mg.st
execute as @e[tag=mg.gta,type=!minecraft:block_display,type=!minecraft:interaction] if score @s mg.gvid = $gvid mg.st run effect give @s minecraft:glowing 60 0 true
title @s title {"text":"🔑","color":"gold"}
$function mg:gta/veh_where_$(t)
