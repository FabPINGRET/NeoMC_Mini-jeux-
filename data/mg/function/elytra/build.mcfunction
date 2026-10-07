# Parcours d'élytra : construction (généré par tools/elytra/gen_elytra.py)
kill @e[tag=mg.elyd]
data modify storage mg:lobby ely1 set value 1b

# Socle de départ au sol
fill 14 63 -11 18 63 -7 minecraft:smooth_quartz
fill 15 63 -10 17 63 -8 minecraft:light_blue_concrete
setblock 16 63 -9 minecraft:sea_lantern
summon minecraft:item_display 16.5 66 -8.5 {Tags:["mg.elyd","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}
summon minecraft:text_display 16.5 67.8 -8.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"🪽 Parcours d'élytra","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 16.5 67.3 -8.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"Monte au centre du socle","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}

# Plateforme de départ
fill -51 174 -47 -47 174 -43 minecraft:smooth_quartz
fill -51 174 -47 -51 175 -43 minecraft:light_blue_stained_glass
setblock -51 176 -45 minecraft:sea_lantern
summon minecraft:text_display -48.5 177.5 -44.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"Saute vers l'est, ouvre tes élytres (Espace en l'air)","color":"yellow"},{"text":"\n8 anneaux dans l'ordre — 3 fusées pour t'aider","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}

# Anneaux (cadre 7x7, ouverture 5x5)
fill -15 166 -48 -15 172 -42 minecraft:light_blue_concrete
fill -15 167 -47 -15 171 -43 minecraft:air
setblock -15 166 -48 minecraft:sea_lantern
setblock -15 166 -42 minecraft:sea_lantern
setblock -15 172 -48 minecraft:sea_lantern
setblock -15 172 -42 minecraft:sea_lantern
summon minecraft:text_display -14.5 173.2 -44.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"1","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 15 162 -48 15 168 -42 minecraft:magenta_concrete
fill 15 163 -47 15 167 -43 minecraft:air
setblock 15 162 -48 minecraft:sea_lantern
setblock 15 162 -42 minecraft:sea_lantern
setblock 15 168 -48 minecraft:sea_lantern
setblock 15 168 -42 minecraft:sea_lantern
summon minecraft:text_display 15.5 169.2 -44.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"2","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 42 156 -15 48 162 -15 minecraft:lime_concrete
fill 43 157 -15 47 161 -15 minecraft:air
setblock 42 156 -15 minecraft:sea_lantern
setblock 48 156 -15 minecraft:sea_lantern
setblock 42 162 -15 minecraft:sea_lantern
setblock 48 162 -15 minecraft:sea_lantern
summon minecraft:text_display 45.5 163.2 -14.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"3","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 42 152 15 48 158 15 minecraft:orange_concrete
fill 43 153 15 47 157 15 minecraft:air
setblock 42 152 15 minecraft:sea_lantern
setblock 48 152 15 minecraft:sea_lantern
setblock 42 158 15 minecraft:sea_lantern
setblock 48 158 15 minecraft:sea_lantern
summon minecraft:text_display 45.5 159.2 15.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"4","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 15 146 42 15 152 48 minecraft:light_blue_concrete
fill 15 147 43 15 151 47 minecraft:air
setblock 15 146 42 minecraft:sea_lantern
setblock 15 146 48 minecraft:sea_lantern
setblock 15 152 42 minecraft:sea_lantern
setblock 15 152 48 minecraft:sea_lantern
summon minecraft:text_display 15.5 153.2 45.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"5","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill -15 142 42 -15 148 48 minecraft:magenta_concrete
fill -15 143 43 -15 147 47 minecraft:air
setblock -15 142 42 minecraft:sea_lantern
setblock -15 142 48 minecraft:sea_lantern
setblock -15 148 42 minecraft:sea_lantern
setblock -15 148 48 minecraft:sea_lantern
summon minecraft:text_display -14.5 149.2 45.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"6","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill -48 136 15 -42 142 15 minecraft:lime_concrete
fill -47 137 15 -43 141 15 minecraft:air
setblock -48 136 15 minecraft:sea_lantern
setblock -42 136 15 minecraft:sea_lantern
setblock -48 142 15 minecraft:sea_lantern
setblock -42 142 15 minecraft:sea_lantern
summon minecraft:text_display -44.5 143.2 15.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"7","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill -48 132 -15 -42 138 -15 minecraft:gold_block
fill -47 133 -15 -43 137 -15 minecraft:air
setblock -48 132 -15 minecraft:sea_lantern
setblock -42 132 -15 minecraft:sea_lantern
setblock -48 138 -15 minecraft:sea_lantern
setblock -42 138 -15 minecraft:sea_lantern
summon minecraft:text_display -44.5 139.2 -14.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"🏁","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
