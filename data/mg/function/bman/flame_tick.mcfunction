scoreboard players remove @s mg.yt 1
execute positioned ~-0.5 ~ ~-0.5 as @a[tag=mg.play,gamemode=adventure,dx=0,dy=1,dz=0] run function mg:bman/hit
execute if score @s mg.yt matches 5 run particle minecraft:flame ~ ~0.5 ~ 0.3 0.3 0.3 0.02 6 force
execute if score @s mg.yt matches ..0 run kill @s
