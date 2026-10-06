# Sheep War 3 « Bastions » — préparation (règles : sheepwar/go et sheepwar/tick)
function mg:sheepwar3/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-40,y=70,z=2380,dx=80,dy=30,dz=40]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 2400

scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 95 2400
spreadplayers -15 2400 2 2 under 81 false @a[team=mg_red,tag=mg.play]
spreadplayers 15 2400 2 2 under 81 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 15 80 2400
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -15 80 2400
