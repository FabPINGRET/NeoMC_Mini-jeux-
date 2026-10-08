# One in the Chamber — préparation (centre 0 ~ 5800)
execute if score $ar mg.st matches 1.. run return run function mg:var/mode/oitc_prepare
execute if score $om mg.st matches 1 run return run function mg:oitc/prepare_1
execute if score $om mg.st matches 2 run return run function mg:oitc/prepare_2
function mg:oitc/build
kill @e[distance=0..,type=minecraft:arrow]
kill @e[type=minecraft:item,x=-20,y=70,z=5780,dx=40,dy=30,dz=40]
scoreboard players reset @a mg.pk

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 5800

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 5800
scoreboard players set @a[tag=mg.play] mg.lv 3
scoreboard players set @a[tag=mg.play] mg.ok 0
scoreboard players set @a[tag=mg.play] mg.cd 0
spreadplayers 0 5800 5 10 under 90 false @a[tag=mg.play]
