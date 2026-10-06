# Parkour du lobby (généré) : départ x 19, avance vers +x
kill @e[type=minecraft:marker,tag=mg.pkm]
kill @e[type=minecraft:text_display,tag=mg.pkd]
fill 18 63 -1 20 63 1 minecraft:emerald_block
setblock 22 63 0 minecraft:light_blue_concrete
setblock 25 63 1 minecraft:cyan_concrete
setblock 28 63 1 minecraft:cyan_concrete
setblock 31 63 1 minecraft:cyan_concrete
setblock 34 63 2 minecraft:white_concrete
setblock 37 63 3 minecraft:light_blue_concrete
setblock 40 63 2 minecraft:white_concrete
setblock 46 63 3 minecraft:lime_concrete
setblock 49 64 3 minecraft:lime_concrete
setblock 52 64 5 minecraft:yellow_concrete
setblock 55 65 4 minecraft:green_concrete
setblock 58 65 2 minecraft:yellow_concrete
setblock 61 66 2 minecraft:yellow_concrete
setblock 64 66 2 minecraft:yellow_concrete
setblock 71 67 1 minecraft:orange_concrete
setblock 74 67 2 minecraft:red_concrete
setblock 77 67 1 minecraft:orange_concrete
setblock 80 67 1 minecraft:orange_concrete
setblock 83 67 -1 minecraft:red_concrete
setblock 86 67 -2 minecraft:orange_concrete
setblock 89 67 -3 minecraft:magenta_concrete
setblock 96 67 -4 minecraft:black_concrete
setblock 99 68 -5 minecraft:blue_concrete
setblock 102 69 -6 minecraft:purple_concrete
setblock 105 70 -5 minecraft:blue_concrete
setblock 108 71 -6 minecraft:purple_concrete
setblock 111 72 -6 minecraft:purple_concrete
setblock 114 73 -6 minecraft:purple_concrete
fill 42 63 0 44 63 2 minecraft:lapis_block
fill 66 67 0 68 67 2 minecraft:lapis_block
fill 92 67 -4 94 67 -2 minecraft:lapis_block
fill 116 74 -7 118 74 -5 minecraft:diamond_block
summon minecraft:marker 19.5 64 0.5 {Tags:["mg.pkc","mg.pks","mg.pkm","mg.pkn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 0
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 43.5 64 1.5 {Tags:["mg.pkc","mg.pkm","mg.pkn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 1
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 67.5 68 1.5 {Tags:["mg.pkc","mg.pkm","mg.pkn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 2
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 93.5 68 -3.5 {Tags:["mg.pkc","mg.pkm","mg.pkn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 3
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 117.5 75 -6.5 {Tags:["mg.pkf","mg.pkm","mg.pkn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 4
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:text_display 19.5 66.5 0.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"✦ PARKOUR ✦","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],scale:[3f,3f,3f],right_rotation:[0f,0f,0f,1f]}}
summon minecraft:text_display 19.5 65.6 0.5 {Tags:["mg.pkd","mg.pkboard"],billboard:"center",text:[{"text":"3 checkpoints — arrive au bloc diamant !","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],scale:[1f,1f,1f],right_rotation:[0f,0f,0f,1f]}}
summon minecraft:text_display 12.5 65.5 0.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"PARKOUR ➜","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f],right_rotation:[0f,0f,0f,1f]}}
summon minecraft:text_display 117.5 77.5 -6.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"★ ARRIVÉE ★","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],scale:[3f,3f,3f],right_rotation:[0f,0f,0f,1f]}}
