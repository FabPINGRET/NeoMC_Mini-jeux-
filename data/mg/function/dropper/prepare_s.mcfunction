# The Dropper (tube commun) — tout le monde saute dans le même puits (x 120, z 5203)
scoreboard players set $rd mg.st 1
scoreboard players set $dph mg.st 3
scoreboard players set $dtm mg.st 0
kill @e[type=minecraft:item,x=100,y=50,z=5170,dx=60,dy=90,dz=60]
execute positioned 120 58 5197 run function mg:dropper/shell_s
function mg:dropper/build_round_s

scoreboard players set $px mg.st 126
scoreboard players set $py mg.st 135
scoreboard players set $pz mg.st 5203

gamemode adventure @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.dp 0
scoreboard players set @a[tag=mg.play] mg.cd 0
scoreboard players set $li mg.st 0
execute as @a[tag=mg.play] run function mg:dropper/assign_lane
