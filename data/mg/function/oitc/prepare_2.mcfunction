# One in the Chamber — préparation Grande forêt (centre 0 ~ 12000)
function mg:oitc/build_2
kill @e[distance=0..,type=minecraft:arrow]
kill @e[type=minecraft:item,x=-40,y=70,z=11960,dx=80,dy=45,dz=80]
scoreboard players reset @a mg.pk

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 110
scoreboard players set $pz mg.st 12000

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 84 12000
scoreboard players set @a[tag=mg.play] mg.lv 3
scoreboard players set @a[tag=mg.play] mg.ok 0
scoreboard players set @a[tag=mg.play] mg.cd 0
spreadplayers 0 12000 8 30 under 86 false @a[tag=mg.play]
