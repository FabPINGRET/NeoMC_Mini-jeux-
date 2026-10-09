# @s : conducteur d'une voiture lancée : renverse (6 dégâts) ce qui est juste devant
tag @s add mg.grd
execute on vehicle rotated as @s positioned ^ ^ ^1.8 as @e[tag=mg.gtg,tag=!mg.grd,tag=!mg.gcarh,distance=..1.5] run damage @s 6 minecraft:player_attack by @a[tag=mg.grd,limit=1]
tag @s remove mg.grd
