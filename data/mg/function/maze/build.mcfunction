# 🌀 Labyrinthe géant : construction (zone chargée ?)
execute unless loaded -50 64 41050 run return run schedule function mg:maze/build 10t
execute unless loaded 56 64 41150 run return run schedule function mg:maze/build 10t
execute unless loaded 0 64 41100 run return run schedule function mg:maze/build 10t
kill @e[type=!minecraft:player,x=-50,y=55,z=41050,dx=106,dy=40,dz=100]
fill -50 65 41050 49 65 41149 minecraft:air
fill -50 66 41050 49 66 41149 minecraft:air
fill -50 67 41050 49 67 41149 minecraft:air
fill -50 68 41050 49 68 41149 minecraft:air
fill -50 69 41050 49 69 41149 minecraft:air
fill -50 70 41050 49 70 41149 minecraft:air
fill -50 63 41050 49 63 41149 minecraft:dirt
fill -50 64 41050 49 64 41149 minecraft:grass_block
fill 50 64 41096 56 69 41103 minecraft:air
fill 50 64 41096 56 64 41103 minecraft:gold_block
fill 50 65 41096 56 68 41096 minecraft:glass
fill 50 65 41103 56 68 41103 minecraft:glass
fill 56 65 41097 56 68 41102 minecraft:glass
setblock 53 68 41100 minecraft:glowstone
execute if score $jv mg.st matches 1 run function mg:maze/walls_1
execute if score $jv mg.st matches 2 run function mg:maze/walls_2
execute if score $jv mg.st matches 3 run function mg:maze/walls_3
execute if score $jv mg.st matches 1 run function mg:maze/ents_1
execute if score $jv mg.st matches 2 run function mg:maze/ents_2
execute if score $jv mg.st matches 3 run function mg:maze/ents_3
scoreboard players set $jg mg.st 0
scoreboard players set $jok mg.st 1
summon minecraft:text_display 53 67.5 41100 {Tags:["mg.jent"],billboard:"center",text:{"text":"🏆 SORTIE","color":"gold","bold":true}}
