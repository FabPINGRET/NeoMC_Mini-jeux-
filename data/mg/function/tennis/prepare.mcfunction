# 🎾 Tennis — préparation : courts remis à neuf, appariement au hasard, robot si joueur impair
function mg:tennis/build
kill @e[tag=mg.tent]
kill @e[type=minecraft:item,x=-80,y=60,z=35375,dx=160,dy=30,dz=51]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 78
scoreboard players set $pz mg.st 35380
tag @a remove mg.tnk
tag @a remove mg.tnwin
tag @a remove mg.tnsrv
scoreboard players reset * mg.tnc
scoreboard players reset * mg.tns
scoreboard players reset * mg.tngw
scoreboard players reset @a mg.tnt
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
scoreboard players set #tnm1 mg.st -1
scoreboard players set #tnm7 mg.st -7
scoreboard players set #tn2 mg.st 2
scoreboard players set #tn3 mg.st 3
scoreboard players set #tn4 mg.st 4
scoreboard players set #tn10 mg.st 10
scoreboard players set #tn40000 mg.st 40000
scoreboard players set #tng mg.st 16
scoreboard players set $tni mg.st 0
execute as @a[tag=mg.play,sort=random] run function mg:tennis/assign
scoreboard players operation $tncourts mg.st = $tni mg.st
scoreboard players add $tncourts mg.st 1
scoreboard players operation $tncourts mg.st /= #tn2 mg.st
execute if score $tncourts mg.st matches 0 run scoreboard players set $tncourts mg.st 1
summon minecraft:marker 0 64 35400 {Tags:["mg.tent","mg.npc","mg.tndir"]}
execute if score $tncourts mg.st matches 1.. run summon minecraft:marker -60.5 65 35400.5 {Tags:["mg.tent","mg.npc","mg.tncm","mg.tnnew"],data:{k:1,a:"0",b:"0",ga:0,gb:0}}
execute if score $tncourts mg.st matches 1.. run summon minecraft:text_display -60.5 71.5 35400.5 {Tags:["mg.tent","mg.npc","mg.tntd","mg.tnnew"],billboard:"center",background:1711276032,line_width:220,alignment:"center",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]},text:{"text":"🎾 Court 1","color":"gold","bold":true}}
scoreboard players set @e[tag=mg.tnnew] mg.tnc 1
tag @e[tag=mg.tnnew] remove mg.tnnew
execute if score $tncourts mg.st matches 2.. run summon minecraft:marker -20.5 65 35400.5 {Tags:["mg.tent","mg.npc","mg.tncm","mg.tnnew"],data:{k:2,a:"0",b:"0",ga:0,gb:0}}
execute if score $tncourts mg.st matches 2.. run summon minecraft:text_display -20.5 71.5 35400.5 {Tags:["mg.tent","mg.npc","mg.tntd","mg.tnnew"],billboard:"center",background:1711276032,line_width:220,alignment:"center",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]},text:{"text":"🎾 Court 2","color":"gold","bold":true}}
scoreboard players set @e[tag=mg.tnnew] mg.tnc 2
tag @e[tag=mg.tnnew] remove mg.tnnew
execute if score $tncourts mg.st matches 3.. run summon minecraft:marker 20.5 65 35400.5 {Tags:["mg.tent","mg.npc","mg.tncm","mg.tnnew"],data:{k:3,a:"0",b:"0",ga:0,gb:0}}
execute if score $tncourts mg.st matches 3.. run summon minecraft:text_display 20.5 71.5 35400.5 {Tags:["mg.tent","mg.npc","mg.tntd","mg.tnnew"],billboard:"center",background:1711276032,line_width:220,alignment:"center",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]},text:{"text":"🎾 Court 3","color":"gold","bold":true}}
scoreboard players set @e[tag=mg.tnnew] mg.tnc 3
tag @e[tag=mg.tnnew] remove mg.tnnew
execute if score $tncourts mg.st matches 4.. run summon minecraft:marker 60.5 65 35400.5 {Tags:["mg.tent","mg.npc","mg.tncm","mg.tnnew"],data:{k:4,a:"0",b:"0",ga:0,gb:0}}
execute if score $tncourts mg.st matches 4.. run summon minecraft:text_display 60.5 71.5 35400.5 {Tags:["mg.tent","mg.npc","mg.tntd","mg.tnnew"],billboard:"center",background:1711276032,line_width:220,alignment:"center",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]},text:{"text":"🎾 Court 4","color":"gold","bold":true}}
scoreboard players set @e[tag=mg.tnnew] mg.tnc 4
tag @e[tag=mg.tnnew] remove mg.tnnew
scoreboard players operation $tnq mg.st = $tni mg.st
scoreboard players operation $tnq mg.st %= #tn2 mg.st
execute if score $tnq mg.st matches 1 if score $tncourts mg.st matches 1 run summon minecraft:mannequin -60.5 65 35414.5 {Tags:["mg.tent","mg.npc","mg.tnrob","mg.tnnew"],NoGravity:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"🤖 Robot","color":"gold"},CustomNameVisible:1b,description:{"text":"Robot de tennis","color":"gray"},equipment:{mainhand:{id:"minecraft:warped_fungus_on_a_stick",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":16733525}}}}
execute if score $tnq mg.st matches 1 if score $tncourts mg.st matches 2 run summon minecraft:mannequin -20.5 65 35414.5 {Tags:["mg.tent","mg.npc","mg.tnrob","mg.tnnew"],NoGravity:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"🤖 Robot","color":"gold"},CustomNameVisible:1b,description:{"text":"Robot de tennis","color":"gray"},equipment:{mainhand:{id:"minecraft:warped_fungus_on_a_stick",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":16733525}}}}
execute if score $tnq mg.st matches 1 if score $tncourts mg.st matches 3 run summon minecraft:mannequin 20.5 65 35414.5 {Tags:["mg.tent","mg.npc","mg.tnrob","mg.tnnew"],NoGravity:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"🤖 Robot","color":"gold"},CustomNameVisible:1b,description:{"text":"Robot de tennis","color":"gray"},equipment:{mainhand:{id:"minecraft:warped_fungus_on_a_stick",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":16733525}}}}
execute if score $tnq mg.st matches 1 if score $tncourts mg.st matches 4 run summon minecraft:mannequin 60.5 65 35414.5 {Tags:["mg.tent","mg.npc","mg.tnrob","mg.tnnew"],NoGravity:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,CustomName:{"text":"🤖 Robot","color":"gold"},CustomNameVisible:1b,description:{"text":"Robot de tennis","color":"gray"},equipment:{mainhand:{id:"minecraft:warped_fungus_on_a_stick",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":16733525}}}}
execute as @e[type=minecraft:mannequin,tag=mg.tnnew] run scoreboard players operation @s mg.tnc = $tncourts mg.st
scoreboard players set @e[type=minecraft:mannequin,tag=mg.tnnew] mg.tns 2
scoreboard players set @e[type=minecraft:mannequin,tag=mg.tnnew] mg.tnt 0
tag @e[tag=mg.tnnew] remove mg.tnnew
execute as @a[tag=mg.play] run function mg:tennis/kit
scoreboard players set $tntm mg.st 0
execute as @e[type=minecraft:marker,tag=mg.tncm] run function mg:tennis/court_init
