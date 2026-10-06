# Armurerie : socles + utilisation des armes (appelé chaque tick après le setup)
execute as @a[tag=!mg.play,x=-13,y=63,z=-7,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_1
execute as @a[tag=!mg.play,x=-13,y=63,z=-3,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_2
execute as @a[tag=!mg.play,x=-13,y=63,z=1,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_3
execute as @a[tag=!mg.play,x=-13,y=63,z=5,dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_4

# Recharge de la baguette
scoreboard players remove @a[scores={mg.wd=1..}] mg.wd 1

# Utilisation (seulement dans le lobby, hors partie)
execute if score $state mg.st matches 0 as @a[scores={mg.qs=1..}] at @s run function mg:lobby/laser
execute if score $state mg.st matches 0 as @a[scores={mg.fw=1..}] at @s run function mg:lobby/wand
execute as @a[scores={mg.wc=1..}] run function mg:lobby/wind_used
execute if score $state mg.st matches 0 as @e[type=minecraft:snowball,tag=mg.sn] at @s run function mg:lobby/snow_tick
execute if score $state mg.st matches 0 as @a[scores={mg.us=1..}] at @s run function mg:lobby/snow_thrown
execute unless score $state mg.st matches 0 run scoreboard players reset @a mg.fw
