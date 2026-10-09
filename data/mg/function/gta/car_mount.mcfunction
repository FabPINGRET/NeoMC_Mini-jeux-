# @s (joueur) : monte dans la voiture $gv (si personne ne la conduit)
execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gv mg.st run tag @s add mg.gmnt
ride @s mount @e[type=minecraft:horse,tag=mg.gmnt,limit=1]
tag @e remove mg.gmnt
