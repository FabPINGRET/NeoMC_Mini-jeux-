# Turf Wars — préparation (terrain x 100..130, z 7000)
function mg:turf/build
function mg:turf/columns
scoreboard players set $nr mg.st 15
scoreboard players set $nb mg.st 15
kill @e[type=minecraft:arrow]
kill @e[type=minecraft:item,x=90,y=60,z=6978,dx=60,dy=40,dz=50]
scoreboard players set $px mg.st 115
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 7000
scoreboard players set $nt mg.st 2
function mg:core/assign_teams
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 115 81 7000
spreadplayers 105 7000 3 8 under 90 false @a[team=mg_red,tag=mg.play]
spreadplayers 125 7000 3 8 under 90 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ facing 115 82 7000
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ facing 115 82 7000
