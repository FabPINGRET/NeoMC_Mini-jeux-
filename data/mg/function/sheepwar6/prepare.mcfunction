# Sheep War 6 « Archipel bicolore » — préparation (règles : sheepwar/go et sheepwar/tick)
function mg:sheepwar6/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-60,y=50,z=3265,dx=120,dy=70,dz=70]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 3300

scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 100 3300
spreadplayers -26 3300 4 9 under 92 false @a[team=mg_red,tag=mg.play]
spreadplayers 26 3300 4 9 under 92 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 26 89 3300
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -26 89 3300
