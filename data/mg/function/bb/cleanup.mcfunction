# Fin de partie Build Battle : retire les entités posées par les joueurs
kill @e[type=!minecraft:player,tag=!mg.bbd,x=-140,y=0,z=13630,dx=280,dy=200,dz=145]
tag @a remove mg.bm
tag @a remove mg.bme
tag @a remove mg.brk
tag @a remove mg.bfar
scoreboard players reset @a mg.bi
scoreboard players reset @a mg.br
scoreboard players reset @a mg.ba
scoreboard players reset @a mg.bb
scoreboard players reset @a mg.bw
data remove storage mg:bb word
