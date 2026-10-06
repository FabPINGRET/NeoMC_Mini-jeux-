# Plateau de la Mini Party (z 15000) : île, chemin, 32 cases, déco centrale
fill -24 62 14980 24 62 15020 minecraft:dirt
fill -24 63 14980 24 63 15020 minecraft:grass_block
fill -24 64 14980 24 72 15020 minecraft:air
fill -18 63 14986 18 63 14986 minecraft:smooth_stone
fill -18 63 15014 18 63 15014 minecraft:smooth_stone
fill -18 63 14986 -18 63 15014 minecraft:smooth_stone
fill 18 63 14986 18 63 15014 minecraft:smooth_stone
fill -19 63 14985 -17 63 14987 minecraft:gold_block
fill -15 63 14985 -13 63 14987 minecraft:blue_concrete
fill -11 63 14985 -9 63 14987 minecraft:blue_concrete
fill -7 63 14985 -5 63 14987 minecraft:red_concrete
fill -3 63 14985 -1 63 14987 minecraft:blue_concrete
fill 1 63 14985 3 63 14987 minecraft:lime_concrete
fill 5 63 14985 7 63 14987 minecraft:blue_concrete
fill 9 63 14985 11 63 14987 minecraft:blue_concrete
fill 13 63 14985 15 63 14987 minecraft:red_concrete
fill 17 63 14985 19 63 14987 minecraft:blue_concrete
fill 17 63 14989 19 63 14991 minecraft:lime_concrete
fill 17 63 14993 19 63 14995 minecraft:blue_concrete
fill 17 63 14997 19 63 14999 minecraft:blue_concrete
fill 17 63 15001 19 63 15003 minecraft:black_concrete
fill 17 63 15005 19 63 15007 minecraft:blue_concrete
fill 17 63 15009 19 63 15011 minecraft:red_concrete
fill 17 63 15013 19 63 15015 minecraft:blue_concrete
fill 13 63 15013 15 63 15015 minecraft:lime_concrete
fill 9 63 15013 11 63 15015 minecraft:blue_concrete
fill 5 63 15013 7 63 15015 minecraft:blue_concrete
fill 1 63 15013 3 63 15015 minecraft:red_concrete
fill -3 63 15013 -1 63 15015 minecraft:blue_concrete
fill -7 63 15013 -5 63 15015 minecraft:lime_concrete
fill -11 63 15013 -9 63 15015 minecraft:blue_concrete
fill -15 63 15013 -13 63 15015 minecraft:blue_concrete
fill -19 63 15013 -17 63 15015 minecraft:black_concrete
fill -19 63 15009 -17 63 15011 minecraft:blue_concrete
fill -19 63 15005 -17 63 15007 minecraft:red_concrete
fill -19 63 15001 -17 63 15003 minecraft:blue_concrete
fill -19 63 14997 -17 63 14999 minecraft:lime_concrete
fill -19 63 14993 -17 63 14995 minecraft:blue_concrete
fill -19 63 14989 -17 63 14991 minecraft:red_concrete
# Bassin et arbres au centre
fill -8 63 14996 8 63 15004 minecraft:water
fill -9 63 14995 9 63 14995 minecraft:sand
fill -9 63 15005 9 63 15005 minecraft:sand
fill -9 63 14995 -9 63 15005 minecraft:sand
fill 9 63 14995 9 63 15005 minecraft:sand
fill -14 66 14990 -10 67 14994 minecraft:oak_leaves[persistent=true]
fill -13 68 14991 -11 68 14993 minecraft:oak_leaves[persistent=true]
fill -12 64 14992 -12 67 14992 minecraft:oak_log
fill -14 66 15006 -10 67 15010 minecraft:oak_leaves[persistent=true]
fill -13 68 15007 -11 68 15009 minecraft:oak_leaves[persistent=true]
fill -12 64 15008 -12 67 15008 minecraft:oak_log
fill 10 66 14990 14 67 14994 minecraft:oak_leaves[persistent=true]
fill 11 68 14991 13 68 14993 minecraft:oak_leaves[persistent=true]
fill 12 64 14992 12 67 14992 minecraft:oak_log
fill 10 66 15006 14 67 15010 minecraft:oak_leaves[persistent=true]
fill 11 68 15007 13 68 15009 minecraft:oak_leaves[persistent=true]
fill 12 64 15008 12 67 15008 minecraft:oak_log
# Panneaux
kill @e[type=minecraft:text_display,tag=mg.mpdeco]
summon minecraft:text_display -17.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"DÉPART","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -13.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -9.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -5.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -1.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 2.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 6.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 10.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 14.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14986.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14990.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14994.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14998.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 15002.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"☠","color":"dark_gray","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 15006.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 15010.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 14.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 10.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 6.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 2.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -1.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -5.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -9.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -13.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 15014.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"☠","color":"dark_gray","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 15010.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 15006.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 15002.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14998.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14994.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14990.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 0.5 73 15000.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"★ MINI PARTY ★","color":"gold","bold":true},{"text":"\n1 dé, 32 cases, des étoiles à gagner","color":"yellow","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[5f,5f,5f]}}
data modify storage mg:party built set value 1b
