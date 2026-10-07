# Temps écoulé : tous les blocs d'une autre couleur disparaissent
function mg:blockparty/strip
scoreboard players set $bp mg.st 2
scoreboard players set $bt mg.st 50
title @a[tag=mg.play] actionbar [{"text":"Les autres blocs disparaissent !","color":"red","bold":true}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.piston.contract master @s ~ ~ ~ 1 0.8
