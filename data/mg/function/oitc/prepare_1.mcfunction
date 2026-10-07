# One in the Chamber — préparation Château (centre 0 ~ 11700)
function mg:oitc/build_1
kill @e[distance=0..,type=minecraft:arrow]
kill @e[type=minecraft:item,x=-24,y=70,z=11676,dx=48,dy=40,dz=48]
scoreboard players reset @a mg.pk

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 106
scoreboard players set $pz mg.st 11700

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 11716
scoreboard players set @a[tag=mg.play] mg.lv 3
scoreboard players set @a[tag=mg.play] mg.ok 0
scoreboard players set @a[tag=mg.play] mg.cd 0
spreadplayers 0 11700 5 17 under 84 false @a[tag=mg.play]
