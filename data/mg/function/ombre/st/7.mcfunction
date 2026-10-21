# Entités permanentes de la région se (retirées puis reposées)
kill @e[tag=mg.ols,x=80,y=-64,z=80,dx=159,dy=400,dz=159]
summon minecraft:villager 140.5 67 104.5 {Tags:["mg.ol","mg.ols","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,VillagerData:{profession:"minecraft:armorer",level:5,type:"minecraft:savanna"},Offers:{Recipes:[]},CustomName:{"text":"🔥 Durgan, forgeron nain","color":"red"},CustomNameVisible:1b}
summon minecraft:interaction 140.5 67 104.5 {Tags:["mg.ol","mg.ols","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid 21
tag @e[tag=mg.olnn] remove mg.olnn
summon minecraft:text_display 140.5 69.35 104.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:{"text":"💬 clic droit","color":"gray"},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:interaction 144.5 67 114.5 {Tags:["mg.ol","mg.ols","mg.olway"],width:1.4f,height:2.4f,response:1b}
summon minecraft:text_display 144.5 69.5 114.5 {Tags:["mg.ol","mg.ols"],billboard:"vertical",text:[{"text":"🌀 Pierre d'appel\n","color":"light_purple","bold":true},{"text":"Bastion des Braises","color":"yellow","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:item_display 134.5 67.4 102.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:item_display 170.5 117.4 188.5 {Tags:["mg.ol","mg.ols","mg.olspin"],item:{id:"minecraft:written_book",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
setblock 160 104 172 minecraft:chest[facing=south]
setblock 161 104 172 minecraft:spruce_fence
setblock 161 105 172 minecraft:spruce_fence
setblock 161 106 172 minecraft:red_wool
setblock 212 79 223 minecraft:chest[facing=south]
setblock 213 79 223 minecraft:spruce_fence
setblock 213 80 223 minecraft:spruce_fence
setblock 213 81 223 minecraft:red_wool
setblock 189 66 102 minecraft:chest[facing=south]
setblock 190 66 102 minecraft:spruce_fence
setblock 190 67 102 minecraft:spruce_fence
setblock 190 68 102 minecraft:red_wool
summon minecraft:marker 187.5 71 115.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 148.5 94 181.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 170.5 84 135.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 115.5 69 121.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 124.5 75 195.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 172.5 75 122.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 136.5 85 190.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 224.5 80 158.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 172.5 68 109.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 175.5 101 154.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 209.5 96 169.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 97.5 67 182.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 134.5 79 154.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 125.5 74 163.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 119.5 65 133.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 140.5 74 224.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 208.5 89 153.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 217.5 72 128.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 186.5 122 198.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 202.5 99 197.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 223.5 77 142.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 159.5 86 141.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 191.5 67 95.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 115.5 66 98.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 104.5 68 222.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 182.5 117 168.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 103.5 68 127.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 205.5 85 216.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 115.5 68 153.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 173.5 96 209.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 202.5 77 130.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 183.5 117 185.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 202.5 86 142.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 174.5 84 225.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 214.5 93 188.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 165.5 117 179.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 185.5 90 220.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 97.5 66 96.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 223.5 86 201.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 110.5 70 171.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 142.5 83 207.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 101.5 67 112.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 95.5 66 154.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 195.5 97 207.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 108.5 66 207.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
summon minecraft:marker 146.5 76 137.5 {Tags:["mg.ol","mg.ols","mg.olsp_se"]}
