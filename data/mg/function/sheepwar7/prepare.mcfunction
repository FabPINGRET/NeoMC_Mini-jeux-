# Sheep War 7 « Double canyon » — préparation (règles : sheepwar/go et sheepwar/tick)
function mg:sheepwar7/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-60,y=50,z=3560,dx=120,dy=70,dz=80]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 3600

scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 100 3600
spreadplayers -20 3600 3 3 under 90 false @a[team=mg_red,tag=mg.play]
spreadplayers 20 3600 3 3 under 90 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 20 85 3600
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -20 85 3600
