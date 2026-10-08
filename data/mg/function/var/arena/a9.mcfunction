# Arène 9 « Jungle » (carte Quakecraft, centre 0 ~ 7900) : construction, perchoir, élimination, placement. Généré.
function mg:quake/build_2
kill @e[type=minecraft:item,x=-34,y=70,z=7866,dx=68,dy=30,dz=68]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 7900
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 28 81 7928
spreadplayers 0 7900 8 28 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:7900,r:28,u:90}
