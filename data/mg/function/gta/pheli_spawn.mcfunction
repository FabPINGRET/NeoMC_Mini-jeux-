# Hélico de police (5 ★) : point d'ancrage + carrosserie, survole le joueur recherché le plus proche, projecteur et tireur
scoreboard players add $gvid mg.st 1
summon minecraft:marker ~ ~20 ~ {Tags:["mg.gta","mg.gphel","mg.gcop","mg.gswat","mg.gvn"]}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:white_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.9f,1.4f,-1.4f],scale:[1.8f,1.5f,2.8f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:blue_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.91f,1.9f,-1.41f],scale:[1.82f,0.3f,2.82f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:light_blue_stained_glass"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.8f,1.5f,1.4f],scale:[1.6f,1.25f,0.9f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:white_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.2f,2.1f,-5.2f],scale:[0.4f,0.4f,3.8f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:blue_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.06f,2.3f,-5.3f],scale:[0.12f,1.1f,0.6f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:gray_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-1.0f,0.75f,-1.3f],scale:[0.12f,0.12f,3.0f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:gray_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.88f,0.75f,-1.3f],scale:[0.12f,0.12f,3.0f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:red_stained_glass"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.5f,2.95f,-0.2f],scale:[0.4f,0.15f,0.4f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphb"],block_state:{Name:"minecraft:blue_stained_glass"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.1f,2.95f,-0.2f],scale:[0.4f,0.15f,0.4f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphr"],block_state:{Name:"minecraft:black_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-4.5f,3.3f,-0.15f],scale:[9f,0.08f,0.3f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.gta","mg.gvn","mg.gphr"],block_state:{Name:"minecraft:black_concrete"},teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.15f,3.3f,-4.5f],scale:[0.3f,0.08f,9f]}}
scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st
tag @e[tag=mg.gvn,type=minecraft:block_display] add mg.gphb
tag @e[tag=mg.gvn] remove mg.gvn
tellraw @a[tag=mg.gtw,scores={mg.gwl=5..}] {"text":"🚁 L'hélicoptère de police est sur toi !","color":"red","bold":true}
