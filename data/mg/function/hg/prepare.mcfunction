# 🏹 Mini Hunger Games — préparation
function mg:hg/build
function mg:hg/pedestals
function mg:hg/chests
function mg:hg/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 110
scoreboard players set $pz mg.st 22800
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team leave @a[tag=mg.play]
function mg:hg/place
