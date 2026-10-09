# Toutes les 0,5 s : la radio s'allume en montant dans une voiture ou un hélico, s'éteint en descendant
execute as @e[type=minecraft:horse,tag=mg.gcarh] on passengers run tag @s add mg.gdrn
execute as @e[type=minecraft:happy_ghast,tag=mg.ghel] on passengers run tag @s add mg.gdrn
execute as @a[tag=mg.gdrn,tag=!mg.gdrv] at @s run function mg:gta/radio_on
execute as @a[tag=mg.gdrv,tag=!mg.gdrn] run function mg:gta/radio_off
tag @a remove mg.gdrn
