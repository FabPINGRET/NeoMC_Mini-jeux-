# @s a complété le bestiaire
title @s title {"text":"📖 BESTIAIRE COMPLET","color":"aqua","bold":true}
scoreboard players add @s mg.tvc 500
function mg:terra/rpg/xp {n:600}
tellraw @a[tag=mg.tvw] [{"text":"📖 ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" a complété le bestiaire de Terra Nova ! (+500 ₵)","color":"aqua"}]
