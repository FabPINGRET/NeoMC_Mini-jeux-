# 🌀 Labyrinthe géant : construction (zone chargée ?)
execute unless loaded -50 64 41050 run return run schedule function mg:maze/build 10t
execute unless loaded 56 64 41150 run return run schedule function mg:maze/build 10t
execute unless loaded 0 64 41100 run return run schedule function mg:maze/build 10t
kill @e[type=!minecraft:player,x=-50,y=55,z=41050,dx=106,dy=40,dz=100]
fill -50 65 41050 49 65 41149 minecraft:air
fill -50 66 41050 49 66 41149 minecraft:air
fill -50 67 41050 49 67 41149 minecraft:air
fill -50 68 41050 49 68 41149 minecraft:air
scoreboard players set $jbs mg.st 1
schedule function mg:maze/build_step 2t
