# 🏹 Mini Hunger Games — préparation
function mg:hg2/build
function mg:hg2/pedestals
function mg:hg2/chests
function mg:hg2/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 110
scoreboard players set $pz mg.st 34600
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team leave @a[tag=mg.play]
function mg:hg2/place
