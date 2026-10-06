execute if score $sg mg.st matches 1 run return run function mg:dropper/prepare_s
# The Dropper — préparation (puits côte à côte le long de X, z = 5200) : un couloir par joueur
scoreboard players set $c8 mg.st 8
scoreboard players set $c4 mg.st 4
scoreboard players set $rd mg.st 1
scoreboard players set $dph mg.st 3
scoreboard players set $dtm mg.st 0
kill @e[type=minecraft:item,x=-20,y=50,z=5170,dx=140,dy=90,dz=60]

# Couloirs (12 max) et disposition aléatoire
function mg:dropper/build_shell
function mg:dropper/build_round

# Perchoir spectateur : au-dessus du milieu des couloirs
scoreboard players operation $px mg.st = $n0 mg.st
scoreboard players operation $px mg.st *= $c4 mg.st
scoreboard players set $py mg.st 135
scoreboard players set $pz mg.st 5200

gamemode adventure @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.dp 0
scoreboard players set @a[tag=mg.play] mg.cd 0
scoreboard players set $li mg.st 0
execute as @a[tag=mg.play] run function mg:dropper/assign_lane
