execute if score @s mg.olhorse matches 1.. run return run tellraw @s {"text":"Tu as déjà un destrier : siffle-le (case 7) !","color":"yellow"}
execute unless score @s mg.olg matches 400.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 400
scoreboard players set @s mg.olhorse 1
item replace entity @s hotbar.6 with minecraft:warped_fungus_on_a_stick[custom_data={ol:5},item_model="minecraft:goat_horn",unbreakable={},custom_name={"text":"🐴 Sifflet du destrier","color":"yellow","italic":false,"bold":true},lore=[{"text":"Clic droit : ton cheval accourt et tu le montes","color":"gray","italic":false}],use_cooldown={seconds:2f,cooldown_group:"mg:olhorse"}]
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Destrier ","color":"green","bold":true},{"text":"(-400 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
