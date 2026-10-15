# 🎄 Noël : ambiance, chaque seconde
execute if score $thi mg.st matches 1.. in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run function mg:lobby/theme/noel/fall
execute store result score $thr mg.st run random value 1..45
execute if score $thr mg.st matches 1 in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run playsound minecraft:block.amethyst_block.chime ambient @s ~ ~2 ~ 1 0.8
function mg:lobby/theme/noel/mobs
