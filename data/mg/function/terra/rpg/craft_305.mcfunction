# @s demande « ⚡ Lance-foudre » à la forge
execute if score @s mg.trwp matches 4.. run return run tellraw @s {"text":"⚒ « Tu as déjà ça, ou mieux ! »","color":"yellow"}
execute unless score @s mg.trwp matches 3.. run return run tellraw @s {"text":"⚒ « Il me faut ton fusil à plasma Mk3 comme base. »","color":"red"}
execute unless score @s mg.trrx matches 1.. run return run tellraw @s {"text":"⚒ « Il me manque des croc du Roi : il en faut 1. »","color":"red"}
execute unless score @s mg.tvc matches 600.. run return run tellraw @s {"text":"⚒ « Ça coûte 600 ₵ : reviens avec les crédits. »","color":"red"}
scoreboard players remove @s mg.trrx 1
scoreboard players remove @s mg.tvc 600
scoreboard players set @s mg.trwp 4
function mg:terra/rpg/kit
title @s times 5 50 15
title @s title {"text":"⚡ Lance-foudre","color":"gold","bold":true}
title @s subtitle {"text":"forgé par Jo","color":"gray"}
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
