# Block Party — préparation (centre 0 ~ 6400)
function mg:blockparty/build
kill @e[type=minecraft:item,x=-25,y=60,z=6375,dx=50,dy=40,dz=50]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 6400
scoreboard players set $rd mg.st 0
scoreboard players set $bp mg.st 0
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 6400
spreadplayers 0 6400 3 9 under 90 false @a[tag=mg.play]
