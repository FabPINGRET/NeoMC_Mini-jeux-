# Entités permanentes de la région ne (retirées puis reposées)
kill @e[tag=mg.ols,x=80,y=-64,z=-240,dx=159,dy=400,dz=159]
summon minecraft:villager 152.5 68 -115.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"✝ Sœur Maëlle","color":"dark_aqua"},CustomNameVisible:1b}
summon minecraft:interaction 152.5 68 -115.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 17
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 152.5 70.35 -115.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 147.5 68 -114.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:farmer",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"🌱 Odo, herboriste","color":"dark_green"},CustomNameVisible:1b}
summon minecraft:interaction 147.5 68 -114.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 18
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 147.5 70.35 -114.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 148.5 68 -119.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 148.5 70.5 -119.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Village des pilotis","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction 182.5 63 -202.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 260
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 182.5 65.9 -202.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"💀 Totem maudit\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 217.5 63 -215.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 261
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 217.5 65.9 -215.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"💀 Totem maudit\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 217.5 63 -173.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 262
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 217.5 65.9 -173.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"💀 Totem maudit\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 138.5 68.4 -111.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 204.5 65.4 -193.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock 221 63 -166 minecraft:chest[facing=south]
setblock 222 63 -166 minecraft:spruce_fence
setblock 222 64 -166 minecraft:spruce_fence
setblock 222 65 -166 minecraft:red_wool
setblock 172 64 -191 minecraft:chest[facing=south]
setblock 173 64 -191 minecraft:spruce_fence
setblock 173 65 -191 minecraft:spruce_fence
setblock 173 66 -191 minecraft:red_wool
setblock 102 63 -203 minecraft:chest[facing=south]
setblock 103 63 -203 minecraft:spruce_fence
setblock 103 64 -203 minecraft:spruce_fence
setblock 103 65 -203 minecraft:red_wool
summon minecraft:marker 150.5 63 -180.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 181.5 64 -132.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 205.5 63 -128.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 188.5 63 -161.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 101.5 63 -130.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 153.5 63 -163.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 97.5 64 -113.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 98.5 63 -152.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 142.5 63 -194.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 106.5 63 -141.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 134.5 63 -158.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 161.5 63 -211.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 179.5 64 -220.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 96.5 64 -95.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 173.5 64 -182.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 206.5 64 -113.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 192.5 64 -124.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 223.5 63 -167.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 185.5 63 -104.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 126.5 63 -221.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 172.5 64 -206.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 206.5 63 -154.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 158.5 63 -190.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 199.5 64 -100.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 182.5 63 -144.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 102.5 63 -207.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 138.5 63 -224.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 176.5 63 -163.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 162.5 63 -153.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 207.5 65 -194.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 143.5 63 -150.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 97.5 64 -168.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 116.5 63 -108.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 213.5 63 -101.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 167.5 63 -171.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 210.5 63 -140.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 120.5 63 -141.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 144.5 63 -210.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 112.5 65 -124.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 113.5 63 -173.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 109.5 63 -98.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 218.5 63 -152.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 100.5 63 -195.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 198.5 63 -145.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 113.5 63 -161.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
summon minecraft:marker 162.5 63 -224.5 {Tags:["mg.ol","mg.ols","mg.olsp_ne"]}
