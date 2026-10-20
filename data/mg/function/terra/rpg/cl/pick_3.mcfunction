# @s devient 🔬 Scientifique
execute if score @s mg.trcl matches 3 run return run tellraw @s {"text":"Tu es déjà 🔬 Scientifique.","color":"gray"}
scoreboard players set @s mg.trcl 3
scoreboard players set @s mg.trcd 0
function mg:terra/rpg/stats
clear @s *[custom_data~{tv:14}]
function mg:terra/rpg/kit
function mg:terra/rpg/cl/bonus
title @s times 5 50 15
title @s title {"text":"🔬 SCIENTIFIQUE","color":"aqua","bold":true}
title @s subtitle {"text":"Soigneur : régénère lentement les colons proches, +50 % d'XP au scanner.","color":"gray"}
tellraw @s [{"text":"🎖 Classe : ","color":"gold"},{"text":"🔬 Scientifique","color":"aqua","bold":true},{"text":" — ✨ Fusée de détection : les dinosaures à 40 blocs brillent 10 s, colons proches régénérés. Recharge 20 s.","color":"gray"}]
execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1
