# @s devient 🏹 Éclaireur
execute if score @s mg.trcl matches 2 run return run tellraw @s {"text":"Tu es déjà 🏹 Éclaireur.","color":"gray"}
scoreboard players set @s mg.trcl 2
scoreboard players set @s mg.trcd 0
function mg:terra/rpg/stats
function mg:terra/kit
title @s times 5 50 15
title @s title {"text":"🏹 ÉCLAIREUR","color":"green","bold":true}
title @s subtitle {"text":"Agile : +15 % de vitesse, sauts plus hauts, chutes amorties, +2 dégâts en mêlée.","color":"gray"}
tellraw @s [{"text":"🎖 Classe : ","color":"gold"},{"text":"🏹 Éclaireur","color":"green","bold":true},{"text":" — 💨 Sprint du chasseur : vitesse et saut 6 s. Recharge 15 s.","color":"gray"}]
execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1
