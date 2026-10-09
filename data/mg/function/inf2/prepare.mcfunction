# 🧪 Infection — préparation
function mg:zm2/build
function mg:zm2/kill_all
function mg:zm2/entities
function mg:zm2/open_all
scoreboard players set $px mg.st 11
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 35789
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_blue @a[tag=mg.play]
spreadplayers 11 35789 4 18 under 84 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
