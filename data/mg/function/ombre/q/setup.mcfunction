# Session : PNJ (villageois immobiles + zone de clic)
summon minecraft:villager -31.5 65 -31.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:librarian",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🔮 Archimagesse Liora","color":"light_purple"},CustomNameVisible:1b}
summon minecraft:interaction -31.5 65 -31.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 1
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -31.5 67.35 -31.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 35.5 65 -38.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🔮 Archimagesse Liora","color":"light_purple"},CustomNameVisible:1b}
summon minecraft:interaction 35.5 65 -38.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 2
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 35.5 67.35 -38.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -26.5 65 -9.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:weaponsmith",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"⚔ Orren, maître d'armes","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction -26.5 65 -9.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 3
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -26.5 67.35 -9.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 6.5 65 -29.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🛡 Capitaine Aldric","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction 6.5 65 -29.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 4
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 6.5 67.35 -29.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 2.5 65 -43.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cartographer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"👑 Régente Isolde","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction 2.5 65 -43.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 5
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 2.5 67.35 -43.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 30.5 65 12.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:toolsmith",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"⚒ Bram, forgeron","color":"red"},CustomNameVisible:1b}
summon minecraft:interaction 30.5 65 12.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 6
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 30.5 67.35 12.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 24.5 65 -9.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:farmer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🧺 Elsa, marchande","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction 24.5 65 -9.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 7
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 24.5 67.35 -9.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -37.5 65 28.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"⚗ Fenna, alchimiste","color":"dark_green"},CustomNameVisible:1b}
summon minecraft:interaction -37.5 65 28.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 8
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -37.5 67.35 28.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 33.5 65 32.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:leatherworker",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🐴 Joss, palefrenier","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction 33.5 65 32.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 9
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 33.5 67.35 32.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -31.5 65 22.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:butcher",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🍺 Marthe, aubergiste","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction -31.5 65 22.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 10
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -31.5 67.35 22.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -147.5 67 24.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:farmer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🌾 Tessa, maire de Brumecombe","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -147.5 67 24.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 11
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -147.5 69.35 24.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -127.5 67 12.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:shepherd",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🐑 Gaspard, berger","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -127.5 67 12.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 12
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -127.5 69.35 12.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -159.5 101 -171.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:librarian",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"🌿 Reine Elyndra","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -159.5 101 -171.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 13
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -159.5 103.35 -171.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -167.5 69 -156.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:fletcher",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"🏹 Thalion, archer elfe","color":"green"},CustomNameVisible:1b}
summon minecraft:interaction -167.5 69 -156.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 14
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -167.5 71.35 -156.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 0.5 75 -130.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:weaponsmith",level:5,type:"minecraft:snow"},Offers:{Recipes:[]},CustomName:{"text":"🪓 Jarl Bjorn","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction 0.5 75 -130.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 15
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 0.5 77.35 -130.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -5.5 75 -111.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:leatherworker",level:5,type:"minecraft:snow"},Offers:{Recipes:[]},CustomName:{"text":"🧵 Sigrun, fourreuse","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction -5.5 75 -111.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 16
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -5.5 77.35 -111.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 152.5 68 -115.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"✝ Sœur Maëlle","color":"dark_aqua"},CustomNameVisible:1b}
summon minecraft:interaction 152.5 68 -115.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 17
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 152.5 70.35 -115.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 147.5 68 -114.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:farmer",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"🌱 Odo, herboriste","color":"dark_green"},CustomNameVisible:1b}
summon minecraft:interaction 147.5 68 -114.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 18
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 147.5 70.35 -114.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 130.5 65 5.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cartographer",level:5,type:"minecraft:desert"},Offers:{Recipes:[]},CustomName:{"text":"🐪 Kassim, caravanier","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction 130.5 65 5.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 19
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 130.5 67.35 5.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 133.5 65 13.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:mason",level:5,type:"minecraft:desert"},Offers:{Recipes:[]},CustomName:{"text":"💍 Zahra, joaillière","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction 133.5 65 13.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 20
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 133.5 67.35 13.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 140.5 67 104.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:savanna"},Offers:{Recipes:[]},CustomName:{"text":"🔥 Durgan, forgeron nain","color":"red"},CustomNameVisible:1b}
summon minecraft:interaction 140.5 67 104.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 21
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 140.5 69.35 104.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -1.5 67 108.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:mason",level:5,type:"minecraft:taiga"},Offers:{Recipes:[]},CustomName:{"text":"👑 Roi Thrain","color":"gray"},CustomNameVisible:1b}
summon minecraft:interaction -1.5 67 108.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 22
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -1.5 69.35 108.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -105.5 65 152.5 {Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🛡 Capitaine Aldric","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction -105.5 65 152.5 {Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 23
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -105.5 67.35 152.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
# Session : pierres d'appel
summon minecraft:interaction 6.5 65 6.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 6.5 67.5 6.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Havreclair","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction -152.5 67 19.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display -152.5 69.5 19.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Brumecombe","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction -155.5 69 -155.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display -155.5 71.5 -155.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Aelindor","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction 3.5 75 -113.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 3.5 77.5 -113.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Hrafnheim","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction 148.5 68 -119.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 148.5 70.5 -119.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Village des pilotis","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction 134.5 65 0.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 134.5 67.5 0.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Oasis d'Azhar","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction 144.5 67 114.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 144.5 69.5 114.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Bastion des Braises","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction 3.5 67 109.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 3.5 69.5 109.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Camp nain","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:interaction -110.5 65 152.5 {Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display -110.5 67.5 152.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Camp rebelle","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# Session : objets de quête (sacs, cocons, scarabées, totems, runes, socles, pylônes)
summon minecraft:item_display -171.5 68.4 -23.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:hay_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display -171.5 69.3 -23.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"🌾 Sac de grain","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -175.5 68.4 -58.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:hay_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display -175.5 69.3 -58.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"🌾 Sac de grain","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -228.5 71.4 -17.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:hay_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display -228.5 72.3 -17.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"🌾 Sac de grain","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -222.5 66.8 -142.5 {Tags:["mg.ol"],item:{id:"minecraft:cobweb",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}
summon minecraft:interaction -222.5 66 -142.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 120
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -222.5 68.9 -142.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🕸 Nid de cocons\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -232.5 77.8 -86.5 {Tags:["mg.ol"],item:{id:"minecraft:cobweb",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}
summon minecraft:interaction -232.5 77 -86.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 121
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -232.5 79.9 -86.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🕸 Nid de cocons\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display -174.5 67.8 -115.5 {Tags:["mg.ol"],item:{id:"minecraft:cobweb",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}
summon minecraft:interaction -174.5 67 -115.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 122
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -174.5 69.9 -115.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🕸 Nid de cocons\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 182.5 63 -202.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 260
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 182.5 65.9 -202.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"💀 Totem maudit\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 217.5 63 -215.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 261
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 217.5 65.9 -215.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"💀 Totem maudit\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 217.5 63 -173.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 262
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 217.5 65.9 -173.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"💀 Totem maudit\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 162.5 66.4 52.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:gold_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display 162.5 67.3 52.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"🪲 Scarabée d'or","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 189.5 65.4 55.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:gold_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display 189.5 66.3 55.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"🪲 Scarabée d'or","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 171.5 68.4 34.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:gold_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display 171.5 69.3 34.5 {Tags:["mg.ol"],billboard:"vertical",text:{"text":"🪲 Scarabée d'or","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 194.5 65 -43.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 320
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 194.5 67.9 -43.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🪲 Socle\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 198.5 65 -43.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 321
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 198.5 67.9 -43.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🪲 Socle\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 202.5 65 -43.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 322
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 202.5 67.9 -43.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🪲 Socle\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -9.5 67 133.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 410
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -9.5 69.9 133.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -3.5 67 133.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 411
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -3.5 69.9 133.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 4.5 67 133.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 412
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 4.5 69.9 133.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 10.5 67 133.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 413
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 10.5 69.9 133.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"ᚱ Pierre runique\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -153.5 67 162.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 470
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -153.5 69.9 162.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🜏 Pylône noir\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -153.5 67 194.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 471
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -153.5 69.9 194.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🜏 Pylône noir\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction -175.5 67 200.5 {Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 472
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -175.5 69.9 200.5 {Tags:["mg.ol"],billboard:"vertical",text:[{"text":"🜏 Pylône noir\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
function mg:ombre/door/kgate_close
function mg:ombre/door/citadel_close
function mg:ombre/door/pyramid_close
# Session : pages du grimoire (livres posés)
summon minecraft:item_display -217.5 71.4 -38.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display -153.5 101.4 -162.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display -109.5 70.4 -208.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display -14.5 75.4 -121.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 32.5 105.4 -216.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 138.5 68.4 -111.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 204.5 65.4 -193.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 203.5 65.4 -41.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 160.5 65.4 50.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 134.5 67.4 102.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 170.5 117.4 188.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 12.5 67.4 120.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 14.5 67.4 145.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display -98.5 65.4 160.5 {Tags:["mg.ol","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
function mg:ombre/tc_deco
