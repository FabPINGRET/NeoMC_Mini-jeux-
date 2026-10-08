# Arène 6 « Grande forêt » (carte One in the Chamber, centre 0 ~ 12000) : construction, perchoir, élimination, placement. Généré.
function mg:oitc/build_2
kill @e[type=minecraft:item,x=-40,y=70,z=11960,dx=80,dy=45,dz=80]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 110
scoreboard players set $pz mg.st 12000
scoreboard players set $ky mg.st 70
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 84 12000
spreadplayers 0 12000 8 30 under 86 false @a[tag=mg.play]
data modify storage mg:var a set value {x:0,z:12000,r:30,u:86}
