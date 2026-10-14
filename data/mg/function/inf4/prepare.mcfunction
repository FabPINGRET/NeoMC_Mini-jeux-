# 🧪 Infection — préparation
function mg:zm4/build
function mg:zm4/kill_all
function mg:zm4/entities
function mg:zm4/open_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 39100
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_blue @a[tag=mg.play]
execute as @a[tag=mg.play] run tp @s @e[type=minecraft:marker,tag=mg.zrc,sort=random,limit=1]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
tag @a remove mg.zhit
advancement revoke @a only mg:infhit
