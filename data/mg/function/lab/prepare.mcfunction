# 🙈 Labyrinthe aveugle — préparation : labyrinthe au hasard, paires, téléportation
execute store result score $lbm mg.st run random value 0..2
function mg:lab/build
scoreboard players set $px mg.st 144
scoreboard players set $py mg.st 84
scoreboard players set $pz mg.st 38215
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_sq @a[tag=mg.play]
tag @a remove mg.lbw
tag @a remove mg.lbg
tag @a remove mg.lbx
scoreboard players reset * mg.lbp
scoreboard players set $lbn mg.st 0
function mg:lab/pair
execute as @a[tag=mg.play] run function mg:lab/place
