# Chaque seconde (lobby/theme/tick) : recharge des cadeaux, objets retirés aux joueurs occupés ailleurs
scoreboard players remove @a[scores={mg.thc=1..}] mg.thc 1
clear @a[tag=mg.play] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.ely] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.elyf] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.xso] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.lk] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.inplot] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.visit] *[minecraft:custom_data~{mg_thg:1b}]
