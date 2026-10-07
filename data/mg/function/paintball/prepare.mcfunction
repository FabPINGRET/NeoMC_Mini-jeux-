# Paintball — préparation (centre 0 ~ 8800)
execute if score $pbm mg.st matches 1 run return run function mg:paintball/prepare_1
execute if score $pbm mg.st matches 2 run return run function mg:paintball/prepare_2
function mg:paintball/build
function mg:paintball/count
kill @e[distance=0..,type=minecraft:item]
scoreboard players reset @a mg.qs
tag @a remove mg.prot
tag @a remove mg.qsh
scoreboard players set $pa mg.st 0
scoreboard players set $pb mg.st 0
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 8800
scoreboard players set $nt mg.st 2
function mg:core/assign_teams
gamemode adventure @a[tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] run spawnpoint @s 0 81 8773
execute as @a[team=mg_blue,tag=mg.play] run spawnpoint @s 0 81 8827
scoreboard players set @a[tag=mg.play] mg.ph 0
scoreboard players set @a[tag=mg.play] mg.pt 0
scoreboard players set @a[tag=mg.play] mg.pi 200
scoreboard players set @a[tag=mg.play] mg.cd 0
scoreboard players set @a[tag=mg.play] mg.deaths 0
function mg:paintball/base_tp_all
