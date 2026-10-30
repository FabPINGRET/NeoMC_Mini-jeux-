execute at @n[tag=frostbyte_head,distance=0..] run particle minecraft:explosion ~ ~2 ~ 1 1 1 0 1 force
execute at @n[tag=frostbyte_forearm,distance=0..] run particle minecraft:explosion ~ ~2 ~ 1 1 1 0 1 force
execute as @n[tag=frostbyte_bicep,distance=0..] at @s positioned ~ ~2 ~ positioned ^ ^ ^2 run particle minecraft:explosion ~ ~ ~ 1 1 1 0 1 force

#execute at @n[tag=frostbyte_bicep] run playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 3 1
execute at @n[tag=frostbyte_bicep,distance=0..] run playsound minecraft:entity.firework_rocket.twinkle_far master @a[tag=mg.flw] ~ ~ ~ 5 0.5
