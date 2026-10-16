# @s a tenu l'outpost
scoreboard players add @s mg.tvc 250
function mg:terra/rpg/xp {n:125}
scoreboard players set @s mg.tval 40
title @s actionbar [{"text":"+250 ₵ ","color":"aqua","bold":true},{"text":"outpost défendu","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2
function mg:terra/mis_clear
title @s title {"text":"✔ Outpost défendu","color":"aqua","bold":true}
title @s subtitle {"text":"+250 ₵","color":"green"}
