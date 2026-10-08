# Arène 17 « Mini-terrain » (carte Paintball, centre 0 ~ 12300) : construction, perchoir, élimination, placement. Généré.
function mg:paintball/build_1
kill @e[type=minecraft:item,x=-16,y=70,z=12279,dx=32,dy=30,dz=42]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 12300
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 12300
spreadplayers 0 12300 4 13 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:12300,r:13,u:90}
