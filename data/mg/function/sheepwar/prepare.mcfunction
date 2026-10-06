# Sheep War — préparation
function mg:sheepwar/build
kill @e[tag=mg.sheep]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 1500

# 2 équipes
scoreboard players set $nt mg.st 2
function mg:core/assign_teams

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 95 1500
spreadplayers -22 1500 3 10 under 81 false @a[team=mg_red,tag=mg.play]
spreadplayers 22 1500 3 10 under 81 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 22 80 1500
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing -22 80 1500
