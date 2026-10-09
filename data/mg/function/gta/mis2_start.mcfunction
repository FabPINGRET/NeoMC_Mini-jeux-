# @s démarre : 🎯 Contrat
scoreboard players set @s mg.gmt 2
scoreboard players set @s mg.gms 1
scoreboard players set @s mg.gmtime 2400
scoreboard players operation $gb mg.st = @s mg.bid
execute as @e[type=minecraft:marker,tag=mg.gsw,distance=50..110,sort=random,limit=1] at @s run function mg:gta/mis2_vip
title @s subtitle {"text":"Élimine la cible marquée","color":"yellow"}
tag @e[tag=mg.gmnew] add mg.gmo
scoreboard players operation @e[tag=mg.gmnew] mg.bid = $gb mg.st
tag @e[tag=mg.gmnew] remove mg.gmnew
title @s times 5 40 10
title @s title {"text":"🎯 CONTRAT","color":"gold","bold":true}
playsound minecraft:block.note_block.chime player @s ~ ~ ~ 1 1.2
scoreboard players set @s mg.gtl 50
