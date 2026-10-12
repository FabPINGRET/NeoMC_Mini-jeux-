# 🎩 Galerie des chapeaux sous le Hall (généré par tools/cosmetics/gen_hats.py) ; relancée par rp_on / rp_off, reconstruite par hat/second si absente
kill @e[tag=mg.hatg]
fill -35 44 7 -15 52 27 minecraft:deepslate_tiles hollow
fill -34 44 8 -16 44 26 minecraft:polished_deepslate
fill -34 52 8 -16 52 26 minecraft:dark_oak_planks
fill -35 45 7 -15 45 27 minecraft:polished_blackstone_bricks replace minecraft:deepslate_tiles
fill -35 51 7 -15 51 27 minecraft:chiseled_deepslate replace minecraft:deepslate_tiles
setblock -33 52 9 minecraft:ochre_froglight
setblock -33 52 13 minecraft:ochre_froglight
setblock -33 52 17 minecraft:ochre_froglight
setblock -33 52 21 minecraft:ochre_froglight
setblock -33 52 25 minecraft:ochre_froglight
setblock -29 52 9 minecraft:ochre_froglight
setblock -29 52 13 minecraft:ochre_froglight
setblock -29 52 17 minecraft:ochre_froglight
setblock -29 52 21 minecraft:ochre_froglight
setblock -29 52 25 minecraft:ochre_froglight
setblock -25 52 9 minecraft:ochre_froglight
setblock -25 52 13 minecraft:ochre_froglight
setblock -25 52 17 minecraft:ochre_froglight
setblock -25 52 21 minecraft:ochre_froglight
setblock -25 52 25 minecraft:ochre_froglight
setblock -21 52 9 minecraft:ochre_froglight
setblock -21 52 13 minecraft:ochre_froglight
setblock -21 52 17 minecraft:ochre_froglight
setblock -21 52 21 minecraft:ochre_froglight
setblock -21 52 25 minecraft:ochre_froglight
setblock -17 52 9 minecraft:ochre_froglight
setblock -17 52 13 minecraft:ochre_froglight
setblock -17 52 17 minecraft:ochre_froglight
setblock -17 52 21 minecraft:ochre_froglight
setblock -17 52 25 minecraft:ochre_froglight
fill -33 44 8 -33 44 26 minecraft:red_terracotta
fill -17 44 8 -17 44 26 minecraft:red_terracotta
fill -26 44 26 -24 44 26 minecraft:emerald_block
summon minecraft:text_display -24.5 47.3 26.3 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"⬆ Retour au spawn","color":"green","bold":true},{"text":"\nmarche sur les blocs d'émeraude","color":"gray"}]}
summon minecraft:text_display -24.5 50.6 24.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"🎩 Galerie des chapeaux","color":"gold","bold":true},{"text":"\nclique sur un piédestal · les victoires débloquent les plus rares","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
setblock -32 45 22 minecraft:polished_blackstone
summon minecraft:text_display -31.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"✖ Sans chapeau","color":"white","bold":true},{"text":"\nretire ton chapeau","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
summon minecraft:interaction -31.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-31.5,y=46,z=22.5,distance=..0.1] mg.st 0
setblock -30 45 22 minecraft:smooth_quartz
summon minecraft:text_display -29.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Haut-de-forme","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -29.5 46 22.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/top_hat"}}}}
summon minecraft:interaction -29.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-29.5,y=46,z=22.5,distance=..0.1] mg.st 1
setblock -28 45 22 minecraft:smooth_quartz
summon minecraft:text_display -27.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Chapeau de cowboy","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -27.5 46 22.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/cowboy"}}}}
summon minecraft:interaction -27.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-27.5,y=46,z=22.5,distance=..0.1] mg.st 2
setblock -26 45 22 minecraft:smooth_quartz
summon minecraft:text_display -25.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Bonnet à pompon","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -25.5 46 22.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/beanie"}}}}
summon minecraft:interaction -25.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-25.5,y=46,z=22.5,distance=..0.1] mg.st 3
setblock -24 45 22 minecraft:smooth_quartz
summon minecraft:text_display -23.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Casquette","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -23.5 46 22.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/cap"}}}}
summon minecraft:interaction -23.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-23.5,y=46,z=22.5,distance=..0.1] mg.st 4
setblock -22 45 22 minecraft:smooth_quartz
summon minecraft:text_display -21.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Béret","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -21.5 46 22.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/beret"}}}}
summon minecraft:interaction -21.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-21.5,y=46,z=22.5,distance=..0.1] mg.st 5
setblock -20 45 22 minecraft:smooth_quartz
summon minecraft:text_display -19.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Chapeau de paille","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -19.5 46 22.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/straw"}}}}
summon minecraft:interaction -19.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-19.5,y=46,z=22.5,distance=..0.1] mg.st 6
setblock -18 45 22 minecraft:smooth_quartz
summon minecraft:text_display -17.5 48.15 22.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Grenouille","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -17.5 46 22.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/frog"}}}}
summon minecraft:interaction -17.5 46 22.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-17.5,y=46,z=22.5,distance=..0.1] mg.st 7
setblock -32 45 19 minecraft:smooth_quartz
summon minecraft:text_display -31.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Canard","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -31.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/duck"}}}}
summon minecraft:interaction -31.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-31.5,y=46,z=19.5,distance=..0.1] mg.st 8
setblock -30 45 19 minecraft:smooth_quartz
summon minecraft:text_display -29.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Gâteau d'anniversaire","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -29.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/cake"}}}}
summon minecraft:interaction -29.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-29.5,y=46,z=19.5,distance=..0.1] mg.st 9
setblock -28 45 19 minecraft:smooth_quartz
summon minecraft:text_display -27.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Casque pastèque","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -27.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/melon"}}}}
summon minecraft:interaction -27.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-27.5,y=46,z=19.5,distance=..0.1] mg.st 10
setblock -26 45 19 minecraft:smooth_quartz
summon minecraft:text_display -25.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Cône de chantier","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -25.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/cone"}}}}
summon minecraft:interaction -25.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-25.5,y=46,z=19.5,distance=..0.1] mg.st 11
setblock -24 45 19 minecraft:smooth_quartz
summon minecraft:text_display -23.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Poulet sur la tête","color":"white","bold":true},{"text":"\nCommun","color":"gray"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -23.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/chicken"}}}}
summon minecraft:interaction -23.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-23.5,y=46,z=19.5,distance=..0.1] mg.st 12
setblock -22 45 19 minecraft:prismarine_bricks
summon minecraft:text_display -21.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Toque de diplômé","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -21.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/grad_cap"}}}}
summon minecraft:interaction -21.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-21.5,y=46,z=19.5,distance=..0.1] mg.st 13
setblock -20 45 19 minecraft:prismarine_bricks
summon minecraft:text_display -19.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Chat endormi","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -19.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/sleepy_cat"}}}}
summon minecraft:interaction -19.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-19.5,y=46,z=19.5,distance=..0.1] mg.st 14
setblock -18 45 19 minecraft:prismarine_bricks
summon minecraft:text_display -17.5 48.15 19.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Axolotl","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -17.5 46 19.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/axolotl"}}}}
summon minecraft:interaction -17.5 46 19.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-17.5,y=46,z=19.5,distance=..0.1] mg.st 15
setblock -32 45 16 minecraft:prismarine_bricks
summon minecraft:text_display -31.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Abeille","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -31.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/bee"}}}}
summon minecraft:interaction -31.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-31.5,y=46,z=16.5,distance=..0.1] mg.st 16
setblock -30 45 16 minecraft:prismarine_bricks
summon minecraft:text_display -29.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Burger","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -29.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/burger"}}}}
summon minecraft:interaction -29.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-29.5,y=46,z=16.5,distance=..0.1] mg.st 17
setblock -28 45 16 minecraft:prismarine_bricks
summon minecraft:text_display -27.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Sushi","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -27.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/sushi"}}}}
summon minecraft:interaction -27.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-27.5,y=46,z=16.5,distance=..0.1] mg.st 18
setblock -26 45 16 minecraft:prismarine_bricks
summon minecraft:text_display -25.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Chapeau TNT","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -25.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/tnt"}}}}
summon minecraft:interaction -25.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-25.5,y=46,z=16.5,distance=..0.1] mg.st 19
setblock -24 45 16 minecraft:prismarine_bricks
summon minecraft:text_display -23.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Casquette à hélice","color":"aqua","bold":true},{"text":"\nRare · 5 victoires","color":"aqua"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -23.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/propeller"}}}}
summon minecraft:interaction -23.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-23.5,y=46,z=16.5,distance=..0.1] mg.st 20
setblock -22 45 16 minecraft:purpur_block
summon minecraft:text_display -21.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Chapeau de sorcier","color":"light_purple","bold":true},{"text":"\nÉpique · 20 victoires","color":"light_purple"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -21.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/wizard"}}}}
summon minecraft:interaction -21.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-21.5,y=46,z=16.5,distance=..0.1] mg.st 21
setblock -20 45 16 minecraft:purpur_block
summon minecraft:text_display -19.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Casque viking","color":"light_purple","bold":true},{"text":"\nÉpique · 20 victoires","color":"light_purple"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -19.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/viking"}}}}
summon minecraft:interaction -19.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-19.5,y=46,z=16.5,distance=..0.1] mg.st 22
setblock -18 45 16 minecraft:purpur_block
summon minecraft:text_display -17.5 48.15 16.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Heaume de chevalier","color":"light_purple","bold":true},{"text":"\nÉpique · 20 victoires","color":"light_purple"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -17.5 46 16.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/knight"}}}}
summon minecraft:interaction -17.5 46 16.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-17.5,y=46,z=16.5,distance=..0.1] mg.st 23
setblock -32 45 13 minecraft:purpur_block
summon minecraft:text_display -31.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Bocal à poisson","color":"light_purple","bold":true},{"text":"\nÉpique · 20 victoires","color":"light_purple"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -31.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/fishbowl"}}}}
summon minecraft:interaction -31.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-31.5,y=46,z=13.5,distance=..0.1] mg.st 24
setblock -30 45 13 minecraft:gold_block
summon minecraft:text_display -29.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Couronne flottante","color":"gold","bold":true},{"text":"\nLégendaire · 50 victoires","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -29.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/crown"}}}}
summon minecraft:interaction -29.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-29.5,y=46,z=13.5,distance=..0.1] mg.st 25
setblock -28 45 13 minecraft:gold_block
summon minecraft:text_display -27.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Crâne de dragon","color":"gold","bold":true},{"text":"\nLégendaire · 50 victoires","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -27.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/dragon"}}}}
summon minecraft:interaction -27.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-27.5,y=46,z=13.5,distance=..0.1] mg.st 26
setblock -26 45 13 minecraft:gold_block
summon minecraft:text_display -25.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Laurier de champion","color":"gold","bold":true},{"text":"\nLégendaire · 50 victoires","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -25.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/laurel"}}}}
summon minecraft:interaction -25.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-25.5,y=46,z=13.5,distance=..0.1] mg.st 27
setblock -24 45 13 minecraft:gold_block
summon minecraft:text_display -23.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Couronne de flammes","color":"gold","bold":true},{"text":"\nLégendaire · 50 victoires","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -23.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/flame_crown"}}}}
summon minecraft:interaction -23.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-23.5,y=46,z=13.5,distance=..0.1] mg.st 28
setblock -22 45 13 minecraft:carved_pumpkin[facing=south]
summon minecraft:text_display -21.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Chapeau de sorcière","color":"gold","bold":true},{"text":"\n🎃 Halloween seulement","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -21.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/witch"}}}}
summon minecraft:interaction -21.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-21.5,y=46,z=13.5,distance=..0.1] mg.st 29
setblock -20 45 13 minecraft:carved_pumpkin[facing=south]
summon minecraft:text_display -19.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Citrouille-lanterne","color":"gold","bold":true},{"text":"\n🎃 Halloween seulement","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -19.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/pumpkin"}}}}
summon minecraft:interaction -19.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-19.5,y=46,z=13.5,distance=..0.1] mg.st 30
setblock -18 45 13 minecraft:carved_pumpkin[facing=south]
summon minecraft:text_display -17.5 48.15 13.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Drap de fantôme","color":"gold","bold":true},{"text":"\n🎃 Halloween seulement","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -17.5 46 13.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/ghost"}}}}
summon minecraft:interaction -17.5 46 13.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-17.5,y=46,z=13.5,distance=..0.1] mg.st 31
setblock -28 45 10 minecraft:carved_pumpkin[facing=south]
summon minecraft:text_display -27.5 48.15 10.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Chauve-souris","color":"gold","bold":true},{"text":"\n🎃 Halloween seulement","color":"gold"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -27.5 46 10.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/bat"}}}}
summon minecraft:interaction -27.5 46 10.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-27.5,y=46,z=10.5,distance=..0.1] mg.st 32
setblock -26 45 10 minecraft:packed_ice
summon minecraft:text_display -25.5 48.15 10.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Bonnet de Noël","color":"red","bold":true},{"text":"\n🎄 Noël seulement","color":"red"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -25.5 46 10.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/santa"}}}}
summon minecraft:interaction -25.5 46 10.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-25.5,y=46,z=10.5,distance=..0.1] mg.st 33
setblock -24 45 10 minecraft:packed_ice
summon minecraft:text_display -23.5 48.15 10.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Bois de renne","color":"red","bold":true},{"text":"\n🎄 Noël seulement","color":"red"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -23.5 46 10.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/antlers"}}}}
summon minecraft:interaction -23.5 46 10.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-23.5,y=46,z=10.5,distance=..0.1] mg.st 34
setblock -22 45 10 minecraft:packed_ice
summon minecraft:text_display -21.5 48.15 10.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"Tête de bonhomme de neige","color":"red","bold":true},{"text":"\n🎄 Noël seulement","color":"red"}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}
execute if score $rp mg.st matches 1 run summon minecraft:armor_stand -21.5 46 10.5 {Tags:["mg.hat","mg.hatg"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{head:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/snowman"}}}}
summon minecraft:interaction -21.5 46 10.5 {Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}
scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x=-21.5,y=46,z=10.5,distance=..0.1] mg.st 35
summon minecraft:text_display -19.5 66.4 8.5 {Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,text:[{"text":"🎩 Galerie des chapeaux","color":"gold","bold":true},{"text":"\nmarche ici pour descendre","color":"gray"}]}
execute if score $rp mg.st matches 1 run summon minecraft:item_display -19.5 65.3 8.5 {Tags:["mg.hat","mg.hatg","mg.lspin"],billboard:"fixed",item_display:"head",item:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/top_hat"}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}
