# Flèche explosive (@s = la flèche) : explose au sol/mur ou à moins de 2,5 blocs d'un adversaire
execute on origin run tag @s add mg.osh
execute if data entity @s {inGround:1b} run return run function mg:oitc/ex_boom
execute if score @s mg.ag matches 3.. if entity @a[tag=mg.play,tag=!mg.osh,distance=..2.5] run return run function mg:oitc/ex_boom
tag @a remove mg.osh
