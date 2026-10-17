# Chaque seconde : toutes les 60 s, les joueurs en ligne hors partie reportent leurs victoires dans les top 3 du hall
scoreboard players add #t3t mg.st 1
execute if score #t3t mg.st matches ..59 run return 0
scoreboard players set #t3t mg.st 0
execute unless entity @e[type=minecraft:item_display,tag=mg.hallbuf] run return 0
execute as @a[tag=!mg.play] run function mg:hall/t3_all
