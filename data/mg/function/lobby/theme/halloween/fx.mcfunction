# 🎃 Halloween : ambiance, chaque seconde
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:ash ~ ~3 ~ 8 3 8 0 25 normal @s
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:soul ~ ~0.3 ~ 6 0.5 6 0.01 2 normal @s
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:tinted_leaves{color:[0.93,0.45,0.08,1.0]} ~ ~7 ~ 10 3 10 0 5 normal @s
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:tinted_leaves{color:[0.78,0.16,0.08,1.0]} ~ ~7 ~ 10 3 10 0 3 normal @s
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:tinted_leaves{color:[0.95,0.72,0.15,1.0]} ~ ~7 ~ 10 3 10 0 3 normal @s
execute in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run particle minecraft:tinted_leaves{color:[0.52,0.30,0.14,1.0]} ~ ~7 ~ 10 3 10 0 2 normal @s
execute store result score $thr mg.st run random value 1..40
execute if score $thr mg.st matches 1 in minecraft:overworld as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run playsound minecraft:ambient.cave ambient @s ~ ~ ~ 0.6 1
function mg:lobby/theme/halloween/mobs
execute in minecraft:overworld unless score $thrs mg.st matches 1.. if loaded 22 64 22 unless entity @e[type=minecraft:interaction,tag=mg.thnpci] run function mg:lobby/theme/halloween/npc
execute in minecraft:overworld unless score $thrs mg.st matches 1.. if loaded 22 64 22 unless entity @e[tag=mg.thnpc,tag=mg.thmob] run function mg:lobby/theme/halloween/npc
