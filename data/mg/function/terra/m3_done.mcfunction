# @s a abattu ses 5 slashers
scoreboard players add @s mg.tvc 200
scoreboard players set @s mg.tval 40
title @s actionbar [{"text":"+200 ₵ ","color":"green","bold":true},{"text":"chasse réussie","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2
function mg:terra/mis_clear
title @s title {"text":"✔ Chasse réussie","color":"green","bold":true}
title @s subtitle {"text":"+200 ₵","color":"green"}
