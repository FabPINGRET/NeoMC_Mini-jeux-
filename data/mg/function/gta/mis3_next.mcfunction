# Point de contrôle passé
scoreboard players add @s mg.gms 1
playsound minecraft:block.note_block.pling player @s ~ ~ ~ 1 1.6
execute if score @s mg.gms matches 6.. run return run function mg:gta/mis_win
scoreboard players operation $gb mg.st = @s mg.bid
execute at @e[tag=mg.gmine,limit=1] as @e[type=minecraft:marker,tag=mg.gix,distance=40..80,sort=random,limit=1] at @s run summon minecraft:item_display ~ ~1.2 ~ {Tags:["mg.gta","mg.gmnew","mg.gmcp"],item:{id:"minecraft:yellow_stained_glass",count:1},billboard:"vertical",Glowing:1b,glow_color_override:16766720,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
kill @e[tag=mg.gmine]
tag @e[tag=mg.gmnew] add mg.gmo
scoreboard players operation @e[tag=mg.gmnew] mg.bid = $gb mg.st
tag @e[tag=mg.gmnew] remove mg.gmnew
title @s actionbar [{"text":"🏁 Point de contrôle ","color":"gold"},{"score":{"name":"@s","objective":"mg.gms"},"color":"yellow","bold":true},{"text":" / 5","color":"gold"}]
scoreboard players set @s mg.gal 30
