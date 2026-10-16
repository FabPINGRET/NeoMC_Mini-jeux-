# Session : PNJ du RPG, balises de voyage, modules de données, cellule, œufs d'ambre, points d'apparition, barres des boss
function mg:terra/rpg/consts
summon minecraft:villager 14.5 65 -14.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[90f,0f],VillagerData:{profession:"minecraft:cartographer",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"⚔ Commandante Varga","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction 14.5 65 -14.5 {Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 1
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display 14.5 67.35 -14.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 15.5 65 -7.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[0f,0f],VillagerData:{profession:"minecraft:librarian",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"🔬 Dr Ossei","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction 15.5 65 -7.5 {Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 2
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display 15.5 67.35 -7.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -11.5 65 7.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[180f,0f],VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"⚒ Jo, forgeronne","color":"red"},CustomNameVisible:1b}
summon minecraft:interaction -11.5 65 7.5 {Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 3
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display -11.5 67.35 7.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 131.5 71 3.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[90f,0f],VillagerData:{profession:"minecraft:leatherworker",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"🏹 Nyla, éclaireuse","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction 131.5 71 3.5 {Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 4
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display 131.5 73.35 3.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -4.5 65 12.5 {Tags:["mg.tv","mg.trbeacon"],width:1.2f,height:2.2f,response:1b}
summon minecraft:text_display -4.5 67.4 12.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🌀 Balise de voyage\n","color":"light_purple","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:interaction -29.5 65 -121.5 {Tags:["mg.tv","mg.trbeacon"],width:1.2f,height:2.2f,response:1b}
summon minecraft:text_display -29.5 67.4 -121.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🌀 Balise de voyage\n","color":"light_purple","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:interaction 128.5 71 6.5 {Tags:["mg.tv","mg.trbeacon"],width:1.2f,height:2.2f,response:1b}
summon minecraft:text_display 128.5 73.4 6.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🌀 Balise de voyage\n","color":"light_purple","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:interaction -141.5 81 62.5 {Tags:["mg.tv","mg.trbeacon"],width:1.2f,height:2.2f,response:1b}
summon minecraft:text_display -141.5 83.4 62.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🌀 Balise de voyage\n","color":"light_purple","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:interaction -25.5 69 122.5 {Tags:["mg.tv","mg.trbeacon"],width:1.2f,height:2.2f,response:1b}
summon minecraft:text_display -25.5 71.4 122.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🌀 Balise de voyage\n","color":"light_purple","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:marker -66.5 64 -164.5 {Tags:["mg.tv","mg.trmod","mg.tvn"]}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 1
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -66.5 64.6 -164.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:recovery_compass",count:1},Glowing:1b,glow_color_override:5636095,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:text_display -66.5 65.3 -164.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"💾 Module de données","color":"aqua","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:marker -45.5 66 -156.5 {Tags:["mg.tv","mg.trmod","mg.tvn"]}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 2
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -45.5 66.6 -156.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:recovery_compass",count:1},Glowing:1b,glow_color_override:5636095,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:text_display -45.5 67.3 -156.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"💾 Module de données","color":"aqua","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:marker -56.5 64 -170.5 {Tags:["mg.tv","mg.trmod","mg.tvn"]}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 3
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -56.5 64.6 -170.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:recovery_compass",count:1},Glowing:1b,glow_color_override:5636095,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:text_display -56.5 65.3 -170.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"💾 Module de données","color":"aqua","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:marker -189.5 65 14.5 {Tags:["mg.tv","mg.trcell"]}
summon minecraft:text_display -189.5 66.6 14.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"🔋 Cellule d'énergie volée","color":"aqua","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -57.5 65.3 -23.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:sniffer_egg",count:1},Glowing:1b,glow_color_override:16755200,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 66.5 65.3 58.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:sniffer_egg",count:1},Glowing:1b,glow_color_override:16755200,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 53.5 76.3 -178.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:sniffer_egg",count:1},Glowing:1b,glow_color_override:16755200,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 176.5 72.3 67.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:sniffer_egg",count:1},Glowing:1b,glow_color_override:16755200,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display -149.5 65.3 -57.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:sniffer_egg",count:1},Glowing:1b,glow_color_override:16755200,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 68.5 69.3 168.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:sniffer_egg",count:1},Glowing:1b,glow_color_override:16755200,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:marker 50.5 64 -134.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker 59.5 64 -193.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker 17.5 64 -244.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker -17.5 64 -240.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker -73.5 64 -239.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker -38.5 64 -186.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker -59.5 64 -112.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker 82.5 64 -183.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker -51.5 65 -172.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker 80.5 64 -235.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker -65.5 64 -139.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker 75.5 64 -125.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker 57.5 65 -115.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker 64.5 64 -155.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_dilo"]}
summon minecraft:marker -38.5 65 -233.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker -22.5 65 -216.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker 34.5 64 -223.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker 44.5 64 -118.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker 65.5 64 -194.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker 62.5 65 -120.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker -63.5 64 -222.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker 11.5 64 -157.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker -72.5 64 -243.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker -55.5 64 -168.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker -82.5 64 -158.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker 74.5 64 -222.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_compy"]}
summon minecraft:marker 55.5 64 -204.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_raptor"]}
summon minecraft:marker 61.5 64 -140.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_raptor"]}
summon minecraft:marker -33.5 64 -220.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_raptor"]}
summon minecraft:marker 37.5 64 -228.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_raptor"]}
summon minecraft:marker -72.5 64 -161.5 {Tags:["mg.tv","mg.trsp","mg.trsp_n","mg.trsp_raptor"]}
summon minecraft:marker 235.5 68 -1.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 199.5 67 13.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 170.5 71 -79.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 233.5 67 -84.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 216.5 67 69.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 156.5 68 20.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 186.5 70 -47.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 153.5 68 -29.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_trike"]}
summon minecraft:marker 241.5 68 7.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_stego"]}
summon minecraft:marker 240.5 69 39.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_stego"]}
summon minecraft:marker 163.5 66 -31.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_stego"]}
summon minecraft:marker 222.5 69 -36.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_stego"]}
summon minecraft:marker 153.5 69 -69.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_stego"]}
summon minecraft:marker 157.5 67 31.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_stego"]}
summon minecraft:marker 242.5 67 78.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_stego"]}
summon minecraft:marker 141.5 68 -28.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ankylo"]}
summon minecraft:marker 169.5 66 10.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ankylo"]}
summon minecraft:marker 165.5 70 65.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ankylo"]}
summon minecraft:marker 128.5 68 79.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ankylo"]}
summon minecraft:marker 199.5 67 17.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ankylo"]}
summon minecraft:marker 199.5 69 -20.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 175.5 65 17.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 143.5 69 -64.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 208.5 68 61.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 120.5 66 -58.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 137.5 70 43.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 170.5 72 79.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 113.5 68 79.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 209.5 68 -72.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 227.5 69 -55.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_galli"]}
summon minecraft:marker 177.5 67 -0.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_brachio"]}
summon minecraft:marker 179.5 69 68.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_brachio"]}
summon minecraft:marker 227.5 68 66.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_brachio"]}
summon minecraft:marker 243.5 69 40.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_raptor"]}
summon minecraft:marker 221.5 67 -72.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_raptor"]}
summon minecraft:marker 118.5 68 71.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_raptor"]}
summon minecraft:marker 233.5 68 -32.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_raptor"]}
summon minecraft:marker -123.5 65 53.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -199.5 66 51.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -239.5 65 -36.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -150.5 85 -36.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -182.5 83 -83.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -231.5 85 63.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -156.5 85 -81.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -122.5 65 -47.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -225.5 83 -58.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -150.5 65 -59.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_raptor"]}
summon minecraft:marker -159.5 75 79.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -117.5 65 62.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -133.5 65 -28.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -223.5 85 -69.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -237.5 65 -33.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -192.5 85 -55.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -116.5 65 -78.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -218.5 65 51.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_ptera"]}
summon minecraft:marker -201.5 85 77.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_dilo"]}
summon minecraft:marker -222.5 85 -69.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_dilo"]}
summon minecraft:marker -211.5 85 -34.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_dilo"]}
summon minecraft:marker -123.5 66 1.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_dilo"]}
summon minecraft:marker -34.5 78 237.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_carno"]}
summon minecraft:marker -20.5 109 202.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_carno"]}
summon minecraft:marker -57.5 65 109.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_carno"]}
summon minecraft:marker 82.5 65 122.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_carno"]}
summon minecraft:marker 69.5 69 187.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_carno"]}
summon minecraft:marker -68.5 65 145.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_carno"]}
summon minecraft:marker -51.5 71 166.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_ankylo"]}
summon minecraft:marker -53.5 69 230.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_ankylo"]}
summon minecraft:marker 0.5 114 163.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_ankylo"]}
summon minecraft:marker 84.5 65 119.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_ankylo"]}
summon minecraft:marker 53.5 63 113.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_ankylo"]}
summon minecraft:marker 85.5 66 215.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_ankylo"]}
summon minecraft:marker 23.5 111 198.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_raptor"]}
summon minecraft:marker -76.5 66 217.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_raptor"]}
summon minecraft:marker 49.5 65 107.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_raptor"]}
summon minecraft:marker -51.5 71 143.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_raptor"]}
summon minecraft:marker -20.5 94 222.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_raptor"]}
summon minecraft:marker -84.5 64 113.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_raptor"]}
summon minecraft:marker -49.5 73 226.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_compy"]}
summon minecraft:marker 9.5 65 107.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_compy"]}
summon minecraft:marker -68.5 65 120.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_compy"]}
summon minecraft:marker -74.5 67 206.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_compy"]}
summon minecraft:marker 47.5 67 131.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_compy"]}
summon minecraft:marker 56.5 78 210.5 {Tags:["mg.tv","mg.trsp","mg.trsp_s","mg.trsp_compy"]}
summon minecraft:marker 222.5 91 58.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"]}
summon minecraft:marker 232.5 98 44.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"]}
summon minecraft:marker 214.5 105 72.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"]}
summon minecraft:marker 238.5 97 66.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"]}
summon minecraft:marker 206.5 104 52.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"]}
summon minecraft:marker 226.5 96 80.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"]}
summon minecraft:marker 244.5 103 50.5 {Tags:["mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"]}
summon minecraft:marker -184.5 65 4.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -193.5 65 9.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -194.5 65 18.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -201.5 65 12.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -211.5 65 13.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -207.5 65 4.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -211.5 65 -4.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -201.5 65 -3.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -194.5 65 -9.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
summon minecraft:marker -193.5 65 -0.5 {Tags:["mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"]}
bossbar add mg:trspino {"text":"🦖 Spinosaure, reine du marais","color":"dark_aqua"}
bossbar set mg:trspino color blue
bossbar set mg:trspino style notched_10
bossbar add mg:trrex {"text":"🦖 Le Roi Tyran","color":"dark_red"}
bossbar set mg:trrex color red
bossbar set mg:trrex style notched_20
bossbar add mg:trvarek {"text":"⚔ Lieutenant Varek","color":"dark_red"}
bossbar set mg:trvarek color red
bossbar set mg:trvarek style notched_10
bossbar set mg:trvarek max 140
scoreboard players set $trspa mg.st 0
scoreboard players set $trva mg.st 0
scoreboard players set $trra mg.st 0
scoreboard players set $trspc mg.st 0
scoreboard players set $trvc mg.st 0
scoreboard players set $trrc mg.st 0
function mg:terra/bio_try
function mg:terra/rpg/dg_setup
function mg:terra/rpg/setup2
