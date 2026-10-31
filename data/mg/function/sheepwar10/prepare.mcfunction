# Sheep War 10 « Pont » — préparation (règles : sheepwar/go et sheepwar/tick) ; petite carte, un pont de bois entre les camps
function mg:sheepwar10/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-32,y=60,z=32030,dx=64,dy=40,dz=40]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 32050

scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 95 32050
spreadplayers -14 32050 1 2 under 81 false @a[team=mg_red,tag=mg.play]
spreadplayers 14 32050 1 2 under 81 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 14 80 32050
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -14 80 32050
