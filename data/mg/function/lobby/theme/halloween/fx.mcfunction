# 🎃 Halloween : ambiance, chaque seconde
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:ash ~ ~3 ~ 8 3 8 0 25 normal @s
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:soul ~ ~0.3 ~ 6 0.5 6 0.01 2 normal @s
execute store result score $thr mg.st run random value 1..40
execute if score $thr mg.st matches 1 in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run playsound minecraft:ambient.cave ambient @s ~ ~ ~ 0.6 1
function mg:lobby/theme/halloween/mobs
