# Arène 4 « Arène OITC » (carte One in the Chamber, centre 0 ~ 5800) : construction, perchoir, élimination, placement. Généré.
function mg:oitc/build
kill @e[type=minecraft:item,x=-20,y=70,z=5780,dx=40,dy=30,dz=40]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 5800
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 5800
spreadplayers 0 5800 5 10 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:5800,r:10,u:90}
