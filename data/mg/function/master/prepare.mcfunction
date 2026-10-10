# 👑 Master dit — préparation
function mg:master/build
kill @e[tag=mg.msd]
summon minecraft:text_display 0.5 77 38600.5 {Tags:["mg.msd","mg.fx"],billboard:"center",background:0,text:{"text":"👑 MASTER","color":"gold","bold":true},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[3f,3f,3f]}}
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 79
scoreboard players set $pz mg.st 38600
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_sq @a[tag=mg.play]
spreadplayers 0 38600 2 7 under 73 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
scoreboard players set $msr mg.st 0
