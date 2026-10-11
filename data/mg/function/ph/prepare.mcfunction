# 🎭 Prop Hunt, préparation : une carte au hasard
execute store result score $phm mg.st run random value 1..4
execute if score $phm mg.st matches 1 run function mg:ph/build
execute if score $phm mg.st matches 2 run function mg:ph/build2
execute if score $phm mg.st matches 3 run function mg:ph/build3
execute if score $phm mg.st matches 4 run function mg:ph/build4
function mg:ph/kill_all
scoreboard players set $px mg.st 0
execute if score $phm mg.st matches 1 run scoreboard players set $py mg.st 95
execute if score $phm mg.st matches 2 run scoreboard players set $py mg.st 100
execute if score $phm mg.st matches 3 run scoreboard players set $py mg.st 94
execute if score $phm mg.st matches 4 run scoreboard players set $py mg.st 96
execute if score $phm mg.st matches 1 run scoreboard players set $pz mg.st 23600
execute if score $phm mg.st matches 2 run scoreboard players set $pz mg.st 23700
execute if score $phm mg.st matches 3 run scoreboard players set $pz mg.st 23800
execute if score $phm mg.st matches 4 run scoreboard players set $pz mg.st 23900
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
tag @a[tag=mg.play] add mg.phx
execute store result score $phn mg.st if entity @a[tag=mg.play]
scoreboard players set #4 mg.st 4
scoreboard players operation $phn mg.st /= #4 mg.st
execute if score $phn mg.st matches ..0 run scoreboard players set $phn mg.st 1
execute if score $n0 mg.st matches 2.. run function mg:ph/pick
execute as @a[tag=mg.play,tag=!mg.phs] run tag @s add mg.phh
team join mg_red @a[tag=mg.phs]
team join mg_ph @a[tag=mg.phh]
execute if score $phm mg.st matches 1 run tp @a[tag=mg.phs] 0.5 89 23600.5
execute if score $phm mg.st matches 2 run tp @a[tag=mg.phs] 0.5 94 23700.5
execute if score $phm mg.st matches 3 run tp @a[tag=mg.phs] 0.5 88 23800.5
execute if score $phm mg.st matches 4 run tp @a[tag=mg.phs] 0.5 90 23900.5
execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~
execute if score $phm mg.st matches 1 run spreadplayers 0 23600 2 13 under 85 false @a[tag=mg.phh]
execute if score $phm mg.st matches 2 run spreadplayers 0 23700 2 14 under 90 false @a[tag=mg.phh]
execute if score $phm mg.st matches 3 run spreadplayers 0 23800 2 12 under 84 false @a[tag=mg.phh]
execute if score $phm mg.st matches 4 run spreadplayers 0 23900 2 13 under 87 false @a[tag=mg.phh]
execute as @a[tag=mg.phh] at @s run spawnpoint @s ~ ~ ~
