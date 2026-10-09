# 🧪 Infection — préparation
function mg:zm3/build
function mg:zm3/kill_all
function mg:zm3/entities
function mg:zm3/open_all
scoreboard players set $px mg.st 11
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 36089
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_blue @a[tag=mg.play]
spreadplayers 11 36089 4 18 under 84 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
