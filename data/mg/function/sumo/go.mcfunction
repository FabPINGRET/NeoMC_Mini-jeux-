# Sumo — début de partie
gamemode adventure @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.lv 3
# Aucun dégât : résistance totale (le recul du bâton, lui, fonctionne toujours) + faim/soin neutralisés
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute as @a[tag=mg.play] run function mg:sumo/kit
# Sumo : on affiche les vies restantes (sous le pseudo et dans la liste Tab) à la place des PV
scoreboard objectives setdisplay below_name mg.lv
scoreboard objectives setdisplay list mg.lv
tellraw @a[tag=mg.play] [{"text":"✊ SUMO ! Frappe tes adversaires avec ton bâton pour les éjecter de la plateforme. Pas de dégâts : 3 vies chacun, dernier debout = gagnant !","color":"gold"}]
