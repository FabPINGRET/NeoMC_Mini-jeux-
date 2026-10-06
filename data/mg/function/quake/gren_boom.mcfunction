# Quakecraft — explosion (@s = marker, à sa position) : tue les joueurs à moins de 4,5 blocs (sauf le lanceur)
scoreboard players operation $cur mg.st = @s mg.gi
execute as @a[tag=mg.play] if score @s mg.gi = $cur mg.st run tag @s add mg.qsh
particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1
particle minecraft:flame ~ ~ ~ 1.5 1.5 1.5 0.1 60
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 1.5 1
execute if entity @a[tag=mg.qsh] as @a[tag=mg.play,tag=!mg.qsh,tag=!mg.prot,tag=!mg.qdd,distance=..4.5] run function mg:quake/hit
tag @a remove mg.qsh
kill @e[type=minecraft:snowball,tag=mg.grs,distance=..6]
kill @s
