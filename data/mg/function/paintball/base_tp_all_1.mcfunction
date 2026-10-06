# Paintball (carte 1) — place chaque équipe dans sa base
spreadplayers 0 12283 1 2 under 90 false @a[team=mg_red,tag=mg.play]
spreadplayers 0 12317 1 2 under 90 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ 0 0
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ 180 0
