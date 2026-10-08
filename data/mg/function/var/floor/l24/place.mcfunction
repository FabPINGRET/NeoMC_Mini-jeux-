# Sol 24 : perchoir, élimination, placement sur l’étage du haut. Généré.
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 90
scoreboard players set $pz mg.st 24300
scoreboard players set $yd mg.st 62
scoreboard players set $ky mg.st 62
scoreboard players set $nf mg.st 3
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 88 24300
spreadplayers 0 24300 3 28 under 82 false @a[tag=mg.play]
