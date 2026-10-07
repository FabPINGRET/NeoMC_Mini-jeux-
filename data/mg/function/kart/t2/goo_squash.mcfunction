# Goomba (@s) percuté : le kart part en tête-à-queue, le Goomba est aplati 5 s
execute as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function mg:kart/t2/hz_hit
tag @s add mg.kdead
scoreboard players set @s mg.t 100
data merge entity @s {start_interpolation:0,interpolation_duration:3,transformation:{scale:[1.4f,0.25f,1.4f]}}
playsound minecraft:entity.slime.squish master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1.4
