# Fin de la boutique : reprise du déplacement, ou arrivée si c'était la dernière case
execute if score $mpr mg.st matches ..0 as @a[tag=mg.mpcur] run return run function mg:party/land
scoreboard players set $mph mg.st 3
scoreboard players set $mpw mg.st 10
