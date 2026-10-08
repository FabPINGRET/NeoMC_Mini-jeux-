# Arène 2 « Mirage » (carte PvP, centre 0 ~ 11300) : construction, perchoir, élimination, placement. Généré.
function mg:mirage/build
kill @e[type=minecraft:item,x=-24,y=60,z=11276,dx=48,dy=40,dz=48]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 11300
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 11316
spreadplayers 0 11300 6 18 under 84 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:11300,r:18,u:84}
