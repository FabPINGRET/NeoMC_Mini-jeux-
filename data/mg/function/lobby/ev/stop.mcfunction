# Fin (ou partie lancée) : tout ce que l'événement a posé disparaît
scoreboard players set $evon mg.st 0
bossbar remove mg:ev
kill @e[tag=mg.evx]
clear @a minecraft:gold_nugget[minecraft:custom_data~{mg_ev:1b}]
clear @a minecraft:gold_ingot[minecraft:custom_data~{mg_ev:1b}]
clear @a minecraft:iron_sword[minecraft:custom_data~{mg_ev:1b}]
