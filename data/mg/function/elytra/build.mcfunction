# Parcours d'élytra et élytres libres : construction (généré par tools/elytra/gen_elytra.py)
kill @e[tag=mg.elyd]
data modify storage mg:lobby ely1 set value 1b

# ===== Petit parcours d'élytra (8 anneaux)
fill 14 63 -11 18 63 -7 minecraft:smooth_quartz
fill 15 63 -10 17 63 -8 minecraft:light_blue_concrete
setblock 16 63 -9 minecraft:sea_lantern
summon minecraft:item_display 16.5 66 -8.5 {Tags:["mg.elyd","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}
summon minecraft:text_display 16.5 67.8 -8.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"🪽 Petit parcours d'élytra","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 16.5 67.3 -8.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"8 anneaux chronométrés — monte au centre du socle","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}
fill -51 174 -47 -47 174 -43 minecraft:smooth_quartz
fill -51 174 -47 -51 175 -43 minecraft:light_blue_stained_glass
setblock -51 176 -45 minecraft:sea_lantern
summon minecraft:text_display -48.5 177.5 -44.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"Saute vers l'est, ouvre tes élytres (Espace en l'air)","color":"yellow"},{"text":"\n8 anneaux dans l'ordre — 4 fusées pour t'aider","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
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

# ===== Grand parcours d'élytra (15 anneaux)
fill 30 63 -17 34 63 -13 minecraft:smooth_quartz
fill 31 63 -16 33 63 -14 minecraft:purple_concrete
setblock 32 63 -15 minecraft:sea_lantern
summon minecraft:item_display 32.5 66 -14.5 {Tags:["mg.elyd","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}
summon minecraft:text_display 32.5 67.8 -14.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"🪽 Grand parcours d'élytra","color":"light_purple","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 32.5 67.3 -14.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"15 anneaux chronométrés — monte au centre du socle","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}
fill -55 299 -50 -51 299 -46 minecraft:smooth_quartz
fill -55 299 -50 -55 300 -46 minecraft:light_blue_stained_glass
setblock -55 301 -48 minecraft:sea_lantern
summon minecraft:text_display -52.5 302.5 -47.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"Saute vers l'est, ouvre tes élytres (Espace en l'air)","color":"yellow"},{"text":"\n15 anneaux dans l'ordre — 6 fusées pour t'aider","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
fill -30 289 -51 -30 295 -45 minecraft:light_blue_concrete
fill -30 290 -50 -30 294 -46 minecraft:air
setblock -30 289 -51 minecraft:sea_lantern
setblock -30 289 -45 minecraft:sea_lantern
setblock -30 295 -51 minecraft:sea_lantern
setblock -30 295 -45 minecraft:sea_lantern
summon minecraft:text_display -29.5 296.2 -47.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"1","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 0 283 -51 0 289 -45 minecraft:magenta_concrete
fill 0 284 -50 0 288 -46 minecraft:air
setblock 0 283 -51 minecraft:sea_lantern
setblock 0 283 -45 minecraft:sea_lantern
setblock 0 289 -51 minecraft:sea_lantern
setblock 0 289 -45 minecraft:sea_lantern
summon minecraft:text_display 0.5 290.2 -47.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"2","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 30 276 -51 30 282 -45 minecraft:lime_concrete
fill 30 277 -50 30 281 -46 minecraft:air
setblock 30 276 -51 minecraft:sea_lantern
setblock 30 276 -45 minecraft:sea_lantern
setblock 30 282 -51 minecraft:sea_lantern
setblock 30 282 -45 minecraft:sea_lantern
summon minecraft:text_display 30.5 283.2 -47.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"3","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 30 269 -27 30 275 -21 minecraft:orange_concrete
fill 30 270 -26 30 274 -22 minecraft:air
setblock 30 269 -27 minecraft:sea_lantern
setblock 30 269 -21 minecraft:sea_lantern
setblock 30 275 -27 minecraft:sea_lantern
setblock 30 275 -21 minecraft:sea_lantern
summon minecraft:text_display 30.5 276.2 -23.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"4","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 0 263 -27 0 269 -21 minecraft:light_blue_concrete
fill 0 264 -26 0 268 -22 minecraft:air
setblock 0 263 -27 minecraft:sea_lantern
setblock 0 263 -21 minecraft:sea_lantern
setblock 0 269 -27 minecraft:sea_lantern
setblock 0 269 -21 minecraft:sea_lantern
summon minecraft:text_display 0.5 270.2 -23.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"5","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill -30 257 -27 -30 263 -21 minecraft:magenta_concrete
fill -30 258 -26 -30 262 -22 minecraft:air
setblock -30 257 -27 minecraft:sea_lantern
setblock -30 257 -21 minecraft:sea_lantern
setblock -30 263 -27 minecraft:sea_lantern
setblock -30 263 -21 minecraft:sea_lantern
summon minecraft:text_display -29.5 264.2 -23.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"6","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill -30 250 -3 -30 256 3 minecraft:lime_concrete
fill -30 251 -2 -30 255 2 minecraft:air
setblock -30 250 -3 minecraft:sea_lantern
setblock -30 250 3 minecraft:sea_lantern
setblock -30 256 -3 minecraft:sea_lantern
setblock -30 256 3 minecraft:sea_lantern
summon minecraft:text_display -29.5 257.2 0.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"7","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 0 243 -3 0 249 3 minecraft:orange_concrete
fill 0 244 -2 0 248 2 minecraft:air
setblock 0 243 -3 minecraft:sea_lantern
setblock 0 243 3 minecraft:sea_lantern
setblock 0 249 -3 minecraft:sea_lantern
setblock 0 249 3 minecraft:sea_lantern
summon minecraft:text_display 0.5 250.2 0.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"8","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 30 237 -3 30 243 3 minecraft:light_blue_concrete
fill 30 238 -2 30 242 2 minecraft:air
setblock 30 237 -3 minecraft:sea_lantern
setblock 30 237 3 minecraft:sea_lantern
setblock 30 243 -3 minecraft:sea_lantern
setblock 30 243 3 minecraft:sea_lantern
summon minecraft:text_display 30.5 244.2 0.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"9","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 30 231 21 30 237 27 minecraft:magenta_concrete
fill 30 232 22 30 236 26 minecraft:air
setblock 30 231 21 minecraft:sea_lantern
setblock 30 231 27 minecraft:sea_lantern
setblock 30 237 21 minecraft:sea_lantern
setblock 30 237 27 minecraft:sea_lantern
summon minecraft:text_display 30.5 238.2 24.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"10","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 0 224 21 0 230 27 minecraft:lime_concrete
fill 0 225 22 0 229 26 minecraft:air
setblock 0 224 21 minecraft:sea_lantern
setblock 0 224 27 minecraft:sea_lantern
setblock 0 230 21 minecraft:sea_lantern
setblock 0 230 27 minecraft:sea_lantern
summon minecraft:text_display 0.5 231.2 24.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"11","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill -30 217 21 -30 223 27 minecraft:orange_concrete
fill -30 218 22 -30 222 26 minecraft:air
setblock -30 217 21 minecraft:sea_lantern
setblock -30 217 27 minecraft:sea_lantern
setblock -30 223 21 minecraft:sea_lantern
setblock -30 223 27 minecraft:sea_lantern
summon minecraft:text_display -29.5 224.2 24.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"12","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill -30 211 45 -30 217 51 minecraft:light_blue_concrete
fill -30 212 46 -30 216 50 minecraft:air
setblock -30 211 45 minecraft:sea_lantern
setblock -30 211 51 minecraft:sea_lantern
setblock -30 217 45 minecraft:sea_lantern
setblock -30 217 51 minecraft:sea_lantern
summon minecraft:text_display -29.5 218.2 48.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"13","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 0 205 45 0 211 51 minecraft:magenta_concrete
fill 0 206 46 0 210 50 minecraft:air
setblock 0 205 45 minecraft:sea_lantern
setblock 0 205 51 minecraft:sea_lantern
setblock 0 211 45 minecraft:sea_lantern
setblock 0 211 51 minecraft:sea_lantern
summon minecraft:text_display 0.5 212.2 48.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"14","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
fill 30 198 45 30 204 51 minecraft:gold_block
fill 30 199 46 30 203 50 minecraft:air
setblock 30 198 45 minecraft:sea_lantern
setblock 30 198 51 minecraft:sea_lantern
setblock 30 204 45 minecraft:sea_lantern
setblock 30 204 51 minecraft:sea_lantern
summon minecraft:text_display 30.5 205.2 48.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"🏁","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}

# ===== Élytres libres
fill 14 63 -23 18 63 -19 minecraft:smooth_quartz
fill 15 63 -22 17 63 -20 minecraft:white_concrete
setblock 16 63 -21 minecraft:sea_lantern
summon minecraft:item_display 16.5 66 -20.5 {Tags:["mg.elyd","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}
summon minecraft:text_display 16.5 67.8 -20.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"🪽 Élytres libres","color":"white","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 16.5 67.3 -20.5 {Tags:["mg.elyd"],billboard:"center",background:0,text:[{"text":"Vol autour du spawn, fusées illimitées — remonte dessus pour les rendre","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}
function mg:elytra/spawn_clean
