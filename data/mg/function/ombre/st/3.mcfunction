# Entités permanentes de la région nw (retirées puis reposées)
kill @e[tag=mg.ols,x=-240,y=-64,z=-240,dx=159,dy=400,dz=159]
summon minecraft:villager -159.5 101 -171.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:librarian",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"🌿 Reine Elyndra","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -159.5 101 -171.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 13
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -159.5 103.35 -171.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -167.5 69 -156.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:fletcher",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"🏹 Thalion, archer elfe","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -167.5 69 -156.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 14
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -167.5 71.35 -156.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -155.5 69 -155.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display -155.5 71.5 -155.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Aelindor","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:item_display -222.5 66.8 -142.5 {Tags:["mg.ol","mg.ols"],item:{id:"minecraft:cobweb",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}
summon minecraft:interaction -222.5 66 -142.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 120
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -222.5 68.9 -142.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🕸 Nid de cocons\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -232.5 77.8 -86.5 {Tags:["mg.ol","mg.ols"],item:{id:"minecraft:cobweb",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}
summon minecraft:interaction -232.5 77 -86.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 121
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -232.5 79.9 -86.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🕸 Nid de cocons\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -174.5 67.8 -115.5 {Tags:["mg.ol","mg.ols"],item:{id:"minecraft:cobweb",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}
summon minecraft:interaction -174.5 67 -115.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 122
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -174.5 69.9 -115.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🕸 Nid de cocons\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -153.5 101.4 -162.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display -109.5 70.4 -208.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock -216 71 -173 minecraft:chest[facing=south]
setblock -215 71 -173 minecraft:spruce_fence
setblock -215 72 -173 minecraft:spruce_fence
setblock -215 73 -173 minecraft:red_wool
setblock -115 68 -144 minecraft:chest[facing=south]
setblock -114 68 -144 minecraft:spruce_fence
setblock -114 69 -144 minecraft:spruce_fence
setblock -114 70 -144 minecraft:red_wool
setblock -95 69 -188 minecraft:chest[facing=south]
setblock -94 69 -188 minecraft:spruce_fence
setblock -94 70 -188 minecraft:spruce_fence
setblock -94 71 -188 minecraft:red_wool
summon minecraft:marker -130.5 67 -214.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -200.5 69 -184.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -126.5 68 -153.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -142.5 66 -205.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -149.5 69 -222.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -101.5 69 -138.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -176.5 66 -104.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -211.5 67 -124.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -162.5 64 -104.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -124.5 69 -97.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -218.5 70 -180.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -207.5 69 -163.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -174.5 67 -195.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -109.5 72 -177.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -105.5 69 -115.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -210.5 68 -147.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -144.5 64 -99.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -102.5 70 -156.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -117.5 69 -168.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -192.5 69 -155.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -198.5 70 -134.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -161.5 67 -129.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -98.5 70 -125.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -95.5 65 -195.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -94.5 72 -177.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -119.5 66 -141.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -124.5 65 -123.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -166.5 66 -218.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -193.5 68 -100.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -178.5 69 -221.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -224.5 68 -160.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -142.5 67 -129.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -175.5 66 -209.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -157.5 68 -201.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -187.5 69 -124.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -104.5 70 -103.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -219.5 72 -224.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -145.5 67 -117.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -113.5 64 -193.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -125.5 70 -179.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -168.5 67 -117.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -203.5 73 -224.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -125.5 69 -197.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -112.5 67 -225.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -191.5 72 -168.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
summon minecraft:marker -131.5 67 -135.5 {Tags:["mg.ol","mg.ols","mg.olsp_nw"]}
