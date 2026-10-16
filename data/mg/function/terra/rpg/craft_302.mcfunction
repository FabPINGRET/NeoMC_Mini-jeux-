# @s demande « 🔫 Fusil à plasma Mk3 » à la forge
execute if score @s mg.trwp matches 3.. run return run tellraw @s {"text":"⚒ « Tu as déjà ça, ou mieux ! »","color":"yellow"}
execute unless score @s mg.trwp matches 2.. run return run tellraw @s {"text":"⚒ « Il me faut ton fusil Mk2 comme base : achète-le au dépôt. »","color":"red"}
execute unless score @s mg.trvn matches 6.. run return run tellraw @s {"text":"⚒ « Il me manque des glandes à venin : il en faut 6. »","color":"red"}
execute unless score @s mg.trec matches 2.. run return run tellraw @s {"text":"⚒ « Il me manque des écailles de spinosaure : il en faut 2. »","color":"red"}
execute unless score @s mg.tvc matches 350.. run return run tellraw @s {"text":"⚒ « Ça coûte 350 ₵ : reviens avec les crédits. »","color":"red"}
scoreboard players remove @s mg.trvn 6
scoreboard players remove @s mg.trec 2
scoreboard players remove @s mg.tvc 350
scoreboard players set @s mg.trwp 3
function mg:terra/rpg/kit
title @s times 5 50 15
title @s title {"text":"🔫 Fusil à plasma Mk3","color":"gold","bold":true}
title @s subtitle {"text":"forgé par Jo","color":"gray"}
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
