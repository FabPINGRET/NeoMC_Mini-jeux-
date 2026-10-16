# 🧪 Infection — préparation
function mg:zm6/build
function mg:zm6/kill_all
function mg:zm6/entities
function mg:zm6/open_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 39800
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_blue @a[tag=mg.play]
execute as @a[tag=mg.play] run tp @s @e[type=minecraft:marker,tag=mg.zrc,sort=random,limit=1]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
tag @a remove mg.zhit
advancement revoke @a only mg:infhit
