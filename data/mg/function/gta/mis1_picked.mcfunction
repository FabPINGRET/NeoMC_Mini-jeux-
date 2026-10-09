# Colis récupéré : livraison à 60..120 blocs
kill @e[tag=mg.gmine]
scoreboard players set @s mg.gms 2
scoreboard players operation $gb mg.st = @s mg.bid
execute as @e[type=minecraft:marker,tag=mg.gix,distance=60..120,sort=random,limit=1] at @s run summon minecraft:item_display ~ ~1.2 ~ {Tags:["mg.gta","mg.gmnew","mg.gmdl"],item:{id:"minecraft:barrel",count:1},billboard:"vertical",Glowing:1b,glow_color_override:16766720,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
tag @e[tag=mg.gmnew] add mg.gmo
scoreboard players operation @e[tag=mg.gmnew] mg.bid = $gb mg.st
tag @e[tag=mg.gmnew] remove mg.gmnew
title @s subtitle {"text":"📦 Colis récupéré : livre-le au faisceau doré !","color":"yellow"}
title @s title {"text":" "}
playsound minecraft:item.armor.equip_leather player @s ~ ~ ~ 1 1
