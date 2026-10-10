# 🟩 Slime Jump — préparation
function mg:slimejump/build
function mg:slimejump/deco
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 122
scoreboard players set $pz mg.st 37860
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_sq @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.sjp 0
scoreboard players set $sjt mg.st 0
spreadplayers 0 37799 1 2 under 113 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run tp @s ~ ~ ~ 0 0
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
