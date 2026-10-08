# Place chaque joueur sur un socle (rotation $hgi)
scoreboard players set $hgi mg.st 0
execute as @a[tag=mg.play,sort=random] run function mg:hg/place_one
