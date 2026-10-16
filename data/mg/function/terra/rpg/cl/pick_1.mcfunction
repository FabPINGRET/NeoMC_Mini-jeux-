# @s devient 🎖 Soldat
execute if score @s mg.trcl matches 1 run return run tellraw @s {"text":"Tu es déjà 🎖 Soldat.","color":"gray"}
scoreboard players set @s mg.trcl 1
scoreboard players set @s mg.trcd 0
function mg:terra/rpg/stats
function mg:terra/kit
title @s times 5 50 15
title @s title {"text":"🎖 SOLDAT","color":"red","bold":true}
title @s subtitle {"text":"Endurant : +3 cœurs, +2 armure, le fusil chauffe 30 % moins vite.","color":"gray"}
tellraw @s [{"text":"🎖 Classe : ","color":"gold"},{"text":"🎖 Soldat","color":"red","bold":true},{"text":" — 💥 Onde de choc : repousse et blesse les dinosaures proches (6 blocs), résistance 5 s. Recharge 15 s.","color":"gray"}]
execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1
