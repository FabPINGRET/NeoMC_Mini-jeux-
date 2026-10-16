# Bonus au hasard dans cette case
execute store result score $yq3 mg.st run random value 1..3
execute if score $yq3 mg.st matches 1 run summon minecraft:item_display ~ ~0.5 ~ {Tags:["mg.yp","mg.yp1"],Glowing:1b,billboard:"vertical",item:{id:"minecraft:tnt",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
execute if score $yq3 mg.st matches 2 run summon minecraft:item_display ~ ~0.5 ~ {Tags:["mg.yp","mg.yp2"],Glowing:1b,billboard:"vertical",item:{id:"minecraft:blaze_powder",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
execute if score $yq3 mg.st matches 3 run summon minecraft:item_display ~ ~0.5 ~ {Tags:["mg.yp","mg.yp3"],Glowing:1b,billboard:"vertical",item:{id:"minecraft:sugar",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
