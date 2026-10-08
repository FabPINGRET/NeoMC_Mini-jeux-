# Arène 12 « Arène TNT Tag » (carte TNT Tag, centre 0 ~ 6100) : construction, perchoir, élimination, placement. Généré.
function mg:tnttag/build
kill @e[type=minecraft:item,x=-25,y=70,z=6075,dx=50,dy=30,dz=50]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 6100
scoreboard players set $ky mg.st 71
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 6100
spreadplayers 0 6100 4 13 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:6100,r:13,u:90}
