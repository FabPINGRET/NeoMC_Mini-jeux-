# @s : clic sur nitro / klaxon
scoreboard players reset @s mg.gqs
execute unless predicate mg:in_vehicle run return run function mg:gta/horn
execute if score @s mg.gnit matches 1.. run return run function mg:gta/horn
scoreboard players set @s mg.gnit 300
execute on vehicle run effect give @s minecraft:speed 3 4 true
execute on vehicle at @s run particle minecraft:flame ^ ^0.4 ^-2 0.2 0.1 0.2 0.05 30 force
execute at @s run playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.7
title @s actionbar {"text":"🔥 NITRO !","color":"gold","bold":true}
scoreboard players set @s mg.gal 30
