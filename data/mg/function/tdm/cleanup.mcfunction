# Fin de partie (appelée aussi après une annulation pendant la préparation : sans effet sur ce qui n'existe pas)
scoreboard players set $tma mg.st 0
kill @e[type=minecraft:marker,tag=mg.tmend]
kill @e[type=minecraft:item_display,tag=mg.tmhk]
execute as @e[type=minecraft:item,x=-22,y=60,z=39928,dx=44,dy=500,dz=945] if items entity @s contents *[custom_data~{mg_tm:1b}] run kill @s
title @a[tag=mg.play] clear
tag @a remove mg.tmsh
tag @a remove mg.tmen
tag @a remove mg.tmvc
tag @a remove mg.tmp
tag @a remove mg.tmsc
scoreboard players reset * mg.tmk
