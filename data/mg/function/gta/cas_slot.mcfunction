# Machine à sous : 73 % perdu, 20 % 🍒🍒 ×2, 6 % 🔔🔔🔔 ×5, 1 % 777 ×20 (la maison garde ~10 %). Tirage maintenant, rouleaux animés, paiement à la fin.
data modify storage mg:gta sym set value [{"text":"🍒","color":"red"},{"text":"🍋","color":"yellow"},{"text":"🔔","color":"gold"},{"text":"💎","color":"aqua"},{"text":"⭐","color":"yellow"},{"text":"7","color":"red","bold":true}]
execute store result score @s mg.gsr run random value 0..99
execute store result score @s mg.gs1 run random value 0..5
execute store result score @s mg.gs2 run random value 0..5
execute store result score @s mg.gs3 run random value 0..5
# perdu : jamais 🍒🍒 en tête ni trois pareils
execute if score @s mg.gsr matches ..72 if score @s mg.gs1 matches 0 if score @s mg.gs2 matches 0 run scoreboard players set @s mg.gs2 1
execute if score @s mg.gsr matches ..72 if score @s mg.gs1 = @s mg.gs2 if score @s mg.gs2 = @s mg.gs3 run function mg:gta/cas_slot_bump
execute if score @s mg.gsr matches 73..92 run scoreboard players set @s mg.gs1 0
execute if score @s mg.gsr matches 73..92 run scoreboard players set @s mg.gs2 0
execute if score @s mg.gsr matches 73..92 run scoreboard players remove @s mg.gs3 1
execute if score @s mg.gsr matches 73..92 if score @s mg.gs3 matches ..0 run scoreboard players set @s mg.gs3 1
execute if score @s mg.gsr matches 93..98 run scoreboard players set @s mg.gs1 2
execute if score @s mg.gsr matches 93..98 run scoreboard players set @s mg.gs2 2
execute if score @s mg.gsr matches 93..98 run scoreboard players set @s mg.gs3 2
execute if score @s mg.gsr matches 99 run scoreboard players set @s mg.gs1 5
execute if score @s mg.gsr matches 99 run scoreboard players set @s mg.gs2 5
execute if score @s mg.gsr matches 99 run scoreboard players set @s mg.gs3 5
scoreboard players operation @s mg.gsb = $gbet mg.st
scoreboard players set @s mg.gsa 0
tag @s add mg.gslot
title @s clear
title @s times 0 12 4
title @s subtitle {"text":"🎰 les rouleaux tournent…","color":"gray"}
playsound minecraft:block.piston.extend player @a ~ ~ ~ 0.8 1.6
particle minecraft:wax_on ~ ~1.5 ~ 0.4 0.4 0.4 0 12
