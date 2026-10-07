# Kart : préparation pendant le compte à rebours (zone chargée, pilotes sur la grille, karts posés 2 s après)
function mg:kart/const
function mg:kart/fl_add
scoreboard players set #km1 mg.st -1
scoreboard players set #k3 mg.st 3
scoreboard players set #k4 mg.st 4
scoreboard players set #k5 mg.st 5
scoreboard players set #k72 mg.st 72
scoreboard players set #k100 mg.st 100
scoreboard players set #k8 mg.st 8
scoreboard players set #k20 mg.st 20
scoreboard players set #k1000 mg.st 1000
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 110
scoreboard players set $pz mg.st 16500
scoreboard players set $ktime mg.st 0
scoreboard players set $kfo mg.st 0
scoreboard players set $kend mg.st 0
scoreboard players set $kph mg.st 0
scoreboard players set $gi mg.st 0
kill @e[tag=mg.ib]
kill @e[tag=mg.kpart]
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
tag @a remove mg.kfin
scoreboard players set @a[tag=mg.play] mg.ksp 0
scoreboard players set @a[tag=mg.play] mg.kdr 0
scoreboard players set @a[tag=mg.play] mg.kbo 0
scoreboard players set @a[tag=mg.play] mg.khi 0
scoreboard players set @a[tag=mg.play] mg.kst 0
scoreboard players set @a[tag=mg.play] mg.kit 0
scoreboard players set @a[tag=mg.play] mg.kcp 0
scoreboard players set @a[tag=mg.play] mg.klp 0
scoreboard players set @a[tag=mg.play] mg.kvy 0
scoreboard players set @a[tag=mg.play] mg.kfp 0
scoreboard players set @a[tag=mg.play] mg.kps 0
scoreboard players reset @a mg.qs
execute as @a[tag=mg.play] run function mg:kart/place_one
scoreboard objectives setdisplay sidebar mg.kps
schedule function mg:kart/place_all 40t
