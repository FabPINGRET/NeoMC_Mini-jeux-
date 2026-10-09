# Une liasse de billets ici, montant $gcv (score mg.gpc de l'objet)
execute if score $rp mg.st matches 1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.gcash","mg.gcnew","mg.gbill"],item:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"mg:cash"}},teleport_duration:1,billboard:"vertical",Glowing:1b,glow_color_override:5635925,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.9f,0.9f,0.9f]}}
execute unless score $rp mg.st matches 1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.gcash","mg.gcnew"],item:{id:"minecraft:emerald_block",count:1},teleport_duration:1,Glowing:1b,glow_color_override:5635925,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.45f,0.6f]}}
scoreboard players operation @e[type=minecraft:item_display,tag=mg.gcnew] mg.gpc = $gcv mg.st
tag @e[tag=mg.gcnew] remove mg.gcnew
particle minecraft:happy_villager ~ ~0.3 ~ 0.4 0.4 0.4 0 10
