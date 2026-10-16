# 🎃 La sorcière donne un ragoût mystère (@s = joueur) ; appelé par lobby/theme/npc_use
execute if score @s mg.thc matches 1.. run return run title @s actionbar [{"text":"🎃 Reviens dans ","color":"gold"},{"score":{"name":"@s","objective":"mg.thc"},"color":"yellow"},{"text":" s","color":"gold"}]
execute store result score $thg mg.st run clear @s *[minecraft:custom_data~{mg_thg:1b}] 0
execute if score $thg mg.st matches 2.. run return run title @s actionbar {"text":"🎃 Utilise d'abord ton cadeau !","color":"gold"}
give @s minecraft:suspicious_stew[minecraft:custom_data={mg_thg:1b,mg_thst:1b},minecraft:custom_name={"text":"Ragoût mystère","color":"gold","italic":false},minecraft:lore=[{"text":"Une sorcière y a jeté un peu de tout…","color":"gray","italic":false},{"text":"Effet : surprise !","color":"dark_purple","italic":false}],minecraft:food={nutrition:0,saturation:0f,can_always_eat:true},!minecraft:use_remainder,minecraft:suspicious_stew_effects=[]]
scoreboard players set @s mg.thc 30
execute at @s run playsound minecraft:entity.witch.celebrate neutral @a[distance=..16] ~ ~ ~ 1 1
execute at @e[type=minecraft:interaction,tag=mg.thnpci,limit=1] run particle minecraft:witch ~ ~1 ~ 0.3 0.5 0.3 0.05 15 normal
title @s actionbar {"text":"🎃 Hihihi… un ragoût mystère !","color":"gold"}
