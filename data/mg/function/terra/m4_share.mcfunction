# @s chassait aussi le carnotaure : une part de la prime
scoreboard players add @s mg.tvc 150
scoreboard players set @s mg.tval 40
title @s actionbar [{"text":"+150 ₵ ","color":"gold","bold":true},{"text":"part de la chasse au carnotaure","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2
function mg:terra/mis_clear
