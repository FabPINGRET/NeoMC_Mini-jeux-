# Flamme dans cette case (0,5 s)
summon minecraft:marker ~ ~ ~ {Tags:["mg.yf","mg.yfn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.yfn] mg.yt 10
tag @e[tag=mg.yfn] remove mg.yfn
particle minecraft:explosion ~ ~0.6 ~ 0 0 0 0 1 force
particle minecraft:flame ~ ~0.6 ~ 0.3 0.4 0.3 0.03 10 force
kill @e[type=minecraft:item_display,tag=mg.yp,distance=..0.6]
execute positioned ~-0.5 ~ ~-0.5 as @a[tag=mg.play,gamemode=adventure,dx=0,dy=1,dz=0] run function mg:bman/hit
