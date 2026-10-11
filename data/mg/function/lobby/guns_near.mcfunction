# @s : présentoir ; un joueur qui marche dessus prend l'arme (une fois par passage)
scoreboard players operation $lgn mg.st = @s mg.st
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,distance=..1.1,tag=!mg.lgn] run function mg:lobby/guns_give
tag @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,distance=..1.1] add mg.lgn2
