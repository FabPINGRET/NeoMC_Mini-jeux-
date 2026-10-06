# Répartition des participants en équipes ($nt = nombre d'équipes, défini par l'appelant)
scoreboard players set $ti mg.st 0
execute as @a[tag=mg.play] run function mg:core/assign_one
