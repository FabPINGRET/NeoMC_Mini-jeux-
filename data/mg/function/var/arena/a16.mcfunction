# Arène 16 « Terrain de paintball » (carte Paintball, centre 0 ~ 8800) : construction, perchoir, élimination, placement. Généré.
function mg:paintball/build
kill @e[type=minecraft:item,x=-28,y=70,z=8766,dx=56,dy=30,dz=68]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 8800
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 8800
spreadplayers 0 8800 6 22 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:8800,r:22,u:90}
