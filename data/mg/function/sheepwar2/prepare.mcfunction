# Sheep War 2 « Forteresses » — préparation (les règles de jeu sont celles de Sheep War : sheepwar/go et sheepwar/tick)
function mg:sheepwar2/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[type=minecraft:item,x=-46,y=70,z=2070,dx=92,dy=30,dz=60]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 2100

# 2 équipes
scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 95 2100
spreadplayers -18 2100 2 3 under 81 false @a[team=mg_red,tag=mg.play]
spreadplayers 18 2100 2 3 under 81 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 18 80 2100
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -18 80 2100
