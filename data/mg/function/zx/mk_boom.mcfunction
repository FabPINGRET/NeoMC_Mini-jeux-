# La grenade singe explose : zombies à 6 blocs tués (crédités au lanceur)
scoreboard players operation $zo mg.st = @s mg.zmo
execute as @a[tag=mg.play] if score @s mg.zid = $zo mg.st run tag @s add mg.gsh
scoreboard players set $gdm mg.st 1000000
execute as @e[tag=mg.zz,distance=..6] run function mg:gun/hit_mob
tag @a remove mg.gsh
particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force
particle minecraft:flame ~ ~ ~ 2 1 2 0.1 40 force
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 3 0.9
kill @s
