# 🧪 Infection — préparation
function mg:zm/build
function mg:zm/kill_all
function mg:zm/entities
function mg:zm/open_all
scoreboard players set $px mg.st 11
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 23189
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_blue @a[tag=mg.play]
spreadplayers 11 23189 4 18 under 84 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
