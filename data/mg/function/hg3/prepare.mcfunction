# 🏹 Mini Hunger Games — préparation
function mg:hg3/build
function mg:hg3/pedestals
function mg:hg3/chests
function mg:hg3/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 110
scoreboard players set $pz mg.st 35000
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team leave @a[tag=mg.play]
function mg:hg3/place
