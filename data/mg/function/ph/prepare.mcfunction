# 🎭 Prop Hunt — préparation
function mg:ph/build
function mg:ph/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 23600
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
tag @a[tag=mg.play] add mg.phx
execute store result score $phn mg.st if entity @a[tag=mg.play]
scoreboard players set #4 mg.st 4
scoreboard players operation $phn mg.st /= #4 mg.st
execute if score $phn mg.st matches ..0 run scoreboard players set $phn mg.st 1
function mg:ph/pick
execute as @a[tag=mg.play,tag=!mg.phs] run tag @s add mg.phh
team join mg_red @a[tag=mg.phs]
team join mg_ph @a[tag=mg.phh]
tp @a[tag=mg.phs] 0.5 89 23600.5
execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~
spreadplayers 0 23600 2 13 under 85 false @a[tag=mg.phh]
execute as @a[tag=mg.phh] at @s run spawnpoint @s ~ ~ ~
