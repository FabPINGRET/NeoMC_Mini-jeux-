# 🔪 Murder Mystery — préparation : une carte de Prop Hunt au hasard, rôles secrets
execute store result score $mmm mg.st run random value 1..4
execute if score $mmm mg.st matches 1 run function mg:ph/build
execute if score $mmm mg.st matches 2 run function mg:ph/build2
execute if score $mmm mg.st matches 3 run function mg:ph/build3
execute if score $mmm mg.st matches 4 run function mg:ph/build4
function mg:mm/kill_all
scoreboard players set $px mg.st 0
execute if score $mmm mg.st matches 1 run scoreboard players set $py mg.st 95
execute if score $mmm mg.st matches 2 run scoreboard players set $py mg.st 100
execute if score $mmm mg.st matches 3 run scoreboard players set $py mg.st 94
execute if score $mmm mg.st matches 4 run scoreboard players set $py mg.st 96
execute if score $mmm mg.st matches 1 run scoreboard players set $pz mg.st 23600
execute if score $mmm mg.st matches 2 run scoreboard players set $pz mg.st 23700
execute if score $mmm mg.st matches 3 run scoreboard players set $pz mg.st 23800
execute if score $mmm mg.st matches 4 run scoreboard players set $pz mg.st 23900
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
tag @a[tag=mg.play] add mg.mmx
team join mg_mm @a[tag=mg.play]
execute if score $n0 mg.st matches 2.. as @a[tag=mg.play,sort=random,limit=1] run tag @s add mg.mmm
execute as @a[tag=mg.play,tag=!mg.mmm,sort=random,limit=1] run tag @s add mg.mmd
execute if score $mmm mg.st matches 1 run spreadplayers 0 23600 3 13 under 85 false @a[tag=mg.play]
execute if score $mmm mg.st matches 2 run spreadplayers 0 23700 3 14 under 90 false @a[tag=mg.play]
execute if score $mmm mg.st matches 3 run spreadplayers 0 23800 3 12 under 84 false @a[tag=mg.play]
execute if score $mmm mg.st matches 4 run spreadplayers 0 23900 3 13 under 87 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
