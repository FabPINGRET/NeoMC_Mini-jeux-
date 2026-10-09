# 🧟 Zombies — préparation
function mg:zm2/build
function mg:zm2/kill_all
function mg:zm2/entities
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 35800
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_blue @a[tag=mg.play]
spreadplayers 0 35800 2 6 under 84 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
