# Explosion de la flèche (@s = la flèche, tireur marqué mg.osh) : tue tout adversaire à moins de 3,5 blocs
particle minecraft:explosion_emitter ~ ~ ~
particle minecraft:flame ~ ~ ~ 1 1 1 0.08 40
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 2 1.1
execute as @a[tag=mg.play,tag=!mg.osh,distance=..3.5] run function mg:oitc/ex_hit
tag @a remove mg.osh
kill @s
