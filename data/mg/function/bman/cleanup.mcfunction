# Fin de partie Bomberman
kill @e[type=!minecraft:player,x=-12,y=60,z=40689,dx=24,dy=15,dz=22]
clear @a *[custom_data~{ybomb:1b}]
effect clear @a[scores={mg.yv=1..}] minecraft:speed
scoreboard players reset * mg.yid
scoreboard players reset * mg.yn
scoreboard players reset * mg.yr
scoreboard players reset * mg.yv
scoreboard players reset * mg.yu
scoreboard players reset * mg.yh
scoreboard players reset * mg.ym
team leave @a[team=mg_sq]
data remove storage mg:ym r
