# Sumo — arène complexe pour beaucoup de joueurs (centre 0 ~ 5500)
function mg:sumo/disk_xl
kill @e[type=minecraft:item,x=-30,y=50,z=5470,dx=60,dy=60,dz=60]
scoreboard players set $sr2 mg.st 16
scoreboard players set $yd mg.st 72

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 5500

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 95 5500
scoreboard players set @a[tag=mg.play] mg.lv 3
spreadplayers 0 5500 2 13 under 90 false @a[tag=mg.play]
