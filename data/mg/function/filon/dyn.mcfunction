# 🧨 Dynamite : seulement dans la mine, sous la surface (les murs du puits protègent l'île)
execute unless entity @s[x=0,y=39,z=46000,dx=15,dy=55,dz=15] run return run title @s actionbar {"text":"🧨 Seulement dans la mine, au moins 4 blocs sous la surface.","color":"red"}
execute anchored eyes positioned ^ ^ ^1.2 run summon minecraft:tnt ~ ~-0.5 ~ {fuse:40,Tags:["mg.fntnt"]}
clear @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data~{fn_dyn:1b}] 1
title @s actionbar {"text":"🧨 Recule ! 2 secondes…","color":"red","bold":true}
