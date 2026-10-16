# @s demande « 🛡 Armure du Tyran » à la forge
execute if score @s mg.trar matches 4.. run return run tellraw @s {"text":"⚒ « Tu as déjà ça, ou mieux ! »","color":"yellow"}
execute unless score @s mg.trrx matches 1.. run return run tellraw @s {"text":"⚒ « Il me manque des croc du Roi : il en faut 1. »","color":"red"}
execute unless score @s mg.trdn matches 4.. run return run tellraw @s {"text":"⚒ « Il me manque des dents de carnotaure : il en faut 4. »","color":"red"}
execute unless score @s mg.tvc matches 800.. run return run tellraw @s {"text":"⚒ « Ça coûte 800 ₵ : reviens avec les crédits. »","color":"red"}
scoreboard players remove @s mg.trrx 1
scoreboard players remove @s mg.trdn 4
scoreboard players remove @s mg.tvc 800
scoreboard players set @s mg.trar 4
function mg:terra/rpg/kit
title @s times 5 50 15
title @s title {"text":"🛡 Armure du Tyran","color":"gold","bold":true}
title @s subtitle {"text":"forgé par Jo","color":"gray"}
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
