# 🧟 Zombies — préparation
function mg:zm3/build
function mg:zm3/kill_all
function mg:zm3/entities
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 36100
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_blue @a[tag=mg.play]
spreadplayers 0 36100 2 6 under 84 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
