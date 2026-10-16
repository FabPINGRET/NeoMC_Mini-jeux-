# @s a abattu le carnotaure traqué
scoreboard players add @s mg.tvc 400
function mg:terra/rpg/xp {n:200}
scoreboard players set @s mg.tval 40
title @s actionbar [{"text":"+400 ₵ ","color":"gold","bold":true},{"text":"chasse au carnotaure réussie","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2
function mg:terra/mis_clear
title @s title {"text":"✔ Carnotaure abattu","color":"gold","bold":true}
title @s subtitle {"text":"+400 ₵","color":"green"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.7 1
