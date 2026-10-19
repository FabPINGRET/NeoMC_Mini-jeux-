# Entités permanentes de la région hub (retirées puis reposées)
kill @e[tag=mg.ols,x=-80,y=-64,z=-80,dx=159,dy=400,dz=159]
summon minecraft:villager -31.5 65 -31.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:librarian",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🔮 Archimagesse Liora","color":"light_purple"},CustomNameVisible:1b}
summon minecraft:interaction -31.5 65 -31.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 1
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -31.5 67.35 -31.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 35.5 65 -38.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🔮 Archimagesse Liora","color":"light_purple"},CustomNameVisible:1b}
summon minecraft:interaction 35.5 65 -38.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 2
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 35.5 67.35 -38.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -26.5 65 -9.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:weaponsmith",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"⚔ Orren, maître d'armes","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction -26.5 65 -9.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 3
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -26.5 67.35 -9.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 6.5 65 -29.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🛡 Capitaine Aldric","color":"aqua"},CustomNameVisible:1b}
summon minecraft:interaction 6.5 65 -29.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 4
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 6.5 67.35 -29.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 2.5 65 -43.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cartographer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"👑 Régente Isolde","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction 2.5 65 -43.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 5
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 2.5 67.35 -43.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 30.5 65 12.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:toolsmith",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"⚒ Bram, forgeron","color":"red"},CustomNameVisible:1b}
summon minecraft:interaction 30.5 65 12.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 6
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 30.5 67.35 12.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 24.5 65 -9.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:farmer",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🧺 Elsa, marchande","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction 24.5 65 -9.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 7
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 24.5 67.35 -9.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -37.5 65 28.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"⚗ Fenna, alchimiste","color":"dark_green"},CustomNameVisible:1b}
summon minecraft:interaction -37.5 65 28.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 8
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -37.5 67.35 28.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 33.5 65 32.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:leatherworker",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🐴 Joss, palefrenier","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction 33.5 65 32.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 9
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 33.5 67.35 32.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -31.5 65 22.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:butcher",level:5,type:"minecraft:plains"},Offers:{Recipes:[]},CustomName:{"text":"🍺 Marthe, aubergiste","color":"gold"},CustomNameVisible:1b}
summon minecraft:interaction -31.5 65 22.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 10
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display -31.5 67.35 22.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 6.5 65 6.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 6.5 67.5 6.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Havreclair","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display 0.5 76 0.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"HAVRECLAIR\n","color":"gold","bold":true},{"text":"Dernière cité libre d'Ombrelune","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[3.0f,3.0f,3.0f]}}
summon minecraft:horse 29.5 65 36.5 {Tags:["mg.ol","mg.ols"],Variant:516,PersistenceRequired:1b,Tame:1b}
summon minecraft:horse 33.5 65 36.5 {Tags:["mg.ol","mg.ols"],Variant:0,PersistenceRequired:1b,Tame:1b}
summon minecraft:horse 37.5 65 36.5 {Tags:["mg.ol","mg.ols"],Variant:516,PersistenceRequired:1b,Tame:1b}
summon minecraft:vindicator -1.5 65 -56.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[180f,0f]}
summon minecraft:vindicator 2.5 65 -56.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[180f,0f]}
summon minecraft:vindicator -1.5 65 57.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[0f,0f]}
summon minecraft:vindicator 2.5 65 57.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[0f,0f]}
summon minecraft:vindicator 57.5 65 -1.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[-90f,0f]}
summon minecraft:vindicator 57.5 65 2.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[-90f,0f]}
summon minecraft:vindicator -56.5 65 -1.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[90f,0f]}
summon minecraft:vindicator -56.5 65 2.5 {Tags:["mg.ol","mg.ols"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"Garde de Havreclair","color":"aqua"},equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[90f,0f]}
