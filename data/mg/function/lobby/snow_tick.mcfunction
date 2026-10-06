# Boule de neige marquée en vol (@s = boule, position = boule) : touche un joueur ? → dégâts
scoreboard players set $snh mg.st 0
execute positioned ~-0.5 ~-0.5 ~-0.5 as @a[dx=0,dy=0,dz=0,tag=!mg.play,limit=1] run function mg:lobby/snow_hit
execute if score $snh mg.st matches 1 run kill @s
