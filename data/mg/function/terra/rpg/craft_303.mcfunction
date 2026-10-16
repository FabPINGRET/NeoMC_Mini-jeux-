# @s demande « 🛡 Armure renforcée » à la forge
execute if score @s mg.trar matches 2.. run return run tellraw @s {"text":"⚒ « Tu as déjà ça, ou mieux ! »","color":"yellow"}
execute unless score @s mg.trgr matches 10.. run return run tellraw @s {"text":"⚒ « Il me manque des griffes : il en faut 10. »","color":"red"}
execute unless score @s mg.trdn matches 2.. run return run tellraw @s {"text":"⚒ « Il me manque des dents de carnotaure : il en faut 2. »","color":"red"}
execute unless score @s mg.tvc matches 250.. run return run tellraw @s {"text":"⚒ « Ça coûte 250 ₵ : reviens avec les crédits. »","color":"red"}
scoreboard players remove @s mg.trgr 10
scoreboard players remove @s mg.trdn 2
scoreboard players remove @s mg.tvc 250
scoreboard players set @s mg.trar 2
function mg:terra/rpg/kit
title @s times 5 50 15
title @s title {"text":"🛡 Armure renforcée","color":"gold","bold":true}
title @s subtitle {"text":"forgé par Jo","color":"gray"}
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
