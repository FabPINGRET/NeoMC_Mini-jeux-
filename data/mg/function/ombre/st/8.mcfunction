# Entités permanentes de la région s (retirées puis reposées)
kill @e[tag=mg.ols,x=-80,y=-64,z=80,dx=159,dy=400,dz=159]
summon minecraft:villager -1.5 67 108.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:mason",level:5,type:"minecraft:taiga"},Offers:{Recipes:[]},CustomName:{"text":"👑 Roi Thrain","color":"gray"},CustomNameVisible:1b}
summon minecraft:interaction -1.5 67 108.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 22
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -1.5 69.35 108.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 3.5 67 109.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 3.5 69.5 109.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Camp nain","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction -9.5 67 133.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 410
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -9.5 69.9 133.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -3.5 67 133.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 411
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -3.5 69.9 133.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 4.5 67 133.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 412
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 4.5 69.9 133.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 10.5 67 133.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 413
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 10.5 69.9 133.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 12.5 67.4 120.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 14.5 67.4 145.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock -55 116 142 minecraft:chest[facing=south]
setblock -54 116 142 minecraft:spruce_fence
setblock -54 117 142 minecraft:spruce_fence
setblock -54 118 142 minecraft:red_wool
setblock 30 123 187 minecraft:chest[facing=south]
setblock 31 123 187 minecraft:spruce_fence
setblock 31 124 187 minecraft:spruce_fence
setblock 31 125 187 minecraft:red_wool
setblock -15 119 183 minecraft:chest[facing=south]
setblock -14 119 183 minecraft:spruce_fence
setblock -14 120 183 minecraft:spruce_fence
setblock -14 121 183 minecraft:red_wool
execute unless data storage mg:ombre doors.kgate run fill -4 67 140 4 79 141 minecraft:deepslate_tiles
summon minecraft:interaction -11.5 67 180.5 {Tags:["mg.ol","mg.ols","mg.olpill"],width:1.4f,height:5.2f,response:1b}
setblock -11 71 180 minecraft:light_blue_stained_glass
summon minecraft:interaction 12.5 67 180.5 {Tags:["mg.ol","mg.ols","mg.olpill"],width:1.4f,height:5.2f,response:1b}
setblock 12 71 180 minecraft:light_blue_stained_glass
summon minecraft:interaction -11.5 67 198.5 {Tags:["mg.ol","mg.ols","mg.olpill"],width:1.4f,height:5.2f,response:1b}
setblock -11 71 198 minecraft:light_blue_stained_glass
summon minecraft:interaction 12.5 67 198.5 {Tags:["mg.ol","mg.ols","mg.olpill"],width:1.4f,height:5.2f,response:1b}
setblock 12 71 198 minecraft:light_blue_stained_glass
summon minecraft:marker -62.5 67 159.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 45.5 92 163.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -65.5 125 177.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -31.5 125 154.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -45.5 127 193.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 48.5 120 214.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 11.5 124 158.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 47.5 126 185.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 8.5 110 141.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -62.5 128 225.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -40.5 76 137.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 62.5 67 97.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 42.5 66 94.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 16.5 127 225.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 36.5 68 149.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -35.5 123 225.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -39.5 65 115.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 36.5 124 220.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 38.5 67 135.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 24.5 123 184.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 57.5 66 114.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -23.5 126 222.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 39.5 65 117.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 22.5 67 140.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -12.5 123 213.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 57.5 124 150.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -4.5 120 183.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -29.5 68 97.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 56.5 121 176.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -10.5 128 157.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 12.5 121 183.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -27.5 122 196.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -65.5 66 109.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -53.5 124 176.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -64.5 66 128.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -18.5 123 174.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 39.5 124 194.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -57.5 128 203.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -44.5 126 213.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -17.5 119 188.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -51.5 115 144.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 31.5 125 207.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 62.5 122 219.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker -10.5 120 200.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 12.5 125 171.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
summon minecraft:marker 61.5 66 131.5 {Tags:["mg.ol","mg.ols","mg.olsp_s"]}
