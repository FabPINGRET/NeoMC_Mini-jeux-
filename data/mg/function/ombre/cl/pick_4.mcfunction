# @s devient ✚ Clerc
execute if score @s mg.olcl matches 4 run return run tellraw @s {"text":"Tu suis déjà cette voie.","color":"gray"}
scoreboard players set @s mg.olcl 4
scoreboard players set @s mg.olc1 0
scoreboard players set @s mg.olc2 0
scoreboard players set @s mg.olc3 0
scoreboard players set @s mg.olc4 0
function mg:ombre/stats
function mg:ombre/kit
title @s times 5 50 15
title @s title {"text":"✚ CLERC","color":"yellow","bold":true}
title @s subtitle {"text":"Soigneur ","color":"gray"}
tellraw @s [{"text":"🎖 Classe : ","color":"gold"},{"text":"✚ Clerc","color":"yellow","bold":true},{"text":". Soigneur : +2 cœurs, +20 mana, soigne ses alliés et châtie les morts-vivants (Esprit).","color":"gray"}]
execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1
execute if score @s mg.olch matches 1 run function mg:ombre/q/adv
