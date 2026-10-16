# @s a rapporté les 6 œufs : un raptor apprivoisé
scoreboard players set @s mg.trmt 1
function mg:terra/rpg/xp {n:500}
item replace entity @s hotbar.3 with minecraft:warped_fungus_on_a_stick[custom_data={tv:11},item_model="minecraft:goat_horn",unbreakable={},custom_name={"text":"🦖 Sifflet de raptor","color":"green","italic":false,"bold":true},lore=[{"text":"Clic droit : ton raptor apprivoisé accourt","color":"gray","italic":false},{"text":"Monte dessus et galope (Z, espace = saut)","color":"gray","italic":false}]]
title @s title {"text":"🦖 RAPTOR APPRIVOISÉ","color":"green","bold":true}
title @s subtitle {"text":"Sifflet en case 4 : clic droit pour l'appeler","color":"gray"}
execute at @s run playsound minecraft:entity.fox.screech player @s ~ ~ ~ 1 1.4
