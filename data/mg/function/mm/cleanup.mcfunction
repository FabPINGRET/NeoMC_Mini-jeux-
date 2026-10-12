function mg:mm/kill_all
effect clear @a[tag=mg.mmx] minecraft:glowing
team leave @a[team=mg_mm]
tag @a remove mg.mmm
tag @a remove mg.mmd
tag @a remove mg.mmhero
tag @a remove mg.mmx
scoreboard players reset * mg.mma
scoreboard players reset * mg.mmo
title @a reset
