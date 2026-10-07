# Splegg XXL — préparation (centre 0 ~ 4600) : 3 étages, œufs qui cassent 3x3
function mg:splegg/build_xxl
kill @e[distance=0..,type=minecraft:egg]
kill @e[distance=0..,type=minecraft:chicken]
kill @e[type=minecraft:item,x=-50,y=50,z=4550,dx=100,dy=60,dz=100]

# Élimination sous le dernier étage (66)
scoreboard players set $yd mg.st 62

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 92
scoreboard players set $pz mg.st 4600

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 92 4600
spreadplayers 0 4600 5 27 under 85 false @a[tag=mg.play]
