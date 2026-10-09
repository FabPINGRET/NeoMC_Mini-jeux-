# @s démarre : 🏁 Contre-la-montre
scoreboard players set @s mg.gmt 3
scoreboard players set @s mg.gms 1
scoreboard players set @s mg.gmtime 1500
scoreboard players operation $gb mg.st = @s mg.bid
execute as @e[type=minecraft:marker,tag=mg.gix,distance=40..80,sort=random,limit=1] at @s run summon minecraft:item_display ~ ~1.2 ~ {Tags:["mg.gta","mg.gmnew","mg.gmcp"],item:{id:"minecraft:yellow_stained_glass",count:1},billboard:"vertical",Glowing:1b,glow_color_override:16766720,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
title @s subtitle {"text":"Point de contrôle 1 / 5 : fonce !","color":"yellow"}
tag @e[tag=mg.gmnew] add mg.gmo
scoreboard players operation @e[tag=mg.gmnew] mg.bid = $gb mg.st
tag @e[tag=mg.gmnew] remove mg.gmnew
title @s times 5 40 10
title @s title {"text":"🏁 CONTRE-LA-MONTRE","color":"gold","bold":true}
playsound minecraft:block.note_block.chime player @s ~ ~ ~ 1 1.2
scoreboard players set @s mg.gtl 50
