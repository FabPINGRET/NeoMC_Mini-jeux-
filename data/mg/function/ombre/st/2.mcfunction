# Entités permanentes de la région w (retirées puis reposées)
kill @e[tag=mg.ols,x=-240,y=-64,z=-80,dx=159,dy=400,dz=159]
summon minecraft:villager -147.5 67 24.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:farmer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🌾 Tessa, maire de Brumecombe","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -147.5 67 24.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 11
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -147.5 69.35 24.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -127.5 67 12.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:shepherd",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🐑 Gaspard, berger","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -127.5 67 12.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 12
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -127.5 69.35 12.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -152.5 67 19.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display -152.5 69.5 19.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Brumecombe","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:item_display -171.5 68.4 -23.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:hay_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display -171.5 69.3 -23.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"🌾 Sac de grain","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -175.5 68.4 -58.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:hay_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display -175.5 69.3 -58.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"🌾 Sac de grain","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -228.5 71.4 -17.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:hay_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display -228.5 72.3 -17.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"🌾 Sac de grain","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -217.5 71.4 -38.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock -159 67 -9 minecraft:chest[facing=south]
setblock -158 67 -9 minecraft:spruce_fence
setblock -158 68 -9 minecraft:spruce_fence
setblock -158 69 -9 minecraft:red_wool
setblock -198 67 11 minecraft:chest[facing=south]
setblock -197 67 11 minecraft:spruce_fence
setblock -197 68 11 minecraft:spruce_fence
setblock -197 69 11 minecraft:red_wool
setblock -109 66 -6 minecraft:chest[facing=south]
setblock -108 66 -6 minecraft:spruce_fence
setblock -108 67 -6 minecraft:spruce_fence
setblock -108 68 -6 minecraft:red_wool
summon minecraft:marker -213.5 67 46.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -155.5 67 -24.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -106.5 70 36.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -192.5 68 63.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -111.5 68 24.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -143.5 68 57.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -194.5 67 10.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -141.5 67 -20.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -163.5 68 -51.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -104.5 66 7.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -209.5 69 10.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -178.5 68 54.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -98.5 68 25.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -154.5 67 -59.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -159.5 68 59.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -220.5 68 -5.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -147.5 65 -48.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -173.5 70 -29.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -221.5 67 27.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -190.5 67 -10.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -94.5 69 44.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -121.5 66 -15.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -98.5 70 -42.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -172.5 64 -7.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -196.5 67 32.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -217.5 65 62.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -99.5 68 -24.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -170.5 67 -63.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -96.5 70 58.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -206.5 66 -11.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -111.5 69 55.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -97.5 66 -65.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -109.5 66 -4.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -206.5 66 57.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -182.5 65 0.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -118.5 66 -28.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -141.5 65 -60.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -222.5 68 14.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -172.5 69 65.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -161.5 67 -13.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -132.5 65 -10.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -225.5 65 45.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -176.5 69 -49.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -135.5 64 -35.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -187.5 67 21.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
summon minecraft:marker -94.5 66 -0.5 {Tags:["mg.ol","mg.ols","mg.olsp_w"]}
