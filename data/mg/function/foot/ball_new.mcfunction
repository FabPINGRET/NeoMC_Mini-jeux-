# Balle (sulfur_cube, bloc d'oak_planks en corps) au centre ; jamais mg.lby / mg.mob / mg.npc : les nettoyages du lobby la tueraient
summon minecraft:sulfur_cube 2.5 48 -30.5 {Tags:["mg.ball"],equipment:{body:{id:"minecraft:oak_planks",count:1}},Invulnerable:1b,PersistenceRequired:1b}
scoreboard players set $fti mg.ft 0
