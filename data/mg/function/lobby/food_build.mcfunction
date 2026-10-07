# Buffet gratuit du spawn (sud-est, pelouse libre) : construction + présentoirs
kill @e[tag=mg.foodd]

# Terrasse et comptoir
fill 24 63 17 29 63 21 minecraft:spruce_planks
fill 25 64 17 29 65 21 minecraft:air
setblock 24 63 19 minecraft:gold_block
fill 26 64 18 26 64 20 minecraft:barrel[facing=up]
setblock 26 65 18 minecraft:cake
setblock 26 65 20 minecraft:spruce_trapdoor[half=bottom,open=false]

# Arrière : feu, foin, tonneau
setblock 28 64 18 minecraft:hay_block
setblock 28 64 19 minecraft:campfire[lit=true]
setblock 28 64 21 minecraft:smoker[facing=west]
setblock 28 64 17 minecraft:barrel[facing=up]

# Poteaux et auvent rayé
fill 29 64 17 29 66 17 minecraft:spruce_fence
fill 29 64 21 29 66 21 minecraft:spruce_fence
fill 25 66 17 25 66 21 minecraft:spruce_fence
fill 24 67 16 29 67 18 minecraft:red_wool
fill 24 67 19 29 67 19 minecraft:white_wool
fill 24 67 20 29 67 22 minecraft:red_wool

# Présentoirs animés (mêmes tags d'animation que l'armurerie)
summon minecraft:item_display 25.5 65.4 19.5 {Tags:["mg.foodd","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:cooked_beef"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:item_display 26.5 66.0 19.5 {Tags:["mg.foodd","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:golden_carrot"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.0f,1.0f,1.0f]}}
summon minecraft:text_display 26.5 68.3 19.5 {Tags:["mg.foodd"],billboard:"center",background:0,text:[{"text":"🍖 Buffet gratuit","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.1f,1.1f,1.1f]}}
summon minecraft:text_display 24.5 65.6 19.5 {Tags:["mg.foodd"],billboard:"center",background:0,text:[{"text":"Monte sur le bloc d'or !","color":"yellow"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}
