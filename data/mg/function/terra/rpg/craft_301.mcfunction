# @s demande « 🗡 Lame d'ambre » à la forge
execute if score @s mg.trml matches 2.. run return run tellraw @s {"text":"⚒ « Tu as déjà ça, ou mieux ! »","color":"yellow"}
execute unless score @s mg.trgr matches 8.. run return run tellraw @s {"text":"⚒ « Il me manque des griffes : il en faut 8. »","color":"red"}
execute unless score @s mg.tvc matches 150.. run return run tellraw @s {"text":"⚒ « Ça coûte 150 ₵ : reviens avec les crédits. »","color":"red"}
scoreboard players remove @s mg.trgr 8
scoreboard players remove @s mg.tvc 150
scoreboard players set @s mg.trml 2
function mg:terra/rpg/kit
title @s times 5 50 15
title @s title {"text":"🗡 Lame d'ambre","color":"gold","bold":true}
title @s subtitle {"text":"forgé par Jo","color":"gray"}
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
