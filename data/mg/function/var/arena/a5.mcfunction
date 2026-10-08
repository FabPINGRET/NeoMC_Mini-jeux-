# Arène 5 « Château » (carte One in the Chamber, centre 0 ~ 11700) : construction, perchoir, élimination, placement. Généré.
function mg:oitc/build_1
kill @e[type=minecraft:item,x=-24,y=70,z=11676,dx=48,dy=40,dz=48]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 106
scoreboard players set $pz mg.st 11700
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 11716
spreadplayers 0 11700 5 17 under 84 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:11700,r:17,u:84}
