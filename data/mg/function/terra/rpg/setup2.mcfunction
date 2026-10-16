# Session : PNJ des quêtes secondaires, décor des trésors
function mg:terra/rpg/tc_deco
summon minecraft:villager -32.5 65 -124.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[0f,0f],VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"🌿 Bastien, ermite","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction -32.5 65 -124.5 {Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 5
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display -32.5 67.35 -124.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"❗ Quête secondaire\n","color":"yellow","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -144.5 81 59.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[0f,0f],VillagerData:{profession:"minecraft:toolsmith",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"⛏ Inès, prospectrice","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction -144.5 81 59.5 {Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 7
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display -144.5 83.35 59.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"❗ Quête secondaire\n","color":"yellow","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:villager -28.5 69 119.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[0f,0f],VillagerData:{profession:"minecraft:mason",level:5,type:"minecraft:swamp"},Offers:{Recipes:[]},CustomName:{"text":"🌋 Arno, vulcanologue","color":"yellow"},CustomNameVisible:1b}
summon minecraft:interaction -28.5 69 119.5 {Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}
scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid 8
tag @e[tag=mg.tvn] remove mg.tvn
summon minecraft:text_display -28.5 71.35 119.5 {Tags:["mg.tv"],billboard:"vertical",text:[{"text":"❗ Quête secondaire\n","color":"yellow","bold":true},{"text":"clic droit","color":"gray","bold":false}],background:1140850688,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
