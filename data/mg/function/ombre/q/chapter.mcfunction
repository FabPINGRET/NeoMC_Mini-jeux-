# @s : titre du nouveau chapitre
title @s times 15 70 20
$title @s title {"text":"$(t)","color":"gold","bold":true}
title @s subtitle {"text":"Nouveau chapitre","color":"gray"}
execute at @s run playsound minecraft:event.mob_effect.raid_omen player @s ~ ~ ~ 0.6 1.2
