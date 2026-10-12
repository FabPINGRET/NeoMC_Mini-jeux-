# La roquette explose : 100 de dégâts dans un rayon de 4 (crédités au tireur)
scoreboard players operation $zo mg.st = @s mg.zmo
execute as @a[tag=mg.play] if score @s mg.zid = $zo mg.st run tag @s add mg.gsh
scoreboard players set $gdm mg.st 1000
execute as @e[tag=mg.zz,distance=..4] run function mg:gun/hit_mob
tag @a remove mg.gsh
particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force
particle minecraft:flame ~ ~ ~ 1.5 1.2 1.5 0.12 40 force
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 4 0.8
kill @s
