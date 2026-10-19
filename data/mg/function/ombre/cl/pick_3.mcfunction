# @s devient 🔮 Mage
execute if score @s mg.olcl matches 3 run return run tellraw @s {"text":"Tu suis déjà cette voie.","color":"gray"}
scoreboard players set @s mg.olcl 3
scoreboard players set @s mg.olc1 0
scoreboard players set @s mg.olc2 0
scoreboard players set @s mg.olc3 0
scoreboard players set @s mg.olc4 0
function mg:ombre/stats
function mg:ombre/kit
title @s times 5 50 15
title @s title {"text":"🔮 MAGE","color":"light_purple","bold":true}
title @s subtitle {"text":"Érudit ","color":"gray"}
tellraw @s [{"text":"🎖 Classe : ","color":"gold"},{"text":"🔮 Mage","color":"light_purple","bold":true},{"text":". Érudit : +40 mana, mana plus rapide, bâton de sorts. Ses sorts font de gros dégâts (Esprit).","color":"gray"}]
execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1
execute if score @s mg.olch matches 1 run function mg:ombre/q/adv
