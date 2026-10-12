# Campeur puni (@s = joueur resté 5 s dans un coin)
scoreboard players set @s mg.acn 0
tag @s remove mg.acz
execute at @s run particle minecraft:block{block_state:"minecraft:anvil"} ~ ~1 ~ 0.3 0.5 0.3 0 40
execute at @s run playsound minecraft:block.anvil.land master @a ~ ~ ~ 1 0.5
tellraw @a [{"text":"⚓ ","color":"gray"},{"selector":"@s","color":"red"},{"text":" a voulu camper dans un coin… l'enclume ne pardonne pas !","color":"gray"}]
function mg:core/eliminate
