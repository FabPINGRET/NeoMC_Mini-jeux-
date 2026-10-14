# Caisse de matériel ici (propriétaire $own) : tonneau lumineux, faisceau, étiquette, marqueur
summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvcrate","mg.tvn"],block_state:{Name:"minecraft:barrel",Properties:{facing:"up"}},Glowing:1b,glow_color_override:16755200,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.45f,0f,-0.45f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvcrate","mg.tvn"],block_state:{Name:"minecraft:yellow_stained_glass"},brightness:{sky:15,block:15},view_range:4f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.1f,0.9f,-0.1f],scale:[0.2f,30f,0.2f]}}
summon minecraft:text_display ~ ~1.6 ~ {Tags:["mg.tv","mg.tvcrate","mg.tvn"],billboard:"center",text:{"text":"📦 Matériel","color":"yellow","bold":true},background:1140850688}
summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.tvcrate","mg.tvcrm","mg.tvn"]}
scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st
tag @e[tag=mg.tvn] remove mg.tvn
