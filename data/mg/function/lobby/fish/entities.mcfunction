# Zone cliquable et panneau du socle (tag mg.lfs, sans mg.lby) : les anciens sont retirés
kill @e[tag=mg.lfs]
summon minecraft:interaction 36.5 64 -26.5 {Tags:["mg.lfs","mg.lfi"],width:1.05f,height:1.05f,response:1b}
summon minecraft:text_display 36.5 65.6 -26.5 {Tags:["mg.lfs"],billboard:"center",background:0,text:[{"text":"🎣 Pêche à l'étang","color":"aqua","bold":true},{"text":"\nclic droit : prendre ou ranger la canne","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
