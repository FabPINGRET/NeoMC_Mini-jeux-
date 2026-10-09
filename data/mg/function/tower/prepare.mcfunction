# 🏰 The Towers — préparation
function mg:tower/build
kill @e[type=minecraft:item,x=-50,y=50,z=20780,dx=100,dy=60,dz=40]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 20800
clear @a[tag=mg.play]
scoreboard players set $nt mg.st 2
function mg:core/assign_teams
scoreboard players reset Rouge mg.tw
scoreboard players reset Bleu mg.tw
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run function mg:tower/spawn
