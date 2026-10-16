# @s a aidé à défendre un outpost
scoreboard players add @s mg.tvc 60
function mg:terra/rpg/xp {n:30}
scoreboard players set @s mg.tval 40
title @s actionbar [{"text":"+60 ₵ ","color":"aqua","bold":true},{"text":"renfort à l'outpost","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2
