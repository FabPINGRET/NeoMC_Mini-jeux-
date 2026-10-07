# Dropper : Défi — préparation
function mg:dropadv/fl_add
scoreboard objectives add mg.dpw dummy [{"text":"⬇ Dropper : Défi","color":"aqua","bold":true}]
scoreboard objectives add mg.dlv dummy
scoreboard objectives add mg.dfl dummy
scoreboard players set @a[tag=mg.play] mg.dpw 0
scoreboard players set #k10 mg.st 10
scoreboard players set #k20 mg.st 20
scoreboard players set #k4 mg.st 4
scoreboard players set $dcr mg.st 0
scoreboard players set $dcl mg.st 0
scoreboard players set $dcph mg.st 0
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
scoreboard objectives setdisplay sidebar mg.dpw
function mg:dropadv/titles
function mg:dropadv/c_pick
scoreboard players set $dci mg.st 0
execute as @a[tag=mg.play] run function mg:dropadv/c_spawn
