# Entités du bunker (portes, achats, apparitions) — tag mg.zent
kill @e[tag=mg.zent]
summon minecraft:marker -12.5 81 35804.5 {Tags:["mg.zent","mg.zsp","mg.zr_a"]}
summon minecraft:marker 0.5 81 35813.5 {Tags:["mg.zent","mg.zsp","mg.zr_a"]}
summon minecraft:marker -12.5 81 35778.5 {Tags:["mg.zent","mg.zsp","mg.zr_b"]}
summon minecraft:marker 0.5 81 35765.5 {Tags:["mg.zent","mg.zsp","mg.zr_b"]}
summon minecraft:marker 35.5 81 35804.5 {Tags:["mg.zent","mg.zsp","mg.zr_c"]}
summon minecraft:marker 22.5 81 35813.5 {Tags:["mg.zent","mg.zsp","mg.zr_c"]}
summon minecraft:marker 35.5 81 35778.5 {Tags:["mg.zent","mg.zsp","mg.zr_d"]}
summon minecraft:marker 22.5 81 35765.5 {Tags:["mg.zent","mg.zsp","mg.zr_d"]}
summon minecraft:interaction 0.5 81 35789.5 {Tags:["mg.zent","mg.zbuy","mg.zb1","mg.zd1"],width:3.4f,height:3f,response:1b}
summon minecraft:text_display 0.5 84.3 35789.5 {Tags:["mg.zent","mg.zd1"],billboard:"center",text:[{"text":"🚪 Porte A → B","color":"gold","bold":true},{"text":"\nclic droit — 750 pts","color":"yellow"}]}
summon minecraft:interaction 11.5 81 35800.5 {Tags:["mg.zent","mg.zbuy","mg.zb2","mg.zd2"],width:3.4f,height:3f,response:1b}
summon minecraft:text_display 11.5 84.3 35800.5 {Tags:["mg.zent","mg.zd2"],billboard:"center",text:[{"text":"🚪 Porte A → C","color":"gold","bold":true},{"text":"\nclic droit — 750 pts","color":"yellow"}]}
summon minecraft:interaction 11.5 81 35778.5 {Tags:["mg.zent","mg.zbuy","mg.zb3","mg.zd3"],width:3.4f,height:3f,response:1b}
summon minecraft:text_display 11.5 84.3 35778.5 {Tags:["mg.zent","mg.zd3"],billboard:"center",text:[{"text":"🚪 Porte B → D","color":"gold","bold":true},{"text":"\nclic droit — 1000 pts","color":"yellow"}]}
summon minecraft:interaction 22.5 81 35789.5 {Tags:["mg.zent","mg.zbuy","mg.zb4","mg.zd4"],width:3.4f,height:3f,response:1b}
summon minecraft:text_display 22.5 84.3 35789.5 {Tags:["mg.zent","mg.zd4"],billboard:"center",text:[{"text":"🚪 Porte C → D","color":"gold","bold":true},{"text":"\nclic droit — 1000 pts","color":"yellow"}]}
summon minecraft:interaction -9.5 81 35806.5 {Tags:["mg.zent","mg.zbuy","mg.zb11"],width:1.3f,height:2.4f,response:1b}
summon minecraft:text_display -9.85 84 35806.5 {Tags:["mg.zent"],billboard:"center",text:[{"text":"🔫 Fusil M14","color":"aqua","bold":true},{"text":"\n500 pts","color":"yellow"}]}
execute if score $rp mg.st matches 1 run summon minecraft:item_display -10.45 82.4 35806.5 {Tags:["mg.zent"],Rotation:[90f,0f],item:{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{"minecraft:item_model":"mg:gun_rifle"}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
execute unless score $rp mg.st matches 1 run summon minecraft:item_display -10.45 82.4 35806.5 {Tags:["mg.zent"],Rotation:[90f,0f],item:{id:"minecraft:crossbow",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:interaction 10.5 81 35806.5 {Tags:["mg.zent","mg.zbuy","mg.zb12"],width:1.3f,height:2.4f,response:1b}
summon minecraft:text_display 9.950000000000001 84 35806.5 {Tags:["mg.zent"],billboard:"center",text:[{"text":"🔫 Fusil à pompe","color":"aqua","bold":true},{"text":"\n500 pts","color":"yellow"}]}
execute if score $rp mg.st matches 1 run summon minecraft:item_display 10.55 82.4 35806.5 {Tags:["mg.zent"],Rotation:[-90f,0f],item:{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{"minecraft:item_model":"mg:gun_shotgun"}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
execute unless score $rp mg.st matches 1 run summon minecraft:item_display 10.55 82.4 35806.5 {Tags:["mg.zent"],Rotation:[-90f,0f],item:{id:"minecraft:crossbow",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:interaction -9.5 81 35784.5 {Tags:["mg.zent","mg.zbuy","mg.zb13"],width:1.3f,height:2.4f,response:1b}
summon minecraft:text_display -9.85 84 35784.5 {Tags:["mg.zent"],billboard:"center",text:[{"text":"🔫 Mitraillette","color":"aqua","bold":true},{"text":"\n1000 pts","color":"yellow"}]}
execute if score $rp mg.st matches 1 run summon minecraft:item_display -10.45 82.4 35784.5 {Tags:["mg.zent"],Rotation:[90f,0f],item:{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{"minecraft:item_model":"mg:gun_smg"}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
execute unless score $rp mg.st matches 1 run summon minecraft:item_display -10.45 82.4 35784.5 {Tags:["mg.zent"],Rotation:[90f,0f],item:{id:"minecraft:crossbow",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:interaction 31.5 81 35806.5 {Tags:["mg.zent","mg.zbuy","mg.zb21"],width:1.3f,height:2.4f,response:1b}
summon minecraft:text_display 31.5 84.4 35806.5 {Tags:["mg.zent"],billboard:"center",text:[{"text":"❤ Juggernog","color":"red","bold":true},{"text":"\n2× plus de vie — 2500 pts","color":"yellow"}]}
summon minecraft:interaction 31.5 81 35785.5 {Tags:["mg.zent","mg.zbuy","mg.zb22"],width:1.3f,height:2.4f,response:1b}
summon minecraft:text_display 31.5 84.4 35785.5 {Tags:["mg.zent"],billboard:"center",text:[{"text":"⚡ Speed Cola","color":"green","bold":true},{"text":"\nrecharge 2× plus vite — 3000 pts","color":"yellow"}]}
summon minecraft:interaction 22.5 81 35773.5 {Tags:["mg.zent","mg.zbuy","mg.zb20"],width:1.6f,height:1.6f,response:1b}
summon minecraft:text_display 22.5 83.4 35773.5 {Tags:["mg.zent"],billboard:"center",text:[{"text":"❓ Boîte mystère","color":"light_purple","bold":true},{"text":"\narme au hasard — 950 pts","color":"yellow"}]}
tag @e[tag=mg.zr_a] add mg.zon
