# The Dropper : Aventure — préparation
function mg:dropadv/fl_add
scoreboard objectives add mg.dlv dummy [{"text":"⬇ Dropper : niveau","color":"aqua","bold":true}]
scoreboard objectives add mg.dfl dummy
scoreboard players set @a[tag=mg.play] mg.dlv 1
scoreboard players set @a[tag=mg.play] mg.dfl 0
scoreboard players set $dat mg.st 0
scoreboard players set #k10 mg.st 10
scoreboard players set #k20 mg.st 20
scoreboard players set #k1000 mg.st 1000
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
execute as @a[tag=mg.play] run function mg:dropadv/spawn
scoreboard objectives setdisplay sidebar mg.dlv
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 203
scoreboard players set $pz mg.st 23989
function mg:dropadv/titles
