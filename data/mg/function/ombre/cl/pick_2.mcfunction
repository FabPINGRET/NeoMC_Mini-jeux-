# @s devient 🏹 Rôdeur
execute if score @s mg.olcl matches 2 run return run tellraw @s {"text":"Tu suis déjà cette voie.","color":"gray"}
scoreboard players set @s mg.olcl 2
scoreboard players set @s mg.olc1 0
scoreboard players set @s mg.olc2 0
scoreboard players set @s mg.olc3 0
scoreboard players set @s mg.olc4 0
function mg:ombre/stats
function mg:ombre/kit
title @s times 5 50 15
title @s title {"text":"🏹 RÔDEUR","color":"green","bold":true}
title @s subtitle {"text":"Agile ","color":"gray"}
tellraw @s [{"text":"🎖 Classe : ","color":"gold"},{"text":"🏹 Rôdeur","color":"green","bold":true},{"text":". Agile : +12 % de vitesse, chutes amorties, arc puissant. Ses compétences visent de loin (Agilité).","color":"gray"}]
execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1
execute if score @s mg.olch matches 1 run function mg:ombre/q/adv
