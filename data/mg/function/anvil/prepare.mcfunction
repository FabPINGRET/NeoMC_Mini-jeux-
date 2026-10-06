# Pluie d'Enclumes — préparation (centre 0 ~ 6700)
function mg:anvil/build
kill @e[tag=mg.sh]
kill @e[tag=mg.hl]
kill @e[type=minecraft:falling_block]
kill @e[type=minecraft:item,x=-20,y=60,z=6680,dx=40,dy=30,dz=40]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 6700
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 6700
spreadplayers 0 6700 3 8 under 90 false @a[tag=mg.play]
