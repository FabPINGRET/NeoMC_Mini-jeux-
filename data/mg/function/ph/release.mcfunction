# Fin de la cachette : les chercheurs entrent
effect clear @a[tag=mg.phs] minecraft:blindness
spreadplayers 0 23600 1 4 under 85 false @a[tag=mg.phs]
execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~
title @a[tag=mg.play] title {"text":"Les chercheurs arrivent !","color":"red","bold":true}
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wolf.howl master @s ~ ~ ~ 0.7 1
