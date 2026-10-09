# ⛏ Mini UHC Run — préparation
function mg:uhc3/build
function mg:uhc3/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 105
scoreboard players set $pz mg.st 34800
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team leave @a[tag=mg.play]
spreadplayers 0 34800 8 34 under 100 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
