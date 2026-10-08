# Arène 18 « Grand terrain » (carte Paintball, centre 0 ~ 12700) : construction, perchoir, élimination, placement. Généré.
function mg:paintball/build_2
kill @e[type=minecraft:item,x=-42,y=70,z=12648,dx=84,dy=30,dz=104]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 105
scoreboard players set $pz mg.st 12700
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 12700
spreadplayers 0 12700 8 37 under 90 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:12700,r:37,u:90}
