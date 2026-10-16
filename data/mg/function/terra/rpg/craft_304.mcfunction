# @s demande « 🛡 Armure d'écailles » à la forge
execute if score @s mg.trar matches 3.. run return run tellraw @s {"text":"⚒ « Tu as déjà ça, ou mieux ! »","color":"yellow"}
execute unless score @s mg.trec matches 3.. run return run tellraw @s {"text":"⚒ « Il me manque des écailles de spinosaure : il en faut 3. »","color":"red"}
execute unless score @s mg.trai matches 4.. run return run tellraw @s {"text":"⚒ « Il me manque des ailes de ptéranodon : il en faut 4. »","color":"red"}
execute unless score @s mg.tvc matches 400.. run return run tellraw @s {"text":"⚒ « Ça coûte 400 ₵ : reviens avec les crédits. »","color":"red"}
scoreboard players remove @s mg.trec 3
scoreboard players remove @s mg.trai 4
scoreboard players remove @s mg.tvc 400
scoreboard players set @s mg.trar 3
function mg:terra/rpg/kit
title @s times 5 50 15
title @s title {"text":"🛡 Armure d'écailles","color":"gold","bold":true}
title @s subtitle {"text":"forgé par Jo","color":"gray"}
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
