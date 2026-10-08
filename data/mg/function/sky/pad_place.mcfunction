# Plateforme posée, joueurs répartis dessus (gelés par le compte à rebours)
scoreboard players set $skpd mg.st 1
kill @e[tag=mg.sky]
execute if score $elm mg.st matches 1..2 run function mg:sky/pad1
execute if score $elm mg.st matches 3 run function mg:sky/pad3
scoreboard players set $skok mg.st 0
execute if score $elm mg.st matches 1..2 store success score $skok mg.st run spreadplayers 0 27640 1 4 under 237 false @a[tag=mg.play]
execute if score $elm mg.st matches 3 store success score $skok mg.st run spreadplayers 0 29000 1 4 under 197 false @a[tag=mg.play]
execute if score $skok mg.st matches 0 if score $elm mg.st matches 1..2 run tp @a[tag=mg.play] 0.5 236 27640.5
execute if score $skok mg.st matches 0 if score $elm mg.st matches 3 run tp @a[tag=mg.play] 0.5 196 29000.5
execute if score $elm mg.st matches 1..2 as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing 0.5 226.5 27700.5
execute if score $elm mg.st matches 3 as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing 0.5 185 29060
execute if score $elm mg.st matches 1..2 run spawnpoint @a[tag=mg.play] 0 236 27640
execute if score $elm mg.st matches 3 run spawnpoint @a[tag=mg.play] 0 196 29000
execute if score $elm mg.st matches 1 run summon minecraft:text_display 0.5 240 27640.5 {Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{"text":"🪽 COURSE D'ANNEAUX","color":"aqua","bold":true},{"text":"\n20 anneaux dans l'ordre — suis la traînée lumineuse","color":"gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.3f,1.3f,1.3f]}}
execute if score $elm mg.st matches 2 run summon minecraft:text_display 0.5 240 27640.5 {Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{"text":"🏹 COURSE + COMBAT","color":"red","bold":true},{"text":"\n20 anneaux — abats tes rivaux à l'arc et à la charge de vent","color":"gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.3f,1.3f,1.3f]}}
execute if score $elm mg.st matches 3 run summon minecraft:text_display 0.5 200 29000.5 {Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{"text":"🌪 SURVIE EN VOL","color":"light_purple","bold":true},{"text":"\nNe te pose jamais — reste dans la zone","color":"gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.3f,1.3f,1.3f]}}
