# Entités permanentes de la région e (retirées puis reposées)
kill @e[tag=mg.ols,x=80,y=-64,z=-80,dx=159,dy=400,dz=159]
summon minecraft:villager 130.5 65 5.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:cartographer",level:5,type:"minecraft:desert"},Offers:{Recipes:[]},CustomName:{"text":"🐪 Kassim, caravanier","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction 130.5 65 5.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 19
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 130.5 67.35 5.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager 133.5 65 13.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:mason",level:5,type:"minecraft:desert"},Offers:{Recipes:[]},CustomName:{"text":"💍 Zahra, joaillière","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction 133.5 65 13.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 20
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 133.5 67.35 13.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 134.5 65 0.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 134.5 67.5 0.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Oasis d'Azhar","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:item_display 162.5 66.4 52.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:gold_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display 162.5 67.3 52.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"🪲 Scarabée d'or","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 189.5 65.4 55.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:gold_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display 189.5 66.3 55.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"🪲 Scarabée d'or","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 171.5 68.4 34.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:gold_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}
summon minecraft:text_display 171.5 69.3 34.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"🪲 Scarabée d'or","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 194.5 65 -43.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 320
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 194.5 67.9 -43.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🪲 Socle\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 198.5 65 -43.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 321
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 198.5 67.9 -43.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🪲 Socle\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 202.5 65 -43.5 {Tags:["mg.ol","mg.ols","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 322
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 202.5 67.9 -43.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🪲 Socle\n","color":"gold","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:item_display 203.5 65.4 -41.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 160.5 65.4 50.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock 107 68 -42 minecraft:chest[facing=south]
setblock 108 68 -42 minecraft:spruce_fence
setblock 108 69 -42 minecraft:spruce_fence
setblock 108 70 -42 minecraft:red_wool
setblock 163 66 57 minecraft:chest[facing=south]
setblock 164 66 57 minecraft:spruce_fence
setblock 164 67 57 minecraft:spruce_fence
setblock 164 68 57 minecraft:red_wool
setblock 99 68 10 minecraft:chest[facing=south]
setblock 100 68 10 minecraft:spruce_fence
setblock 100 69 10 minecraft:spruce_fence
setblock 100 70 10 minecraft:red_wool
fill 197 65 -39 199 67 -39 minecraft:chiseled_sandstone
summon minecraft:marker 118.5 66 -61.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 107.5 68 47.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 98.5 68 -62.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 106.5 68 60.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 101.5 68 22.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 167.5 66 53.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 147.5 66 -50.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 199.5 67 15.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 144.5 65 -34.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 173.5 68 36.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 162.5 68 -13.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 170.5 65 9.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 158.5 68 -43.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 154.5 66 -63.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 126.5 68 -48.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 98.5 66 -44.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 222.5 69 35.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 194.5 65 29.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 138.5 68 41.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 181.5 68 21.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 158.5 67 23.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 124.5 66 -24.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 96.5 69 36.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 129.5 67 53.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 207.5 68 -61.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 211.5 66 14.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 99.5 68 -27.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 215.5 68 50.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 102.5 66 -14.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 224.5 66 59.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 100.5 68 0.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 214.5 66 26.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 138.5 67 61.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 225.5 67 -61.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 157.5 66 60.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 150.5 67 44.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 136.5 67 -63.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 110.5 67 -48.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 119.5 66 40.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 172.5 67 65.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 132.5 66 -33.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 156.5 69 -0.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 223.5 69 10.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 159.5 69 -25.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 108.5 68 32.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
summon minecraft:marker 178.5 67 -61.5 {Tags:["mg.ol","mg.ols","mg.olsp_e"]}
