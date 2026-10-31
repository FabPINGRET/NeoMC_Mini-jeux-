# Sheep War 9 « Mini-îles » — préparation (règles : sheepwar/go et sheepwar/tick) ; petite carte, 12 blocs entre les îles
function mg:sheepwar9/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-32,y=60,z=31780,dx=64,dy=40,dz=40]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 31800

scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 95 31800
spreadplayers -11 31800 1 2 under 81 false @a[team=mg_red,tag=mg.play]
spreadplayers 11 31800 1 2 under 81 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 11 80 31800
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -11 80 31800
