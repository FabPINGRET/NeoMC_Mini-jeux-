# Plateau de la Mini Party (z 14300) : île, chemin, 32 cases, déco centrale
fill -24 62 14280 24 62 14320 minecraft:dirt
fill -24 63 14280 24 63 14320 minecraft:grass_block
fill -24 64 14280 24 72 14320 minecraft:air
fill -18 63 14286 18 63 14286 minecraft:smooth_stone
fill -18 63 14314 18 63 14314 minecraft:smooth_stone
fill -18 63 14286 -18 63 14314 minecraft:smooth_stone
fill 18 63 14286 18 63 14314 minecraft:smooth_stone
fill -19 63 14285 -17 63 14287 minecraft:gold_block
fill -15 63 14285 -13 63 14287 minecraft:blue_concrete
fill -11 63 14285 -9 63 14287 minecraft:blue_concrete
fill -7 63 14285 -5 63 14287 minecraft:red_concrete
fill -3 63 14285 -1 63 14287 minecraft:blue_concrete
fill 1 63 14285 3 63 14287 minecraft:lime_concrete
fill 5 63 14285 7 63 14287 minecraft:blue_concrete
fill 9 63 14285 11 63 14287 minecraft:blue_concrete
fill 13 63 14285 15 63 14287 minecraft:red_concrete
fill 17 63 14285 19 63 14287 minecraft:blue_concrete
fill 17 63 14289 19 63 14291 minecraft:lime_concrete
fill 17 63 14293 19 63 14295 minecraft:blue_concrete
fill 17 63 14297 19 63 14299 minecraft:blue_concrete
fill 17 63 14301 19 63 14303 minecraft:black_concrete
fill 17 63 14305 19 63 14307 minecraft:blue_concrete
fill 17 63 14309 19 63 14311 minecraft:red_concrete
fill 17 63 14313 19 63 14315 minecraft:blue_concrete
fill 13 63 14313 15 63 14315 minecraft:lime_concrete
fill 9 63 14313 11 63 14315 minecraft:blue_concrete
fill 5 63 14313 7 63 14315 minecraft:blue_concrete
fill 1 63 14313 3 63 14315 minecraft:red_concrete
fill -3 63 14313 -1 63 14315 minecraft:blue_concrete
fill -7 63 14313 -5 63 14315 minecraft:lime_concrete
fill -11 63 14313 -9 63 14315 minecraft:blue_concrete
fill -15 63 14313 -13 63 14315 minecraft:blue_concrete
fill -19 63 14313 -17 63 14315 minecraft:black_concrete
fill -19 63 14309 -17 63 14311 minecraft:blue_concrete
fill -19 63 14305 -17 63 14307 minecraft:red_concrete
fill -19 63 14301 -17 63 14303 minecraft:blue_concrete
fill -19 63 14297 -17 63 14299 minecraft:lime_concrete
fill -19 63 14293 -17 63 14295 minecraft:blue_concrete
fill -19 63 14289 -17 63 14291 minecraft:red_concrete
# Bassin et arbres au centre
fill -8 63 14296 8 63 14304 minecraft:water
fill -9 63 14295 9 63 14295 minecraft:sand
fill -9 63 14305 9 63 14305 minecraft:sand
fill -9 63 14295 -9 63 14305 minecraft:sand
fill 9 63 14295 9 63 14305 minecraft:sand
fill -14 66 14290 -10 67 14294 minecraft:oak_leaves[persistent=true]
fill -13 68 14291 -11 68 14293 minecraft:oak_leaves[persistent=true]
fill -12 64 14292 -12 67 14292 minecraft:oak_log
fill -14 66 14306 -10 67 14310 minecraft:oak_leaves[persistent=true]
fill -13 68 14307 -11 68 14309 minecraft:oak_leaves[persistent=true]
fill -12 64 14308 -12 67 14308 minecraft:oak_log
fill 10 66 14290 14 67 14294 minecraft:oak_leaves[persistent=true]
fill 11 68 14291 13 68 14293 minecraft:oak_leaves[persistent=true]
fill 12 64 14292 12 67 14292 minecraft:oak_log
fill 10 66 14306 14 67 14310 minecraft:oak_leaves[persistent=true]
fill 11 68 14307 13 68 14309 minecraft:oak_leaves[persistent=true]
fill 12 64 14308 12 67 14308 minecraft:oak_log
# Panneaux
kill @e[type=minecraft:text_display,tag=mg.mpdeco]
summon minecraft:text_display -17.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"DÉPART","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -13.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -9.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -5.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -1.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 2.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 6.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 10.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 14.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14286.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14290.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14294.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14298.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14302.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"☠","color":"dark_gray","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14306.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14310.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 18.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 14.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 10.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 6.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 2.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -1.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -5.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -9.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -13.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14314.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"☠","color":"dark_gray","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14310.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14306.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14302.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14298.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"?","color":"green","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14294.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"+3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display -17.5 64.6 14290.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"-3","color":"red","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
summon minecraft:text_display 0.5 73 14300.5 {Tags:["mg.mpdeco"],billboard:"center",text:[{"text":"★ MINI PARTY ★","color":"gold","bold":true},{"text":"\n1 dé, 32 cases, des étoiles à gagner","color":"yellow","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[5f,5f,5f]}}
data modify storage mg:party built set value 1b
