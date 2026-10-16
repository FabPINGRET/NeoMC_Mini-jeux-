# @s devient ⚙ Ingénieur
execute if score @s mg.trcl matches 4 run return run tellraw @s {"text":"Tu es déjà ⚙ Ingénieur.","color":"gray"}
scoreboard players set @s mg.trcl 4
scoreboard players set @s mg.trcd 0
function mg:terra/rpg/stats
function mg:terra/kit
title @s times 5 50 15
title @s title {"text":"⚙ INGÉNIEUR","color":"gold","bold":true}
title @s subtitle {"text":"Bricoleur : lance-filets et 3 filets offerts, +3 pièges, 8 pièges posés au plus.","color":"gray"}
tellraw @s [{"text":"🎖 Classe : ","color":"gold"},{"text":"⚙ Ingénieur","color":"gold","bold":true},{"text":" — 🔫 Tourelle : une tourelle automatique tire sur les prédateurs (16 blocs) pendant 20 s. Recharge 25 s.","color":"gray"}]
execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1
