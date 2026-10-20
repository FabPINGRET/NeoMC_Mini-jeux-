# Pose un pack ici (position = emplacement) ; un pack à moins de 2 blocs = nouvel essai dans 1 s
execute if entity @e[type=minecraft:item_display,tag=mg.tmhk,distance=..2] run return run scoreboard players set $tmhc mg.st 20
summon minecraft:item_display ~ ~0.6 ~ {Tags:["mg.tmhk"],billboard:"vertical",Glowing:1b,item:{id:"minecraft:golden_apple",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
