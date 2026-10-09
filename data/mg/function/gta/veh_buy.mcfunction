# @s achète un véhicule de type $(t) : l'ancien disparaît, le nouveau est livré
scoreboard players operation $gv mg.st = @s mg.gveh
execute if score @s mg.gveh matches 1.. as @e[tag=mg.gta] if score @s mg.gvid = $gv mg.st run kill @s
$function mg:gta/veh_$(t)
scoreboard players operation @s mg.gveh = $gvid mg.st
title @s title {"text":"🔑","color":"gold"}
title @s subtitle {"text":"Ton véhicule t'attend dehors !","color":"yellow"}
