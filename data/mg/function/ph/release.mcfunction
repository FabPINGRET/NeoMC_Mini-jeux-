# Fin de la cachette : les chercheurs entrent
effect clear @a[tag=mg.phs] minecraft:blindness
execute if score $phm mg.st matches 1 run spreadplayers 0 23600 1 4 under 85 false @a[tag=mg.phs]
execute if score $phm mg.st matches 2 run spreadplayers 0 23700 1 4 under 90 false @a[tag=mg.phs]
execute if score $phm mg.st matches 3 run spreadplayers 0 23800 1 4 under 84 false @a[tag=mg.phs]
execute if score $phm mg.st matches 4 run spreadplayers 0 23900 1 4 under 87 false @a[tag=mg.phs]
execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~
title @a[tag=mg.play] title {"text":"Les chercheurs arrivent !","color":"red","bold":true}
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wolf.howl master @s ~ ~ ~ 0.7 1
