# Sol 22 : perchoir, élimination, placement sur l’étage du haut. Généré.
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 94
scoreboard players set $pz mg.st 24300
scoreboard players set $yd mg.st 60
scoreboard players set $ky mg.st 60
scoreboard players set $nf mg.st 3
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 92 24300
spreadplayers 0 24300 3 12 under 86 false @a[tag=mg.play]
