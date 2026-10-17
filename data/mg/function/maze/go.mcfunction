# Départ : le sas s'ouvre (dès que le labyrinthe est fini de construire)
execute if score $jok mg.st matches 1 run function mg:maze/open
effect give @a[tag=mg.play] minecraft:night_vision infinite 0 true
scoreboard players set $jtm mg.st 0
