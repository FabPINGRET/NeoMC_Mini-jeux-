# Arène 3 « Nuketown » (carte PvP, centre 0 ~ 11500) : construction, perchoir, élimination, placement. Généré.
function mg:nuketown/build
kill @e[type=minecraft:item,x=-26,y=60,z=11474,dx=52,dy=40,dz=52]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 11500
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 11513
spreadplayers 0 11500 6 15 under 84 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:11500,r:15,u:84}
