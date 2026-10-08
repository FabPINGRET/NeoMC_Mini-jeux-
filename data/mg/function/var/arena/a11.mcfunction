# Arène 11 « Glacier » (carte Quakecraft, centre 0 ~ 8500) : construction, perchoir, élimination, placement. Généré.
function mg:quake/build_4
kill @e[type=minecraft:item,x=-14,y=70,z=8486,dx=28,dy=30,dz=28]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 8500
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 7 81 8507
spreadplayers 0 8500 3 7 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:8500,r:7,u:90}
