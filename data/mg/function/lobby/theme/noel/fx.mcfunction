# 🎄 Noël : ambiance, chaque seconde
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:snowflake ~ ~6 ~ 10 4 10 0 30 normal @s
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:white_ash ~ ~3 ~ 8 3 8 0 20 normal @s
execute store result score $thr mg.st run random value 1..45
execute if score $thr mg.st matches 1 in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run playsound minecraft:block.amethyst_block.chime ambient @s ~ ~2 ~ 1 0.8
function mg:lobby/theme/noel/mobs
