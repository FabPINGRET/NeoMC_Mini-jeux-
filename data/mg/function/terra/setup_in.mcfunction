# Session (dans la dimension) : panneaux, présentoirs, tableau, marqueurs, herbivores, barres
# reste d'une session interrompue (/reload, arrêt du serveur) : tout est retiré avant
function mg:terra/clear
function mg:terra/shop_fix
execute as @a[tag=mg.tvw] run function mg:terra/mis_clear
function mg:terra/rules
summon minecraft:marker -11.5 65 16.5 {Tags:["mg.tv","mg.tvexit"]}
summon minecraft:text_display 0.5 73 0.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"TERRA NOVA\n","color":"green","bold":true},{"text":"Colonie humaine · il y a 85 millions d'années","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[3.0f,3.0f,3.0f]}}
summon minecraft:text_display -7.4 70.4 -17.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"🛒 DÉPÔT D'ÉQUIPEMENT","color":"aqua","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.3f,1.3f,1.3f]}}
summon minecraft:text_display 9.4 71.4 -17.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"🏛 QG DE COMMANDEMENT","color":"gold","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.3f,1.3f,1.3f]}}
summon minecraft:text_display 7.4 70.6 17.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"✚ INFIRMERIE\n","color":"red","bold":true},{"text":"reste à l'intérieur pour te soigner","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.3f,1.3f,1.3f]}}
summon minecraft:text_display -11.5 72.6 16.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🌀 Portail du temps\n","color":"light_purple","bold":true},{"text":"retour au spawn","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 0.5 75.6 -27.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"🚪 PORTE NORD","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 0.5 75.6 28.5 {Tags:["mg.tv"],billboard:"vertical",text:{"text":"🚪 PORTE SUD","color":"yellow","bold":true},background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 8.4 67.4 -22.5 {Tags:["mg.tv"],Rotation:[90f,0f],text:[{"text":"📋 MISSIONS\n","color":"gold","bold":true},{"text":"clic droit sur le tableau","color":"gray","bold":false}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:interaction 8.8 65 -22.5 {Tags:["mg.tv","mg.tvboard"],width:2.6f,height:3.2f,response:1b}
summon minecraft:villager -15.5 65 -23.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[0f,0f],VillagerData:{profession:"minecraft:weaponsmith",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"🛒 Intendant","color":"gold"},CustomNameVisible:1b}
summon minecraft:villager 20.5 65 17.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[90f,0f],VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},CustomName:{"text":"✚ Médecin","color":"red"},CustomNameVisible:1b}
summon minecraft:item_display -22.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:goat_horn",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -22.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"📢 Canon sonique\n","color":"aqua","bold":true},{"text":"150 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -22.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 1
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -20.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:crossbow",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -20.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🔫 Fusil à impulsions Mk2\n","color":"gold","bold":true},{"text":"220 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -20.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 2
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -18.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:fishing_rod",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -18.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🕸 Lance-filets (+3 filets)\n","color":"white","bold":true},{"text":"80 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -18.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 3
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -16.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:cobweb",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -16.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🕸 Filets ×3\n","color":"white","bold":true},{"text":"25 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -16.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 4
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -14.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:tripwire_hook",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -14.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"⚙ Pièges au sol ×3\n","color":"gray","bold":true},{"text":"45 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -14.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 5
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -12.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:golden_apple",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -12.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"✚ Trousses de soins ×2\n","color":"red","bold":true},{"text":"15 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -12.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 6
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -10.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:chainmail_chestplate",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -10.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🛡 Armure de patrouille\n","color":"dark_aqua","bold":true},{"text":"100 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -10.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 7
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:item_display -8.5 66.7 -21.5 {Tags:["mg.tv","mg.tvpdi"],item:{id:"minecraft:saddle",count:1},billboard:"fixed",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
summon minecraft:text_display -8.5 67.55 -21.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"🐴 Selle de brachiosaure\n","color":"yellow","bold":true},{"text":"40 ₵","color":"green","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:interaction -8.5 65 -21.5 {Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk 8
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display 62.5 69 -73.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"📡 Outpost Alpha\n","color":"aqua","bold":true},{"text":"générateur de la colonie","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display -71.5 74 6.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"📡 Outpost Bravo\n","color":"aqua","bold":true},{"text":"générateur de la colonie","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 30.5 70 72.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"📡 Outpost Charlie\n","color":"aqua","bold":true},{"text":"générateur de la colonie","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:marker -63.5 64 28.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -62.5 68 -38.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 81.5 65 29.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 56.5 64 69.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 6.5 66 -84.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 54.5 64 34.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -41.5 66 7.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker 44.5 65 15.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker 37.5 67 -65.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 84.5 66 66.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 54.5 64 6.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker -29.5 64 -50.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker -86.5 73 3.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 73.5 66 -0.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -38.5 65 54.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 74.5 65 -73.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 49.5 64 -32.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker -18.5 66 46.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker 58.5 68 -86.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 0.5 64 -57.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker -0.5 65 82.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 19.5 64 -63.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -55.5 67 5.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker -8.5 66 -78.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -86.5 66 26.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -17.5 65 -66.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -56.5 65 -58.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -86.5 66 -21.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -50.5 66 33.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker 1.5 66 45.5 {Tags:["mg.tv","mg.tvsp"]}
summon minecraft:marker -77.5 68 -66.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -53.5 65 59.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 75.5 66 -38.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -73.5 66 -26.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -87.5 69 48.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker -54.5 64 -75.5 {Tags:["mg.tv","mg.tvsp","mg.tvfar"]}
summon minecraft:marker 80.5 66 61.5 {Tags:["mg.tv","mg.tvhp"]}
summon minecraft:marker 61.5 65 -6.5 {Tags:["mg.tv","mg.tvhp"]}
summon minecraft:marker -74.5 65 71.5 {Tags:["mg.tv","mg.tvhp"]}
summon minecraft:marker 7.5 66 -65.5 {Tags:["mg.tv","mg.tvhp"]}
summon minecraft:marker -74.5 67 -66.5 {Tags:["mg.tv","mg.tvhp"]}
summon minecraft:marker -73.5 66 -24.5 {Tags:["mg.tv","mg.tvhp"]}
summon minecraft:marker 1.5 65 72.5 {Tags:["mg.tv","mg.tvhp"]}
summon minecraft:marker 83.5 65 -44.5 {Tags:["mg.tv","mg.tvhp"]}
execute positioned 80.5 66 61.5 run function mg:terra/dino/brachio
execute positioned 61.5 65 -6.5 run function mg:terra/dino/brachio
execute positioned -74.5 65 71.5 run function mg:terra/dino/brachio
execute positioned 7.5 66 -65.5 run function mg:terra/dino/pachy
execute positioned -74.5 67 -66.5 run function mg:terra/dino/pachy
execute positioned -73.5 66 -24.5 run function mg:terra/dino/pachy
execute positioned 1.5 65 72.5 run function mg:terra/dino/pachy
execute positioned 83.5 65 -44.5 run function mg:terra/dino/pachy
bossbar add mg:tvcarno {"text":"🦖 Carnotaure","color":"red"}
bossbar set mg:tvcarno color red
bossbar set mg:tvcarno style notched_10
bossbar set mg:tvcarno max 160
bossbar set mg:tvcarno players
bossbar add mg:tvo1 {"text":"🛡 Outpost Alpha","color":"aqua"}
bossbar set mg:tvo1 color blue
bossbar set mg:tvo1 style notched_10
bossbar set mg:tvo1 max 100
bossbar set mg:tvo1 players
scoreboard players set $tvo1 mg.st 0
bossbar add mg:tvo2 {"text":"🛡 Outpost Bravo","color":"aqua"}
bossbar set mg:tvo2 color blue
bossbar set mg:tvo2 style notched_10
bossbar set mg:tvo2 max 100
bossbar set mg:tvo2 players
scoreboard players set $tvo2 mg.st 0
bossbar add mg:tvo3 {"text":"🛡 Outpost Charlie","color":"aqua"}
bossbar set mg:tvo3 color blue
bossbar set mg:tvo3 style notched_10
bossbar set mg:tvo3 max 100
bossbar set mg:tvo3 players
scoreboard players set $tvo3 mg.st 0
scoreboard players set $tvcc mg.st 90
scoreboard players set $tvpk mg.st 3
scoreboard players set $tvsu mg.st 1
