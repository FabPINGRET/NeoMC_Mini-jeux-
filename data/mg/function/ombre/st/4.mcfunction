# Entités permanentes de la région n (retirées puis reposées)
kill @e[tag=mg.ols,x=-80,y=-64,z=-240,dx=159,dy=400,dz=159]
summon minecraft:villager 0.5 75 -130.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:weaponsmith",level:5,type:"minecraft:snow"},Offers:{Recipes:[]},CustomName:{"text":"🪓 Jarl Bjorn","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction 0.5 75 -130.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 15
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 0.5 77.35 -130.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -5.5 75 -111.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:leatherworker",level:5,type:"minecraft:snow"},Offers:{Recipes:[]},CustomName:{"text":"🧵 Sigrun, fourreuse","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction -5.5 75 -111.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 16
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -5.5 77.35 -111.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 3.5 75 -113.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 3.5 77.5 -113.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Hrafnheim","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:item_display -14.5 75.4 -121.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 32.5 105.4 -216.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock -57 83 -170 minecraft:chest[facing=south]
setblock -56 83 -170 minecraft:spruce_fence
setblock -56 84 -170 minecraft:spruce_fence
setblock -56 85 -170 minecraft:red_wool
setblock 32 96 -100 minecraft:chest[facing=south]
setblock 33 96 -100 minecraft:spruce_fence
setblock 33 97 -100 minecraft:spruce_fence
setblock 33 98 -100 minecraft:red_wool
setblock -13 89 -171 minecraft:chest[facing=south]
setblock -12 89 -171 minecraft:spruce_fence
setblock -12 90 -171 minecraft:spruce_fence
setblock -12 91 -171 minecraft:red_wool
summon minecraft:marker 50.5 107 -124.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 60.5 110 -105.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 9.5 86 -158.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 33.5 84 -167.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -44.5 106 -96.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -57.5 95 -219.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 34.5 83 -108.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -9.5 94 -199.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -32.5 105 -218.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 26.5 96 -150.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 63.5 82 -176.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -60.5 89 -94.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -27.5 110 -190.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -3.5 84 -184.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -13.5 90 -151.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -12.5 88 -165.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 57.5 86 -138.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -48.5 92 -159.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -30.5 98 -171.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -18.5 104 -215.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -31.5 105 -145.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 65.5 97 -147.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -57.5 82 -173.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 33.5 90 -123.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -34.5 105 -105.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -0.5 76 -148.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 63.5 86 -161.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 53.5 108 -150.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -52.5 99 -145.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -65.5 100 -208.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -27.5 105 -206.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 37.5 113 -141.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -47.5 71 -115.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -64.5 88 -159.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 64.5 108 -121.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -62.5 103 -135.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 64.5 98 -202.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -62.5 85 -110.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -64.5 85 -123.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 43.5 101 -98.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -40.5 106 -205.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 65.5 100 -94.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 3.5 82 -172.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 64.5 109 -222.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker -5.5 94 -225.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
summon minecraft:marker 44.5 92 -159.5 {Tags:["mg.ol","mg.ols","mg.olsp_n"]}
