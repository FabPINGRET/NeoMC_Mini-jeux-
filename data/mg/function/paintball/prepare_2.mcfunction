# Paintball (carte 2) — préparation (centre 0 ~ 12700)
function mg:paintball/build_2
function mg:paintball/count_2
kill @e[distance=0..,type=minecraft:item]
scoreboard players reset @a mg.qs
tag @a remove mg.prot
tag @a remove mg.qsh
scoreboard players set $pa mg.st 0
scoreboard players set $pb mg.st 0
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 105
scoreboard players set $pz mg.st 12700
scoreboard players set $nt mg.st 2
function mg:core/assign_teams
gamemode adventure @a[tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] run spawnpoint @s 0 81 12653
execute as @a[team=mg_blue,tag=mg.play] run spawnpoint @s 0 81 12747
scoreboard players set @a[tag=mg.play] mg.ph 0
scoreboard players set @a[tag=mg.play] mg.pt 0
scoreboard players set @a[tag=mg.play] mg.pi 200
scoreboard players set @a[tag=mg.play] mg.cd 0
scoreboard players set @a[tag=mg.play] mg.deaths 0
function mg:paintball/base_tp_all
