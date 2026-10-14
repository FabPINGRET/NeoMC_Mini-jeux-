tag @s add mg.tvout
scoreboard players set @s mg.tval 40
title @s actionbar {"text":"🌿 Tu quittes le périmètre : prudence, colon !","color":"gold"}
execute at @s run playsound minecraft:block.bell.use player @s ~ ~ ~ 0.5 0.8
