# Sheep War 4 « Cubes Voxel » — préparation (règles : sheepwar/go et sheepwar/tick)
function mg:sheepwar4/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-60,y=50,z=2665,dx=120,dy=70,dz=70]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 102
scoreboard players set $pz mg.st 2700

scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 102 2700
spreadplayers -22 2700 4 6 under 86 false @a[team=mg_red,tag=mg.play]
spreadplayers 22 2700 4 6 under 86 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 22 86 2700
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -22 86 2700
