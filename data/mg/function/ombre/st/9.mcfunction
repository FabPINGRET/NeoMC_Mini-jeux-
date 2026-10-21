# Entités permanentes de la région sw (retirées puis reposées)
kill @e[tag=mg.ols,x=-240,y=-64,z=80,dx=159,dy=400,dz=159]
summon minecraft:villager -105.5 65 152.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🛡 Capitaine Aldric","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction -105.5 65 152.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 23
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -105.5 67.35 152.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -110.5 65 152.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display -110.5 67.5 152.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Camp rebelle","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction -153.5 67 162.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 470
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -153.5 69.9 162.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🜏 Pylône noir\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -153.5 67 194.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 471
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -153.5 69.9 194.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🜏 Pylône noir\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -175.5 67 200.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 472
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -175.5 69.9 200.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🜏 Pylône noir\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -98.5 65.4 160.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock -112 69 207 minecraft:chest[facing=south]
setblock -111 69 207 minecraft:spruce_fence
setblock -111 70 207 minecraft:spruce_fence
setblock -111 71 207 minecraft:red_wool
setblock -158 65 129 minecraft:chest[facing=south]
setblock -157 65 129 minecraft:spruce_fence
setblock -157 66 129 minecraft:spruce_fence
setblock -157 67 129 minecraft:red_wool
setblock -223 63 214 minecraft:chest[facing=south]
setblock -222 63 214 minecraft:spruce_fence
setblock -222 64 214 minecraft:spruce_fence
setblock -222 65 214 minecraft:red_wool
execute unless data storage mg:ombre doors.citadel run fill -158 67 176 -158 72 180 minecraft:iron_bars
fill -138 67 176 -138 74 180 minecraft:air
summon minecraft:marker -118.5 66 109.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -101.5 63 187.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -123.5 69 208.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -163.5 64 130.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -132.5 66 105.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -191.5 65 123.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -165.5 67 97.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -109.5 65 202.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -115.5 65 181.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -164.5 67 109.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -110.5 66 124.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -222.5 68 151.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -222.5 65 187.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -220.5 66 171.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -220.5 75 212.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -141.5 65 128.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -111.5 76 215.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -178.5 76 119.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -191.5 64 109.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -103.5 71 99.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -97.5 68 219.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -125.5 77 119.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -97.5 68 118.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -224.5 66 134.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -122.5 65 220.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -96.5 66 199.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -123.5 65 190.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -143.5 65 116.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -118.5 75 97.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -182.5 65 99.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -143.5 66 95.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -203.5 65 127.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -223.5 65 224.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -104.5 64 174.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -225.5 64 199.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -152.5 63 106.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -155.5 64 118.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
summon minecraft:marker -215.5 65 126.5 {Tags:["mg.ol","mg.ols","mg.olsp_sw"]}
