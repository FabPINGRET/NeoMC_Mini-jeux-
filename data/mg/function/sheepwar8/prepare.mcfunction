# Sheep War 8 « Nuages voxel » — préparation (règles : sheepwar/go et sheepwar/tick)
function mg:sheepwar8/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-60,y=50,z=3865,dx=120,dy=70,dz=70]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 102
scoreboard players set $pz mg.st 3900

scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 102 3900
spreadplayers -21 3900 2 3 under 85 false @a[team=mg_red,tag=mg.play]
spreadplayers 21 3900 2 3 under 85 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 21 84 3900
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -21 84 3900
