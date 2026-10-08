# Arène 7 « Néon » (carte Quakecraft, centre 0 ~ 7300) : construction, perchoir, élimination, placement. Généré.
function mg:quake/build
kill @e[type=minecraft:item,x=-20,y=70,z=7280,dx=40,dy=30,dz=40]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 7300
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 13 81 7313
spreadplayers 0 7300 5 13 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:7300,r:13,u:90}
