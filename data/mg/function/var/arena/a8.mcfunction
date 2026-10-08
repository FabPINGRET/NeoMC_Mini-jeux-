# Arène 8 « Volcan » (carte Quakecraft, centre 0 ~ 7600) : construction, perchoir, élimination, placement. Généré.
function mg:quake/build_1
kill @e[type=minecraft:item,x=-34,y=70,z=7566,dx=68,dy=30,dz=68]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 7600
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 28 81 7628
spreadplayers 0 7600 8 28 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:7600,r:28,u:90}
