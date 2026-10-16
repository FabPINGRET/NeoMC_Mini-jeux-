# @s rapporte la caisse à la colonie
scoreboard players add @s mg.tvc 150
function mg:terra/rpg/xp {n:75}
scoreboard players set @s mg.tval 40
title @s actionbar [{"text":"+150 ₵ ","color":"gold","bold":true},{"text":"matériel livré à la colonie","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2
function mg:terra/mis_clear
title @s title {"text":"✔ Mission accomplie","color":"green","bold":true}
title @s subtitle {"text":"+150 ₵ : matériel livré","color":"gray"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
